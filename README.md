# ComicCraft Submission Package

## Project
**ComicCraft – AI Comic Story Creator**

**Team ID:** `6ab2240ffc67a5bc0222524ef`

### Team
- Jennet Mercy A — Team Leader
- Prasanna P
- Sadana S
- Sadana D
- Anushiya A

## Package structure
This submission combines the original ComicCraft source project with the phase-wise documentation structure used by the supplied reference template.

- `Comic-Craft-main/` — original project source, tests, README and configuration
- `1. Brainstorming & Ideation/` — ideation, problem statement and empathy artifacts
- `2. Requirement Analysis/` — journey map, DFD, requirements and technology stack
- `3. Project Design Phase/` — problem-solution fit, proposed solution and architecture
- `4. Project Planning Phase/` — backlog, sprint planning and estimates
- `5. Project Development Phase/` — code quality, coding solution and functional features
- `6.Project Testing/` — performance/testing plan
- `7.Project Documentation/` — executable files checklist and project documentation
- `8.Project Demonstration/` — communication, demo, planning, scalability and team involvement

## Accuracy note
The documentation is related to the supplied ComicCraft source. It does not claim that the packaged `gemini_flash.py` or `gemini_pro.py` are currently making live Gemini API calls: those modules explicitly contain demo/local generators. The configuration contains Gemini model settings, while the supplied image generator uses Hugging Face `InferenceClient` with `black-forest-labs/FLUX.1-schnell`.

## Run
From `Comic-Craft-main`:

```bash
python -m venv comiccraft-env
# Windows:
comiccraft-env\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

Keep API tokens/secrets in a local `.env` file and do not commit them.
