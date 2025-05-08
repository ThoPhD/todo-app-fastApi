from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TaskStatus(str):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELED = "canceled"
    FAILED = "failed"
    UNKNOWN = "unknown"

class Task(BaseModel):
    title: str
    description: str
    done: bool = False

tasks = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}/", response_model=Task)
def update_task(task_id: int, task: Task):
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}/", response_model=Task)
def delete_task(task_id: int):
    return tasks.pop(task_id)
