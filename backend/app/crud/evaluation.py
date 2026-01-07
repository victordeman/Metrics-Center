from sqlalchemy.orm import Session
from app.models.evaluation import Evaluation
from app.schemas.evaluation import EvaluationCreate

def create_evaluation(db: Session, evaluation: Evaluation, project_id: int):
    db_eval = Evaluation(**evaluation.dict(), project_id=project_id)
    db.add(db_eval)
    db.commit()
    db.refresh(db_eval)
    return db_eval

def get_evaluations(db: Session, project_id: int, user_id: int):
    # Join with project to check ownership
    return db.query(Evaluation).join(Project).filter(Evaluation.project_id == project_id, Project.user_id == user_id).all()
