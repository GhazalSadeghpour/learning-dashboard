from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/skills")
def get_skills(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT* FROM skills ORDER BY id"))
    rows = result.mappings().all()
    return [dict(row) for row in rows]