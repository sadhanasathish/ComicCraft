# ComicCraft

ComicCraft is an AI-powered five-panel comic generator.

The application uses:

- FastAPI
- Jinja2
- Gemini
- Diffusers
- Stable Diffusion
- Pillow
- FPDF

## Architecture

Browser

↓

FastAPI

↓

Gemini Flash

↓

Five-panel outline

↓

Gemini Pro

↓

Narration + dialogue

↓

Stable Diffusion / Diffusers

↓

Five panel images

↓

Layout builder

↓

PDF exporter

↓

Comic preview + PDF download


## Requirements

Python 3.10 or newer.

A Gemini API key is required.

A Hugging Face token may be required depending on the selected image model.

A capable GPU is strongly recommended for local Stable Diffusion generation.


# Installation

Create virtual environment:

```bash
python -m venv .venv