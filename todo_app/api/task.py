from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from todo_app import schemas, utils
from todo_app.dependencies import get_db


# On cree notre router
router = APIRouter(prefix="/api")

# On renvoie une liste de Tache
@router.get('/tasks', response_model=List[schemas.Task])
def get_items(db: Session = Depends(get_db)):
    """
        Return all task in database
    """
    items = utils.get_tasks(db)
    return items

@router.post('/create-task/', response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)) -> schemas.Task:
    """ 
        Create a task in database
            - task: TaskCreate Schema
        Return The Task Created
    """
    return utils.create_task(db, task=task)