from flask import Flask
from extensions import db
from models import TestItem # for app_context() to detect new tables


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.route("/")
def home():
    return "Flask application is running"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=8000)