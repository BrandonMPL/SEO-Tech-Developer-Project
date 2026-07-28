import os
import requests

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"

# always pass a list of books in this format
FALLBACK_BOOKS = [
    {
        "title": "Book of Proof",
        "authors": ["Richard Hammack"]
    },
    {
        "title": "Mathematics for Computer Science",
        "authors": ["Eric Lehman", "F. Thomson Leighton", "Albert R. Meyer"]
    },
    {
        "title": "Introduction to Linear Algebra",
        "authors": ["Gilbert Strang"]
    },
    {
        "title": "Introduction to Probability",
        "authors": ["Joseph K. Blitzstein", "Jessica Hwang"]
    },
    {
        "title": "OpenStax Calculus Volume 1",
        "authors": ["Gilbert Strang", "Edwin Herman"]
    },
    {
        "title": "OpenStax Calculus Volume 2",
        "authors": ["Gilbert Strang", "Edwin Herman"]
    },
    {
        "title": "OpenStax Calculus Volume 3",
        "authors": ["Gilbert Strang", "Edwin Herman"]
    },
    {
        "title": "How to Prove It",
        "authors": ["Daniel J. Velleman"]
    },
    {
        "title": "Concrete Mathematics",
        "authors": ["Ronald L. Graham", "Donald E. Knuth", "Oren Patashnik"]
    },
    {
        "title": "Linear Algebra Done Right",
        "authors": ["Sheldon Axler"]
    }
]


def get_books(keyword):
    params = {
        "q": keyword,
        "key": os.getenv("GOOGLE_BOOKS_API_KEY"),
        "maxResults": 10
    }

    try:
        response = requests.get(GOOGLE_BOOKS_URL, params=params)
        data = response.json()
        response.raise_for_status()
    except Exception as error:
        print(error)
        return FALLBACK_BOOKS
        
    books = []
    for item in data.get("items", []):
        volume_info = item.get("volumeInfo", {})

        books.append({
            "title": volume_info.get("title", "Unknown title"),
            "authors": volume_info.get("authors", ["Unknown author"]),
        })

    return books
