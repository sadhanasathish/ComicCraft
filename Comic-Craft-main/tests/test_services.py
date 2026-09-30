from pathlib import Path

from app.services.layout_builder import (
    build_comic_layout
)


def test_build_comic_layout():

    outline = [

        {
            "panel_number": i,
            "title": f"Title {i}",
            "scene_description": f"Scene {i}",
            "image_prompt": f"Prompt {i}",
        }

        for i in range(1, 6)
    ]


    story = [

        {
            "panel_number": i,

            "caption": f"Caption {i}",

            "narration":
                f"Narration {i}",

            "dialogue": [

                {
                    "speaker": "Maya",
                    "line": f"Line {i}"
                }

            ],
        }

        for i in range(1, 6)
    ]


    image_paths = [

        f"/tmp/panel_{i}.png"

        for i in range(1, 6)
    ]


    result = build_comic_layout(

        outline,

        story,

        image_paths
    )


    assert len(result) == 5

    assert (
        result[0]["panel_number"]
        == 1
    )

    assert (
        result[-1]["dialogue"][0]["line"]
        == "Line 5"
    )


def test_project_files_exist():

    assert Path(
        "templates/index.html"
    ).is_file()


    assert Path(
        "templates/comic_preview.html"
    ).is_file()


    assert Path(
        "static/css/style.css"
    ).is_file()