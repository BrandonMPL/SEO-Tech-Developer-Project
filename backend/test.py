import os
import unittest

from dotenv import load_dotenv
from google import genai
import requests
from sqlalchemy import text

from app import app
from models import db
from services.google_books import GOOGLE_BOOKS_URL


class ServiceTests(unittest.TestCase):

    def test_gemini_api_key(self):
        load_dotenv()
        client = genai.Client()
        self.assertIsNotNone(
            client.models.get(model="gemini-3.5-flash-lite")
        )


    def test_google_books_api_key(self):
        load_dotenv()
        key = os.getenv("GOOGLE_BOOKS_API_KEY")
        self.assertIsNotNone(key)

        response = requests.get(
            GOOGLE_BOOKS_URL,
            params={"q": "test", "key": key},
        )
        self.assertIn(response.status_code, (200, 503))


    # if the database is connected, return 1
    def test_sqlite_connection(self):
        with app.app_context():
            result = db.session.execute(text("SELECT 1")).scalar_one()
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
