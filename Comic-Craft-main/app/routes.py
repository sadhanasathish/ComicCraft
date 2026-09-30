from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import settings
from app.schemas import ImageTestRequest, PromptRequest

from app.services.exporters import save_pdf
from app.services.gemini_flash import generate_outline
from app.services.gemini_pro import generate_story
from app.services.image_generator import generate_image
from app.services.layout_builder import build_comic_layout

from app.utils.files import safe_file_url


BASE_DIR = Path(__file__).resolve().parent.parent


templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


router = APIRouter()


# ============================================================
# VALIDATION
# ============================================================

def _validate_prompt_size(*values: str) -> None:

    for value in values:

        if len(value) > settings.max_prompt_length:

            raise HTTPException(
                status_code=400,
                detail="One of the inputs is too long."
            )


# ============================================================
# COMPLETE COMIC GENERATION PIPELINE
# ============================================================

def _generate_comic(data: PromptRequest):

    _validate_prompt_size(
        data.story_prompt,
        data.character_name,
        data.setting,
        data.tone,
        data.art_style,
    )

    # --------------------------------------------------------
    # STEP 1: Gemini Flash
    # Generate 5-panel outline
    # --------------------------------------------------------

    outline = generate_outline(data)


    # --------------------------------------------------------
    # STEP 2: Gemini Pro
    # Generate narration/dialogue
    # --------------------------------------------------------

    story = generate_story(
        data,
        outline
    )


    # --------------------------------------------------------
    # STEP 3: Image generation
    # --------------------------------------------------------

    image_paths = []

    for panel in outline:

        image_path = generate_image(
            prompt=panel["image_prompt"],
            panel_number=panel["panel_number"],
            art_style=data.art_style,
        )

        image_paths.append(image_path)


    # --------------------------------------------------------
    # STEP 4: Build final layout
    # --------------------------------------------------------

    layout = build_comic_layout(
        outline,
        story,
        image_paths
    )


    # --------------------------------------------------------
    # STEP 5: Export PDF
    # --------------------------------------------------------

    pdf_path = save_pdf(
        layout,
        data.character_name
    )


    return layout, pdf_path


# ============================================================
# HOME PAGE
# ============================================================

@router.get(
    "/",
    response_class=HTMLResponse
)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "ComicCraft"
        },
    )


# ============================================================
# HTML COMIC GENERATION
# ============================================================

@router.post(
    "/generate",
    response_class=HTMLResponse
)
async def generate(

    request: Request,

    story_prompt: Annotated[
        str,
        Form(...)
    ],

    character_name: Annotated[
        str,
        Form(...)
    ],

    setting: Annotated[
        str,
        Form(...)
    ],

    tone: Annotated[
        str,
        Form(...)
    ],

    art_style: Annotated[
        str,
        Form(...)
    ],
):

    try:

        data = PromptRequest(
            story_prompt=story_prompt,
            character_name=character_name,
            setting=setting,
            tone=tone,
            art_style=art_style,
        )

        layout, pdf_path = _generate_comic(data)


        return templates.TemplateResponse(
            request=request,

            name="comic_preview.html",

            context={
                "title": "Comic Preview",
                "layout": layout,
                "pdf_url": safe_file_url(pdf_path),
            },
        )


    except HTTPException:

        raise


    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=f"Comic generation failed: {exc}"
        ) from exc


# ============================================================
# JSON API
# ============================================================

@router.post(
    "/generate-comic/json"
)
async def generate_comic_json(
    data: PromptRequest
):

    try:

        layout, pdf_path = _generate_comic(data)


        return {
            "success": True,

            "layout": layout,

            "pdf_url": safe_file_url(
                pdf_path
            ),
        }


    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=f"Comic generation failed: {exc}"
        ) from exc


# ============================================================
# IMAGE TEST API
# ============================================================

@router.post(
    "/test-image"
)
async def test_image(
    data: ImageTestRequest
):

    try:

        path = generate_image(
            prompt=data.prompt,
            panel_number=0,
            art_style="comic book",
        )


        return {
            "success": True,
            "image_url": safe_file_url(path),
        }


    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=f"Image generation failed: {exc}"
        ) from exc


# ============================================================
# DOWNLOAD PDF
# ============================================================

@router.get(
    "/download/{filename}"
)
async def download(
    filename: str
):

    candidate = (
        settings.exports_dir /
        Path(filename).name
    ).resolve()


    export_dir = (
        settings.exports_dir.resolve()
    )


    if (
        export_dir not in candidate.parents
        or not candidate.is_file()
    ):

        raise HTTPException(
            status_code=404,
            detail="Export not found."
        )


    return FileResponse(
        path=str(candidate),

        media_type="application/pdf",

        filename=candidate.name,
    )


# ============================================================
# SUCCESS PAGE
# ============================================================

@router.get(
    "/export-success",
    response_class=HTMLResponse
)
async def export_success(
    request: Request
):

    return templates.TemplateResponse(
        request=request,

        name="export_success.html",

        context={
            "title": "Export Complete"
        },
    )