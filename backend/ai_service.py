import os

from dotenv import load_dotenv

try:
    from google import genai
except Exception:
    genai = None


load_dotenv()


TEXT_MODEL = "gemini-3.5-flash-lite"
IMAGE_MODEL = "gemini-3.5-flash-lite"


SYSTEM_PROMPT = """
You are a senior automobile technician and AI car mechanic.

Analyze the user's vehicle problem carefully.

Provide:

1. What the problem may indicate
2. Possible causes
3. Recommended checks
4. Recommended action
5. Safety warning if the vehicle may be unsafe to drive

Do not claim certainty when the available information is insufficient.

Ask relevant follow-up questions when necessary.

Only discuss automobile-related problems.
"""


IMAGE_PROMPT = """
You are a senior automobile technician and AI car mechanic.

Analyze the uploaded car image carefully.

Identify visible:

- Dashboard warning lights
- Engine components
- Tyre damage
- Brake-related visible problems
- Fluid leaks
- Smoke or visible damage
- Wiring issues
- Visible mechanical problems
- Other automobile-related issues

Do not claim certainty when the image is unclear.

Provide:

1. What is visible in the image
2. Possible problem
3. Possible causes
4. Recommended action
5. Safety warning if the issue may be dangerous

Only discuss automobile-related observations.
"""


def get_client():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    if genai is None:
        return None

    return genai.Client(
        api_key=api_key
    )


def gemini_answer(prompt: str) -> str:

    client = get_client()

    if client is None:
        return (
            "Gemini client is not available. "
            "Please check your .env file."
        )

    try:

        print(
            f"Gemini text request | model={TEXT_MODEL}"
        )

        response = client.models.generate_content(
            model=TEXT_MODEL,
            contents=[
                SYSTEM_PROMPT,
                "\nUser's car problem:\n",
                prompt
            ]
        )

        if response.text:
            return response.text.strip()

        return (
            "I need more information about "
            "your vehicle problem."
        )

    except Exception as error:

        print("Gemini text error:", error)

        return (
            "AI service is temporarily unavailable. "
            "Please try again."
        )


def gemini_image_analysis(image_path: str) -> str:

    client = get_client()

    if client is None:
        return (
            "Gemini client is not available. "
            "Please check your .env file."
        )

    try:

        print(
            f"Gemini image request | model={IMAGE_MODEL}"
        )

        image_file = client.files.upload(
            file=image_path
        )

        response = client.models.generate_content(
            model=IMAGE_MODEL,
            contents=[
                IMAGE_PROMPT,
                image_file
            ]
        )

        if response.text:
            return response.text.strip()

        return (
            "Unable to analyze the uploaded image."
        )

    except Exception as error:

        print(
            "Gemini image error:",
            error
        )

        return (
            "AI image analysis is temporarily unavailable. "
            "Please try again."
        )