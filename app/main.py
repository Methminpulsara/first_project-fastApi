from fastapi import FastAPI
from app.controller import task_controller
from app.core.database import Base, engine

# create tables (development only)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API")

app.include_router(task_controller.router)
