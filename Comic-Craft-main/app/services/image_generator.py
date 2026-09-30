from pathlib import Path
import re

from app.config import settings


def _safe_name(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_-]+", "_", value).strip("_")
    return value[:60] or "panel"


def generate_image(prompt: str, panel_number: int, art_style: str) -> str:
    """
    Generate a comic panel using Hugging Face.
    """

    try:
        from huggingface_hub import InferenceClient
    except ImportError as exc:
        raise RuntimeError(
            "Hugging Face package is not installed. "
            "Run: pip install huggingface_hub"
        ) from exc

    if not settings.hf_token:
        raise RuntimeError(
            "HF_TOKEN is missing from your .env file."
        )

    settings.panels_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output = (
        settings.panels_dir
        / f"panel_{panel_number}_{_safe_name(prompt)}.png"
    )

    full_prompt = (
        f"{art_style} comic book illustration, "
        f"{prompt}, "
        "cinematic composition, expressive character, "
        "detailed college environment, "
        "high quality, colorful, "
        "no text, no speech bubbles, no watermark"
    )

    client = InferenceClient(
        token=settings.hf_token
    )

    image = client.text_to_image(
        prompt=full_prompt,
        model="black-forest-labs/FLUX.1-schnell",
    )

    image.save(output)

    return str(output)