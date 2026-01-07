from pydantic import BaseModel
from typing import Dict

class EvaluationCreate(BaseModel):
    algorithm: str
    hyperparameters: Dict[str, any]

class Evaluation(BaseModel):
    id: int
    algorithm: str
    hyperparameters: Dict[str, any]
    metrics: Dict[str, float]
    visualizations: Dict[str, str]  # JSON for Plotly or paths

    class Config:
        from_attributes = True
