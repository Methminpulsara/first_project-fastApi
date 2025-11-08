from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories import user_repository
from app.core.security import *

def register_user(db: Session, username: str, email: str, password: str):
    existing_user = user_repository.get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    hashed_pw = hash_password(password)
    return user_repository.create_user(db, username, email, hashed_pw)


def user_login(db: Session, email: str, password: str):
    user = user_repository.get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, 'token_type': "bearer"}
