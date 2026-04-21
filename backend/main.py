from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import get_db

app = FastAPI()

@app.get("/skills")
def get_skills(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT* FROM skills ORDER BY id"))
    rows = result.mappings().all()
    return [dict(row) for row in rows]