from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Task schemas
class TaskBase(BaseModel):
    title: str
    description: str
    done: bool = False

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True
