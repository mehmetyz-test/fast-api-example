from pydantic import BaseModel


class TaskBase(BaseModel):
    """
        Schema de base d'une Tache (Task)
    """
    content: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config: #orm_mode permet de 
        orm_mode = True
