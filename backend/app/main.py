from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import get_db

app = FastAPI(title="CareerOS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "CareerOS Lite API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db-health")
def db_health_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).scalar()
    return {"database": "ok", "result": result}

@app.get("/skills")
def get_skills(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM skills"))
    skills = [dict(row) for row in result.mappings().all()]
    return {"Skills": skills}