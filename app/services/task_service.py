from sqlalchemy.orm import Session
from app.repositories import task_repository
from app.schemas.task_schema import TaskCreate

def get_tasks(db: Session):
    return task_repository.get_all_tasks(db)

def create_task(db: Session, task: TaskCreate):
    return task_repository.create_task(db, task)

def complete_task(db: Session, task_id: int):
    return task_repository.mark_completed(db, task_id)
