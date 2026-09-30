import json

from app.config import settings
from app.schemas import PromptRequest


def generate_outline(data: PromptRequest) -> list[dict]:
    """
    Demo/local outline generator.

    This version does NOT call Gemini.
    It works even when Gemini API quota is exhausted.
    """

    character = data.character_name
    setting = data.setting
    tone = data.tone
    art_style = data.art_style
    story = data.story_prompt

    panels = [
        {
            "panel_number": 1,
            "title": "The Beginning",
            "scene_description": (
                f"{character} begins an unusual adventure in {setting}. "
                f"The story starts with: {story}"
            ),
            "image_prompt": (
                f"{character} in {setting}, beginning an adventure, "
                f"{tone} mood, {art_style} comic illustration"
            ),
        },
        {
            "panel_number": 2,
            "title": "Something Happens",
            "scene_description": (
                f"{character} discovers something unexpected while "
                f"exploring {setting}."
            ),
            "image_prompt": (
                f"{character} discovering something unexpected in {setting}, "
                f"expressive face, {tone} mood, {art_style} comic illustration"
            ),
        },
        {
            "panel_number": 3,
            "title": "The Problem",
            "scene_description": (
                f"A problem suddenly appears and {character} must find "
                f"a way to solve it."
            ),
            "image_prompt": (
                f"{character} facing a funny unexpected problem in {setting}, "
                f"dynamic scene, {tone} mood, {art_style} comic illustration"
            ),
        },
        {
            "panel_number": 4,
            "title": "The Turning Point",
            "scene_description": (
                f"{character} comes up with an idea and takes action "
                f"to overcome the problem."
            ),
            "image_prompt": (
                f"{character} taking action and solving a problem in {setting}, "
                f"dramatic comic composition, {tone} mood, "
                f"{art_style} comic illustration"
            ),
        },
        {
            "panel_number": 5,
            "title": "The Ending",
            "scene_description": (
                f"The adventure ends successfully and {character} "
                f"learns something from the experience."
            ),
            "image_prompt": (
                f"{character} celebrating after an adventure in {setting}, "
                f"happy ending, {tone} mood, {art_style} comic illustration"
            ),
        },
    ]

    return panels