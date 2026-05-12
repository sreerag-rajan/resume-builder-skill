# Resume Builder Agentic Skill

Welcome to the `resume_builder` skill! This project acts as a multi-agent orchestrated workflow designed to generate highly optimized, ATS-friendly resumes (scoring >80% on platforms like Resume Worded) using specialized AI personas.

## How It Works

The workflow is managed by a **Conductor** agent that dynamically pulls in the expertise of 5 other specialist agents located in the `.agents/resume_builder/` directory:

1. **Data Gatherer**: Analyzes your raw input and interviews you to fill information gaps (especially quantifiable impact).
2. **Domain Expert**: Researches your target role and ensures industry-specific keywords and tools are emphasized.
3. **ATS Content Expert**: Rewrites your experience and summary using strict ATS-friendly formulas and strong action verbs.
4. **ATS Formatter Expert**: Structures the text into an ATS-parseable markdown format (no tables, standard headings).
5. **Outputter**: Converts the markdown into a clean PDF and DOCX using `pandoc`.

## Directory Structure

- `raw/`: **(Your Input)** Place your old resume, LinkedIn export, or any raw career notes here.
- `internal/`: **(System Use)** The Conductor uses this directory to manage session state (`status.md`, `thoughts.md`, `data.md`).
- `output/`: **(Your Output)** The finalized `.md`, `.pdf`, and `.docx` resumes will be saved here.
- `.agents/`: Contains the modular instructions for each specialist agent.

## Getting Started

### Prerequisites
- **Python**: Python 3.x must be installed on your system.
- **Pandoc**: Make sure you have [Pandoc](https://pandoc.org/) installed on your machine for document conversion.
- **WeasyPrint** (Optional): If PDF generation via HTML is used, WeasyPrint is required. 
- Python dependencies are listed in `.agents/resume_builder/skill-requirement.txt`.

### Instructions

1. **Setup**:
   - Clone this repository.
   - Ensure the `.agents` folder is kept intact as it contains all the agent instructions and python scripts.
   - A virtual environment (`venv`) will be created automatically by the Outputter agent to install the necessary dependencies.

2. **Provide Your Data**:
   - Place your existing resume or raw career information (in `.txt`, `.md`, or `.pdf` format) inside the `raw/` directory.

3. **Initiate the Workflow**:
   - Open this workspace in your IDE with your AI Assistant enabled.
   - Prompt the AI Assistant with the following command to begin:
     
     > "Start the resume_builder skill. Act as the Conductor defined in `.agents/resume_builder/conductor.md`."

4. **Collaborate**:
   - The Conductor will initialize the session and switch between various expert personas.
   - It will interview you to fill in information gaps, ensuring your resume includes quantifiable metrics and impact data to achieve a >80% ATS score. Simply answer its questions naturally!

5. **Retrieve Output**:
   - Once the workflow finishes, your polished resume will be available in the `output/` folder in `.md`, `.pdf`, and `.docx` formats.
