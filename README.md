## Hi, I'm Amier Lorenz Davis 👋

<!-- TODO(issue): add headshot. Drop it in this repo as headshot.jpg, then uncomment:
<img align="right" src="headshot.jpg" width="200" alt="Amier Davis">
-->

**CS: AI/ML Student @ Hampton University[^1][^2]**

[![Follow on GitHub](https://img.shields.io/github/followers/amierlorenz?label=Follow&style=social)](https://github.com/amierlorenz)
[![Book a chat](https://img.shields.io/badge/-Book_a_chat-4285F4?style=flat-square&logo=googlecalendar&logoColor=white)](https://calendar.app.google/cnMKfDF11F9o77mK7)

### AboutMe.swift

```swift
struct Amier: Student, Builder, Teacher, Mentor {
    let student = Student(
        at: "Hampton University",
        degree: .bs(.computerScience, concentration: .aiML),
        graduating: .spring(2028),
        gpa: 3.9
    )

    var currentlyWorkingOn: [Project] = [
        .course(
            "CodePath AI301",
            goal: .firstOpenSourcePR(repo: "codepath/pathreview"),
            building: .claudeCodeSkills([
                // skills to assist in making contributions to Open Source
                "issue-select",
                "repro-check",
                "plan-check",
                "pr-precheck",
            ])
        ),
        .app(
            "MieracleStudy",
            platforms: [.iPhone, .mac],
            features: [
                .spacedRepetition(.sm2),
                .onDeviceAIGrading,
                .canvasIntegration,
            ]
        ),
    ]

    let experience: [Role] = [
        Role(
            "Research Assistant",
            at: "Hampton University",
            program: "Google REACH",
            project: "SafeGenAI",
            researching: [.genAISecurity, .misinformation, .privacy, .bias],
            building: [.riskFramework, .safeguardMatrix, .communityWorkshops],
            when: .fall(2026) ... .now
        ),
        Role(
            "Associate Software Developer Intern",
            at: "Google",
            team: "Android XR",
            built: .aiPoweredUserJourneys(
                count: 2,
                extending: .glassesPhotography
            ),
            used: [.java, .kotlin, .jetpackCompose, .aiAssistedCoding],
            demoedTo: [.directors, .seniorEngineeringManagers],
            wrote: [.designDocs, .implementationDocs],
            when: .summer(2025)
        ),
    ]

    let community: [Role] = [
        Role(
            "HECSA Swift Outreach Scholar",
            at: "Hampton University",
            teaching: .swift,
            to: [.k12, .undergrad, .grad, .staff, .community],
            when: .fall(2026) ... .now
        ),
        Role(
            "President-in-training",
            at: ("ACM", chapter: .hamptonUniversity),
            when: .fall(2026) ... .now
        ),
        Role(
            "Teaching Assistant",
            at: "Hampton University",
            classes: ["Computer Programming I", "Computer Programming II"],
            students: 50...,
            when: .fall(2025) ... .spring(2026)
        ),
    ]

    let honors: Set<Honor> = [
        .hackathon(place: 1, event: "ADMI AI Conference", year: 2026),
        .fullRideScholarship,
        .deansList,
    ]
}
```

<div align="center">

### 🛠️ Tech I Use[^3]

<!-- tech-counts:start -->
[![Swift](https://img.shields.io/badge/Swift-4_projects-555555?style=flat-square&logo=swift&logoColor=white&labelColor=F05138)](https://github.com/search?type=repositories&q=topic%3Aswift%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![SwiftUI](https://img.shields.io/badge/SwiftUI-4_projects-555555?style=flat-square&logo=swift&logoColor=white&labelColor=0D96F6)](https://github.com/search?type=repositories&q=topic%3Aswiftui%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![CloudKit](https://img.shields.io/badge/CloudKit-2_projects-555555?style=flat-square&logo=icloud&logoColor=white&labelColor=3693F3)](https://github.com/search?type=repositories&q=topic%3Acloudkit%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Foundation Models](https://img.shields.io/badge/Foundation_Models-2_projects-555555?style=flat-square&logo=swift&logoColor=white&labelColor=000000)](https://github.com/search?type=repositories&q=topic%3Afoundation-models%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Gemini API](https://img.shields.io/badge/Gemini_API-2_projects-555555?style=flat-square&logo=googlegemini&logoColor=white&labelColor=8E75B2)](https://github.com/search?type=repositories&q=topic%3Agemini-api%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Canvas API](https://img.shields.io/badge/Canvas_API-2_projects-555555?style=flat-square&logo=canvas&logoColor=white&labelColor=E72429)](https://github.com/search?type=repositories&q=topic%3Acanvas-lms%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Python](https://img.shields.io/badge/Python-1_project-555555?style=flat-square&logo=python&logoColor=white&labelColor=3776AB)](https://github.com/search?type=repositories&q=topic%3Apython%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Kotlin](https://img.shields.io/badge/Kotlin-1_project-555555?style=flat-square&logo=kotlin&logoColor=white&labelColor=7F52FF)](https://github.com/search?type=repositories&q=topic%3Akotlin%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Java](https://img.shields.io/badge/Java-1_project-555555?style=flat-square&logo=openjdk&logoColor=white&labelColor=ED8B00)](https://github.com/search?type=repositories&q=topic%3Ajava%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![SwiftData](https://img.shields.io/badge/SwiftData-1_project-555555?style=flat-square&logo=swift&logoColor=white&labelColor=1575F9)](https://github.com/search?type=repositories&q=topic%3Aswiftdata%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Vision](https://img.shields.io/badge/Vision-1_project-555555?style=flat-square&logo=swift&logoColor=white&labelColor=5856D6)](https://github.com/search?type=repositories&q=topic%3Avision%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Jetpack Compose](https://img.shields.io/badge/Jetpack_Compose-1_project-555555?style=flat-square&logo=jetpackcompose&logoColor=white&labelColor=4285F4)](https://github.com/search?type=repositories&q=topic%3Ajetpack-compose%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Streamlit](https://img.shields.io/badge/Streamlit-1_project-555555?style=flat-square&logo=streamlit&logoColor=white&labelColor=FF4B4B)](https://github.com/search?type=repositories&q=topic%3Astreamlit%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Claude Code](https://img.shields.io/badge/Claude_Code-1_project-555555?style=flat-square&logo=claude&logoColor=white&labelColor=D97757)](https://github.com/search?type=repositories&q=topic%3Aclaude-code%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![Supabase](https://img.shields.io/badge/Supabase-1_project-555555?style=flat-square&logo=supabase&logoColor=white&labelColor=3FCF8E)](https://github.com/search?type=repositories&q=topic%3Asupabase%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![pytest](https://img.shields.io/badge/pytest-1_project-555555?style=flat-square&logo=pytest&logoColor=white&labelColor=0A9EDC)](https://github.com/search?type=repositories&q=topic%3Apytest%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) [![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-1_project-555555?style=flat-square&logo=githubactions&logoColor=white&labelColor=2088FF)](https://github.com/search?type=repositories&q=topic%3Agithub-actions%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital)
<!-- tech-counts:end -->

</div>

<div align="center">

### 🛠️ Tech by Project[^3]

<details>
<summary><em>(click to expand)</em></summary>

<!-- tech-by-project:start -->
| | [archive-buddy](https://github.com/amierlorenz/archive-buddy) | [master-todo](https://github.com/amierlorenz/master-todo) | [mieracle-study](https://github.com/amierlorenz/mieracle-study) | [not-lang](https://github.com/amierlorenz/not-lang) | [skills](https://github.com/amierlorenz/skills) | [ise-genai-galea-digital](https://github.com/CodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) | Google (Android XR) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| [![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Aswift%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) | ✅ | ✅ | ✅ | ✅ |  |  |  |
| [![SwiftUI](https://img.shields.io/badge/SwiftUI-0D96F6?style=flat-square&logo=swift&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Aswiftui%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) | ✅ | ✅ | ✅ | ✅ |  |  |  |
| [![CloudKit](https://img.shields.io/badge/CloudKit-3693F3?style=flat-square&logo=icloud&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Acloudkit%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  | ✅ | ✅ |  |  |  |  |
| [![Foundation Models](https://img.shields.io/badge/Foundation_Models-000000?style=flat-square&logo=swift&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Afoundation-models%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) | ✅ |  | ✅ |  |  |  |  |
| [![Gemini API](https://img.shields.io/badge/Gemini_API-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Agemini-api%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  | ✅ |  | ✅ |  |
| [![Canvas API](https://img.shields.io/badge/Canvas_API-E72429?style=flat-square&logo=canvas&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Acanvas-lms%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  | ✅ | ✅ |  |  |  |  |
| [![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Apython%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  |  | ✅ |  |
| [![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Akotlin%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  |  |  | ✅ |
| [![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Ajava%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  |  |  | ✅ |
| [![SwiftData](https://img.shields.io/badge/SwiftData-1575F9?style=flat-square&logo=swift&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Aswiftdata%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  | ✅ |  |  |  |
| [![Vision](https://img.shields.io/badge/Vision-5856D6?style=flat-square&logo=swift&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Avision%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) | ✅ |  |  |  |  |  |  |
| [![Jetpack Compose](https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Ajetpack-compose%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  |  |  | ✅ |
| [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Astreamlit%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  |  | ✅ |  |
| [![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=claude&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Aclaude-code%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  | ✅ |  |  |
| [![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Asupabase%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  | ✅ |  |  |  |
| [![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Apytest%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  |  | ✅ |  |
| [![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/search?type=repositories&q=topic%3Agithub-actions%20user%3Aamierlorenz%20repo%3ACodePath-Tech-Exchange-CTEx/ise-genai-galea-digital) |  |  |  |  |  | ✅ |  |
<!-- tech-by-project:end -->

</details>

</div>

### 📫 Want to chat w/ me about anything?

Reach me at the email on [my GitHub profile](https://github.com/amierlorenz) or grab a slot below:

[![Book a 30-min chat](https://img.shields.io/badge/Book_a_30--min_chat-4285F4?style=for-the-badge&logo=googlecalendar&logoColor=white)](https://calendar.app.google/cnMKfDF11F9o77mK7)

:wq

[^1]: Class of '28
[^2]: The real HU
[^3]: Rebuilt daily from my repos' topics by a [GitHub Action](https://github.com/amierlorenz/amierlorenz/blob/main/.github/workflows/tech-badges.yml).
