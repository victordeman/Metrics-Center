from pydantic import BaseModel
from typing import List
from .evaluation import Evaluation

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    evaluations: List[Evaluation] = []

    class Config:
        from_attributes = True
