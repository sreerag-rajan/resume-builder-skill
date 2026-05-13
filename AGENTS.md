# Agent Skills Index

This document acts as the index for available agent workflows/skills within the repository.

## 1. Resume Builder (`resume_builder`)

A modular, multi-agent workflow designed to generate ATS-optimized, high-quality resumes from raw data.

**How to Start**:
To initiate a resume building session, prompt the AI Agent to act as the `resume_builder` Conductor. 
Command: "Start the resume_builder skill. Act as the Conductor defined in `.agents/resume_builder/personas/conductor.md`."

### Architecture
The `resume_builder` skill comprises 7 specialized agents. The Conductor is responsible for reading the specialist files and switching personas to perform specific tasks.

Specialists are located in `.agents/resume_builder/`:
1. **[Conductor](file:///.agents/resume_builder/personas/conductor.md)**: Master orchestrator. Manages state, folders, and workflow sequence.
2. **[Data Gatherer](file:///.agents/resume_builder/personas/data_gatherer.md)**: Interacts with user to parse `raw/` files and fill missing gaps.
3. **[Domain Expert](file:///.agents/resume_builder/personas/domain_expert.md)**: Researches and ensures domain-specific accuracy (e.g., Data Analyst skills).
4. **[ATS Content Expert](file:///.agents/resume_builder/personas/ats_content_expert.md)**: Phrases achievements and structures content to guarantee an 80%+ ATS score.
5. **[ATS Formatter Expert](file:///.agents/resume_builder/personas/ats_formatter_expert.md)**: Enforces strict ATS formatting rules for the markdown output.
6. **[Tester](file:///.agents/resume_builder/personas/tester.md)**: Evaluates and scores the generated resume against ATS standards.
7. **[Outputter](file:///.agents/resume_builder/personas/outputter.md)**: Uses `pandoc` to generate final PDF and DOCX files.
