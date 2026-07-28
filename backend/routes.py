from flask import Blueprint, request
from services.google_books import get_books
from services.gemini import get_study_plan
from models import db, SavedPlans


routes = Blueprint("routes", __name__)


@routes.get("/books")
def books():
    keyword = request.args.get("keyword")
    return get_books(keyword)


@routes.post("/plans/new")
def newPlan():
    body = request.get_json()
    return get_study_plan(body)


@routes.post("/plans/save")
def savePlan():
    body = request.get_json()        
    saved_plan = SavedPlans(plan=body["text"])
    db.session.add(saved_plan)
    db.session.commit()
    return {"id": saved_plan.id, "plan": saved_plan.plan, "createdAt": saved_plan.created_at, "updatedAt": saved_plan.updated_at}


@routes.get("/plans")
def getPlans():
    rows = db.session.scalars(db.select(SavedPlans)).all()
    return [{"id": row.id, "plan": row.plan, "createdAt": row.created_at, "updatedAt": row.updated_at} for row in rows]


@routes.get("/plans/<int:plan_id>")
def getPlan(plan_id):
    row = db.get_or_404(SavedPlans, plan_id)
    return {"id": row.id, "plan": row.plan, "createdAt": row.created_at, "updatedAt": row.updated_at}


@routes.patch("/plans/<int:plan_id>")
def updatePlan(plan_id):
    row = db.get_or_404(SavedPlans, plan_id)
    row.plan = request.get_json()["text"]
    db.session.commit()
    return {"id": row.id, "plan": row.plan, "createdAt": row.created_at, "updatedAt": row.updated_at}


@routes.delete("/plans/<int:plan_id>")
def deletePlan(plan_id):
    row = db.get_or_404(SavedPlans, plan_id)
    db.session.delete(row)
    db.session.commit()
    return ""
