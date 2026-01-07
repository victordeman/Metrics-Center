from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.project import ProjectCreate, Project
from app.schemas.evaluation import EvaluationCreate, Evaluation
from app.crud.project import create_project, get_projects, get_project
from app.crud.evaluation import create_evaluation, get_evaluations
from app.services.clustering import run_clustering
from app.services.visualization import generate_visualizations
from app.services.google_drive import import_from_google_drive
from app.utils.file_handler import handle_uploaded_file
from app.dependencies import get_db, get_current_user, get_background_tasks
from fastapi.background import BackgroundTasks

router = APIRouter()

@router.post("/", response_model=Project)
def create_new_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_project(db, project, current_user.id)

@router.get("/", response_model=List[Project])
def list_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_projects(db, current_user.id)

@router.post("/{project_id}/upload")
def upload_file(project_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = get_project(db, project_id, current_user.id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    file_path = handle_uploaded_file(file)
    # Update project with file_path (simplified)
    return {"message": "File uploaded", "file_path": file_path}

@router.post("/{project_id}/google-drive-import")
def google_drive_import(project_id: int, file_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = get_project(db, project_id, current_user.id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    file_path = import_from_google_drive(file_id)
    # Update project with file_path
    return {"message": "File imported from Google Drive", "file_path": file_path}

@router.post("/{project_id}/evaluate")
def evaluate_clustering(project_id: int, eval_data: EvaluationCreate, background_tasks: BackgroundTasks = Depends(get_background_tasks), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = get_project(db, project_id, current_user.id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    # Add background task for clustering
    background_tasks.add_task(run_clustering, db, project_id, eval_data, current_user.id)
    return {"message": "Evaluation started"}

@router.get("/{project_id}/results", response_model=List[Evaluation])
def get_results(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_evaluations(db, project_id, current_user.id)

@router.get("/{project_id}/download/{format}")
def download_results(project_id: int, format: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Implement download logic for CSV, PNG, PDF
    pass  # Placeholder
