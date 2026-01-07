from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from app.models import Base

class Evaluation(Base):
    __tablename__ = "evaluations"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    algorithm = Column(String)
    hyperparameters = Column(JSON)
    metrics = Column(JSON)
    visualizations = Column(JSON)
    project = relationship("Project", back_populates="evaluations")
