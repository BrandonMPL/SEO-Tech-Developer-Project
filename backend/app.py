from flask import Flask
from dotenv import load_dotenv
from google import genai

from models import db, SavedPlans
from routes import routes

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

app.extensions["gemini"] = genai.Client()
app.register_blueprint(routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=8000)
