from pathlib import Path

from app.config import settings


def ensure_directories() -> None:

    settings.panels_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    settings.exports_dir.mkdir(
        parents=True,
        exist_ok=True
    )


def safe_file_url(
    path: str
) -> str:

    file_path = Path(path)


    # PDF

    if (
        file_path.parent.resolve()
        ==
        settings.exports_dir.resolve()
    ):

        return (
            f"/download/"
            f"{file_path.name}"
        )


    # Generated images

    if (
        file_path.parent.resolve()
        ==
        settings.panels_dir.resolve()
    ):

        return (
            f"/static/panels/"
            f"{file_path.name}"
        )


    raise ValueError(
        "File is outside "
        "an allowed output directory."
    )