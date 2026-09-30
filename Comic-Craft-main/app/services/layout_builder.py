from pathlib import Path


def _story_for_panel(
    story: list[dict],
    number: int
) -> dict:

    for item in story:

        if item["panel_number"] == number:

            return item


    return {

        "panel_number": number,

        "caption": "",

        "narration": "",

        "dialogue": [],
    }


def build_comic_layout(
    outline: list[dict],
    story: list[dict],
    image_paths: list[str]
) -> list[dict]:

    if (
        len(outline) != 5
        or len(story) != 5
        or len(image_paths) != 5
    ):

        raise ValueError(
            "A comic must contain exactly five panels."
        )


    layout = []


    for index, panel in enumerate(
        outline
    ):

        number = index + 1


        narrative = _story_for_panel(
            story,
            number
        )


        image_path = Path(
            image_paths[index]
        )


        layout.append({

            "panel_number": number,

            "title": panel["title"],

            "scene_description":
                panel["scene_description"],

            "image_prompt":
                panel["image_prompt"],

            "image_url":
                f"/static/panels/"
                f"{image_path.name}",

            "caption":
                narrative["caption"],

            "narration":
                narrative["narration"],

            "dialogue":
                narrative["dialogue"],

            "image_path":
                str(image_path),
        })


    return layout