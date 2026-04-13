from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Skill(BaseModel):
    id: int
    title: str
    subtitle: Optional[str] = None
    percentage_done: float
    description: Optional[str] = None
    archived: bool = False
    completed: bool = False


class SkillsResponse(BaseModel):
    skills: List[Skill]


class StatCard(BaseModel):
    label: str
    value: int
    description: str


class SkillProgress(BaseModel):
    skill: str
    category: str
    progress: int
    nextStep: str


class ProjectCard(BaseModel):
    name: str
    stack: str
    status: str
    nextTask: str


class CurrentFocus(BaseModel):
    title: str
    summary: str
    thisWeek: List[str]
    nextStep: str


class WeeklyProgress(BaseModel):
    done: List[str]
    nextUp: List[str]


class DashboardResponse(BaseModel):
    title: str
    subtitle: str
    currentFocus: CurrentFocus
    stats: List[StatCard]
    skillsInProgress: List[SkillProgress]
    projects: List[ProjectCard]
    weeklyProgress: WeeklyProgress


skills_data = [
    {
        "id": 1,
        "title": "Angular",
        "subtitle": "Frontend",
        "percentage_done": 20,
        "description": "Building components, routing, and using Angular Material.",
        "archived": False,
        "completed": False,
    },
    {
        "id": 2,
        "title": "TypeScript",
        "subtitle": "Frontend",
        "percentage_done": 10,
        "description": "Learning strong typing, interfaces, and cleaner JavaScript development.",
        "archived": False,
        "completed": False,
    },
    {
        "id": 3,
        "title": "FastAPI",
        "subtitle": "Backend",
        "percentage_done": 30,
        "description": "Creating APIs, routes, and backend services with Python.",
        "archived": False,
        "completed": False,
    },
    {
        "id": 4,
        "title": "PostgreSQL",
        "subtitle": "Database",
        "percentage_done": 0,
        "description": "Working with relational databases, tables, and SQL queries.",
        "archived": False,
        "completed": False,
    },
]

dashboard_data = {
    "title": "Learning OS",
    "subtitle": "Track skills, projects, and progress in one place",
    "currentFocus": {
        "title": "Current Focus",
        "summary": "Building the Learning OS frontend and improving dashboard UX.",
        "thisWeek": [
            "Improve visual design",
            "Add progress tracking",
            "Simplify card actions"
        ],
        "nextStep": "Build the Skills page filters and improve card layout"
    },
    "stats": [
        {
            "label": "Active Skills",
            "value": 4,
            "description": "Frontend, backend, and database skills in progress"
        },
        {
            "label": "Projects in Progress",
            "value": 1,
            "description": "Learning OS"
        },
        {
            "label": "Certifications",
            "value": 2,
            "description": "AZ-104 and AZ-305 in progress"
        }
    ],
    "skillsInProgress": [
        {
            "skill": "Angular",
            "category": "Frontend",
            "progress": 35,
            "nextStep": "Refactor card layout and improve page structure"
        },
        {
            "skill": "TypeScript",
            "category": "Frontend",
            "progress": 20,
            "nextStep": "Add typed models for skill and project data"
        },
        {
            "skill": "FastAPI",
            "category": "Backend",
            "progress": 10,
            "nextStep": "Build the first GET /skills endpoint"
        },
        {
            "skill": "PostgreSQL",
            "category": "Database",
            "progress": 15,
            "nextStep": "Design the first app schema"
        }
    ],
    "projects": [
        {
            "name": "Learning OS",
            "stack": "Angular, FastAPI, PostgreSQL",
            "status": "In Progress",
            "nextTask": "Improve dashboard hierarchy and add progress bars"
        }
    ],
    "weeklyProgress": {
        "done": [
            "Built dashboard layout",
            "Created initial skill cards",
            "Committed version 1"
        ],
        "nextUp": [
            "Add progress bars",
            "Improve color system",
            "Build Skills page filters"
        ]
    }
}


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/skills", response_model=SkillsResponse)
def get_skills():
    return {"skills": skills_data}


@app.get("/dashboard", response_model=DashboardResponse)
def get_dashboard_data():
    return dashboard_data



@app.get("/skill/{id}", response_model = Skill)
def get_skill(id:int):
    for skill in skills_data:
        if skill["id"] == id:
            return skill
    return HTTPException(status_code=404, detail="Skill not found")
 