from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate

def get_all_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def mark_completed(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        db.commit()
        db.refresh(task)
    return task
