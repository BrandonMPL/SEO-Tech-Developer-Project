from flask import current_app

def get_study_plan(books):
    client = current_app.extensions["gemini"]

    prompt = f"""
    Given:
    {books}

    Write a day by day study plan with all of these books.
    The output must be in list form like this:

    Don't make the plans all about reading. Include review days and retest days as well.

    Day 1: plan here
    Day 2: plan here
    Day 3: plan here
    ...

    Keep the plan simple as possible
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )
    return response.text
