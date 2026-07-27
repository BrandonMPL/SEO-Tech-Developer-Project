from flask import Blueprint, request
from services.google_books import get_books

routes = Blueprint("routes", __name__)


@routes.get("/")
def home():
    return {"testing": "testing"}

@routes.get("/books")
def books():
    keyword = request.args.get("keyword")
    return get_books(keyword)

