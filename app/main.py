from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from . import models, database, schemas, auth
from .database import engine, SessionLocal

from sqlalchemy.exc import IntegrityError

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class TaskSchema(BaseModel):
    title: str
    description: str
    done: bool = False

class TaskOut(TaskSchema):
    id: int
    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/", response_model=TaskOut)
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=List[schemas.TaskOut])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)  # 👈 chỉ user đã login
):
    return db.query(models.Task).all()


@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(
        task_id: int,
        updated: TaskSchema,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(auth.get_current_user)
        ):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in updated.dict().items():
        setattr(task, key, value)
    db.commit()
    return task

@app.delete("/tasks/{task_id}", response_model=TaskOut)
def delete_task(
        task_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(auth.get_current_user)
        ):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return task


@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username already exists")

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
