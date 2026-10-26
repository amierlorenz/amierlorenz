# Rebuilds the README's tech sections from the topics on my public repos.
# Run: GH_TOKEN=$(gh auth token) python3 .github/scripts/tech_badges.py
import base64, json, os, re, urllib.error, urllib.parse, urllib.request
from pathlib import Path

USER = "amierlorenz"
EXTRA_REPOS = ["CodePath-Tech-Exchange-CTEx/ise-genai-galea-digital"]  # public, but not under my account
# Work with no public repo. Shown in the matrix, counted in the totals.
OFFLINE = {"Google (Android XR)": ["java", "kotlin", "jetpack-compose"]}

# topic -> (badge label, color, simple-icons logo). Order here is display order.
TOPICS = {
    "swift": ("Swift", "F05138", "swift"),
    "python": ("Python", "3776AB", "python"),
    "kotlin": ("Kotlin", "7F52FF", "kotlin"),
    "java": ("Java", "ED8B00", "openjdk"),
    "swiftui": ("SwiftUI", "0D96F6", "swift"),
    "swiftdata": ("SwiftData", "1575F9", "swift"),
    "cloudkit": ("CloudKit", "3693F3", "icloud"),
    "vision": ("Vision", "5856D6", "swift"),
    "jetpack-compose": ("Jetpack Compose", "4285F4", "jetpackcompose"),
    "streamlit": ("Streamlit", "FF4B4B", "streamlit"),
    "foundation-models": ("Foundation Models", "000000", "swift"),
    "gemini-api": ("Gemini API", "8E75B2", "googlegemini"),
    "claude-code": ("Claude Code", "D97757", "claude"),
    "supabase": ("Supabase", "3FCF8E", "supabase"),
    "canvas-lms": ("Canvas API", "E72429", "canvas"),
    "pytest": ("pytest", "0A9EDC", "pytest"),
    "github-actions": ("GitHub Actions", "2088FF", "githubactions"),
}

README = Path(__file__).resolve().parents[2] / "README.md"


def api(path):
    req = urllib.request.Request(f"https://api.github.com/{path}", headers={"Accept": "application/vnd.github+json"})
    if token := os.environ.get("GH_TOKEN"):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def repos():
    """My public, non-fork repos (minus this profile repo) plus EXTRA_REPOS, as GitHub API objects."""
    own = [r for r in api(f"users/{USER}/repos?per_page=100") if not r["fork"] and not r["private"] and r["name"] != USER]
    return own + [api(f"repos/{r}") for r in EXTRA_REPOS]


def projects(repos):
    """{display name: (url or None, [mapped topics])}, only projects with at least one mapped topic."""
    out = {r["name"]: (r["html_url"], [t for t in TOPICS if t in r["topics"]]) for r in repos}
    out |= {name: (None, topics) for name, topics in OFFLINE.items()}
    return {k: v for k, v in out.items() if v[1]}


def search_url(topic):
    owners = [f"user:{USER}"] + [f"repo:{r}" for r in EXTRA_REPOS]
    return "https://github.com/search?type=repositories&q=" + urllib.parse.quote(f"topic:{topic} " + " ".join(owners))


def badge(topic, msg=None):
    """Linked shields.io badge. With msg, the brand color moves to the label and the message goes grey."""
    label, color, logo = TOPICS[topic]
    esc = lambda s: s.replace("-", "--").replace("_", "__").replace(" ", "_")
    if msg:
        src = f"https://img.shields.io/badge/{esc(label)}-{esc(msg)}-555555?style=flat-square&logo={logo}&logoColor=white&labelColor={color}"
    else:
        src = f"https://img.shields.io/badge/{esc(label)}-{color}?style=flat-square&logo={logo}&logoColor=white"
    return f"[![{label}]({src})]({search_url(topic)})"


def ranked(projs):
    """{topic: project count} for used topics, most-used first; ties keep TOPICS order."""
    used = {t: sum(t in ts for _, ts in projs.values()) for t in TOPICS}
    return {t: used[t] for t in sorted((t for t in TOPICS if used[t]), key=lambda t: -used[t])}


def counts(projs):
    """One badge per topic with how many projects use it."""
    return " ".join(badge(t, f"{n} project{'s' * (n > 1)}") for t, n in ranked(projs).items())


def matrix(projs):
    """Table: a row per topic (same order as counts), a column per project, ✅ where used."""
    names = list(projs)
    head = "| | " + " | ".join(f"[{n}]({u})" if u else n for n, (u, _) in projs.items()) + " |"
    rows = [f"| {badge(t)} | " + " | ".join("✅" if t in projs[n][1] else "" for n in names) + " |"
            for t in ranked(projs)]
    return "\n".join([head, "|---|" + ":-:|" * len(names), *rows])


def file_text(full, path):
    """A file's contents (or a folder's file names) on the default branch, or "" if it doesn't exist."""
    try:
        c = api(f"repos/{full}/contents/{path}")
        return " ".join(f["name"] for f in c) if isinstance(c, list) else base64.b64decode(c["content"]).decode()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return ""
        raise


def commits_mentioning(full, phrase):
    return api(f"search/commits?q={urllib.parse.quote(f'repo:{full} \"{phrase}\"')}")["total_count"]


def reminders(repos):
    """Topics a repo's code or history suggests but that aren't on the repo. Only suggests, never edits."""
    out = []
    for r in repos:
        full, have, found = r["full_name"], set(r["topics"]), {}
        langs = api(f"repos/{full}/languages")
        found |= {t: f"GitHub detects {label} code" for t, (label, _, _) in TOPICS.items() if label in langs}
        if any(commits_mentioning(full, p) for p in ("Co-Authored-By: Claude", "Claude Code")):
            found["claude-code"] = "commits credit Claude"
        if file_text(full, ".github/workflows"):
            found["github-actions"] = "has .github/workflows"
        if "Python" in langs:
            deps = (file_text(full, "requirements.txt") + file_text(full, "pyproject.toml")).lower()
            found |= {t: "listed in Python dependencies" for t in ("streamlit", "pytest") if t in deps}
        out += [f"- {r['name']}: add `{t}` ({why})" for t, why in found.items() if t not in have]
    return out


def fill(text, name, body):
    """Replace what's between <!-- name:start --> and <!-- name:end -->; leave the text alone if they're absent."""
    pat = re.compile(rf"(<!-- {name}:start -->\n).*?(<!-- {name}:end -->)", re.S)
    return pat.sub(lambda m: m[1] + body + "\n" + m[2], text)


assert fill("a\n<!-- x:start -->\nold\n<!-- x:end -->\nb", "x", "new") == "a\n<!-- x:start -->\nnew\n<!-- x:end -->\nb"
assert fill("a\n<!-- x:start -->\n<!-- x:end -->", "x", "new") == "a\n<!-- x:start -->\nnew\n<!-- x:end -->"
assert fill("no markers", "x", "new") == "no markers"

if __name__ == "__main__":
    rs = repos()
    projs = projects(rs)
    text = README.read_text()
    text = fill(text, "tech-counts", counts(projs))
    text = fill(text, "tech-by-project", matrix(projs))
    README.write_text(text)
    print("## Topic reminders", *(reminders(rs) or ["None, every repo's topics match what was found."]), sep="\n")
