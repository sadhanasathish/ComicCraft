from pathlib import Path
import re

from fpdf import FPDF

from app.config import settings


def _safe_filename(name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]+", "_", name).strip("_")
    return cleaned[:50] or "comic"


def _clean_text(value) -> str:
    """
    Convert any value to safe PDF text.
    Also breaks very long words so FPDF can wrap them.
    """
    if value is None:
        return ""

    text = str(value)

    # Replace characters that can cause problems with Helvetica
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")

    # Break extremely long words
    text = re.sub(r"([^\s]{40})(?=\S)", r"\1 ", text)

    return text.strip()


class ComicPDF(FPDF):

    def header(self):
        self.set_font("Helvetica", "B", 16)

        self.cell(
            0,
            10,
            "ComicCraft",
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )

        self.ln(2)


def write_text(pdf, text, bold=False, italic=False, size=10):
    """
    Safely write text into the PDF.
    """

    text = _clean_text(text)

    if not text:
        return

    style = ""

    if bold:
        style += "B"

    if italic:
        style += "I"

    pdf.set_font(
        "Helvetica",
        style,
        size,
    )

    pdf.multi_cell(
        0,
        6,
        text,
    )

    pdf.ln(1)


def save_pdf(layout: list[dict], character_name: str) -> str:

    settings.exports_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    pdf = ComicPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15,
    )

    for panel in layout:

        pdf.add_page()

        # Panel title
        write_text(
            pdf,
            f"Panel {panel.get('panel_number', '')}: "
            f"{panel.get('title', '')}",
            bold=True,
            size=14,
        )

        # Image
        image_path = Path(
            panel.get("image_path", "")
        )

        if image_path.is_file():

            pdf.image(
                str(image_path),
                x=15,
                w=180,
            )

            pdf.ln(4)

        # Scene description
        write_text(
            pdf,
            panel.get(
                "scene_description",
                "",
            ),
            italic=True,
            size=10,
        )

        # Caption
        caption = panel.get(
            "caption",
            "",
        )

        if caption:

            write_text(
                pdf,
                "Caption: " + _clean_text(caption),
                bold=True,
                size=10,
            )

        # Narration
        narration = panel.get(
            "narration",
            "",
        )

        if narration:

            write_text(
                pdf,
                "Narration: " + _clean_text(narration),
                size=10,
            )

        # Dialogue
        dialogue_list = panel.get(
            "dialogue",
            [],
        )

        if isinstance(dialogue_list, list):

            for dialogue in dialogue_list:

                if not isinstance(dialogue, dict):
                    continue

                speaker = _clean_text(
                    dialogue.get(
                        "speaker",
                        "Character",
                    )
                )

                line = _clean_text(
                    dialogue.get(
                        "line",
                        "",
                    )
                )

                if line:

                    write_text(
                        pdf,
                        f"{speaker}: {line}",
                        size=10,
                    )

    output = (
        settings.exports_dir
        / f"{_safe_filename(character_name)}_comic.pdf"
    )

    pdf.output(str(output))

    return str(output)