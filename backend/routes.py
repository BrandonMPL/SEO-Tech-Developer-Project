from flask import Blueprint, request
from services.google_books import get_books
from services.gemini import get_study_plan
from models import db, SavedPlans


routes = Blueprint("routes", __name__)


# URL: GET http://localhost:8000/books?keyword=math
# JSON body: none
# Returns: JSON list of {"title": string, "authors": [string]}
@routes.get("/books")
def books():
    keyword = request.args.get("keyword")
    return get_books(keyword)


# URL: POST http://localhost:8000/plans/new
# JSON body: [{"title": "Book title", "authors": ["Author name"]}]
# Returns: plain text containing the generated study plan with gemini API
@routes.post("/plans/new")
def newPlan():
    body = request.get_json()
    return get_study_plan(body)


# URL: POST http://localhost:8000/plans/save
# JSON body: {"text": "Study plan text"}
# Returns: JSON object with id, plan, createdAt, and updatedAt
@routes.post("/plans/save")
def savePlan():
    body = request.get_json()        
    saved_plan = SavedPlans(plan=body["text"])
    db.session.add(saved_plan)
    db.session.commit()
    return {"id": saved_plan.id, "plan": saved_plan.plan, "createdAt": saved_plan.created_at, "updatedAt": saved_plan.updated_at}


# URL: GET http://localhost:8000/plans
# JSON body: none
# Returns: JSON list of plan objects with id, plan, createdAt, and updatedAt
@routes.get("/plans")
def getPlans():
    rows = db.session.scalars(db.select(SavedPlans)).all()
    return [{"id": row.id, "plan": row.plan, "createdAt": row.created_at, "updatedAt": row.updated_at} for row in rows]


# URL: GET http://localhost:8000/plans/<plan_id>
# JSON body: none
# Returns: JSON object with id, plan, createdAt, and updatedAt
@routes.get("/plans/<int:plan_id>")
def getPlan(plan_id):
    row = db.get_or_404(SavedPlans, plan_id)
    return {"id": row.id, "plan": row.plan, "createdAt": row.created_at, "updatedAt": row.updated_at}


# URL: PATCH http://localhost:8000/plans/<plan_id>
# JSON body: {"text": "Updated study plan text"}
# Returns: JSON object with id, plan, createdAt, and updatedAt
@routes.patch("/plans/<int:plan_id>")
def updatePlan(plan_id):
    row = db.get_or_404(SavedPlans, plan_id)
    row.plan = request.get_json()["text"]
    db.session.commit()
    return {"id": row.id, "plan": row.plan, "createdAt": row.created_at, "updatedAt": row.updated_at}


# URL: DELETE http://localhost:8000/plans/<plan_id>
# JSON body: none
# Returns: empty response
@routes.delete("/plans/<int:plan_id>")
def deletePlan(plan_id):
    row = db.get_or_404(SavedPlans, plan_id)
    db.session.delete(row)
    db.session.commit()
    return ""
