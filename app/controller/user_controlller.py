from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, UserOut
from app.services import user_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/users", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/sing-up', response_model=UserOut)
def sing_up(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.register_user(db, user.username, user.email, user.password)


@router.post('/login')
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    return user_service.user_login(db, user.email, user.password)
