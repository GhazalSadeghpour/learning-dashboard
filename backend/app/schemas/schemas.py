from pydantic import BaseModel

class skill(BaseModel):
    id: id
    title: str
    subtitle: str | None = None
    percentage_done: float
    description: str | None = None
    archived: bool | None = False
    completed: bool | None = False

   