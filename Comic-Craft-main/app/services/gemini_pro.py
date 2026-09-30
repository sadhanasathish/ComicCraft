def generate_story(data, outline):
    """
    Demo story generator.

    This version does NOT call Gemini.
    It works even when the Gemini API quota is exhausted.
    """

    character = data.character_name
    setting = data.setting
    tone = data.tone

    story = [
        {
            "panel_number": 1,
            "caption": f"A new adventure begins in {setting}.",
            "narration": (
                f"{character} starts an ordinary day, "
                "but something unusual is about to happen."
            ),
            "dialogue": [
                {
                    "speaker": character,
                    "line": "I wonder what will happen today!"
                }
            ],
        },
        {
            "panel_number": 2,
            "caption": "Something unexpected appears.",
            "narration": (
                f"{character} discovers something strange "
                f"while exploring {setting}."
            ),
            "dialogue": [
                {
                    "speaker": character,
                    "line": "Whoa! What is that?"
                }
            ],
        },
        {
            "panel_number": 3,
            "caption": "A problem suddenly appears.",
            "narration": (
                f"The unexpected discovery creates a problem, "
                f"and {character} must find a solution."
            ),
            "dialogue": [
                {
                    "speaker": character,
                    "line": "Okay, I need to solve this!"
                }
            ],
        },
        {
            "panel_number": 4,
            "caption": "An idea changes everything.",
            "narration": (
                f"{character} thinks carefully and decides "
                "to take action."
            ),
            "dialogue": [
                {
                    "speaker": character,
                    "line": "I have an idea!"
                }
            ],
        },
        {
            "panel_number": 5,
            "caption": "The adventure comes to an end.",
            "narration": (
                f"{character} successfully solves the problem "
                f"and finishes the adventure with a {tone.lower()} ending."
            ),
            "dialogue": [
                {
                    "speaker": character,
                    "line": "That was quite an adventure!"
                }
            ],
        },
    ]

    return story