from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
# Import more as needed
from sqlalchemy.orm import Session
from app.crud.evaluation import create_evaluation
from app.services.visualization import generate_visualizations
import pandas as pd

def run_clustering(db: Session, project_id: int, eval_data: EvaluationCreate, user_id: int):
    # Load data from project file_path (placeholder)
    data = pd.read_csv("path/to/file.csv")  # Implement properly
    X = data.values  # Assume numerical data

    # Run clustering based on algorithm
    if eval_data.algorithm == "KMeans":
        model = KMeans(**eval_data.hyperparameters)
    elif eval_data.algorithm == "DBSCAN":
        model = DBSCAN(**eval_data.hyperparameters)
    elif eval_data.algorithm == "Agglomerative":
        model = AgglomerativeClustering(**eval_data.hyperparameters)
    # Add more

    labels = model.fit_predict(X)

    # Compute metrics
    metrics = {
        "silhouette": silhouette_score(X, labels),
        "davies_bouldin": davies_bouldin_score(X, labels),
        "calinski_harabasz": calinski_harabasz_score(X, labels),
        # Dunn Index, etc.
    }

    # Generate visualizations
    vis = generate_visualizations(X, labels)

    # Save evaluation
    eval_obj = Evaluation(algorithm=eval_data.algorithm, hyperparameters=eval_data.hyperparameters, metrics=metrics, visualizations=vis)
    create_evaluation(db, eval_obj, project_id)
