from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SavedPlans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now(),
        nullable=False,
    )
