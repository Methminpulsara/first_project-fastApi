from sqlalchemy.orm import Session
from app.repositories import task_repository
from app.schemas.task_schema import TaskCreate
from app.models.task import Task


def get_tasks(db: Session):
    return task_repository.get_all_tasks(db)


def create_task(db: Session, task_data:TaskCreate, current_user):
    task = Task(title=task_data.title, user_id=current_user.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def complete_task(db: Session, task_id: int):
    return task_repository.mark_completed(db, task_id)
