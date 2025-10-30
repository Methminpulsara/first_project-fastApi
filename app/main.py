from fastapi import FastAPI
from app.controller import task_controller , user_controlller
from app.core.database import Base, engine

# create tables (development only)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API")


app.include_router(task_controller.router)
app.include_router(user_controlller.router)