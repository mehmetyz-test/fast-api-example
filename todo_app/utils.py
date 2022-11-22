# Session permettra de déclarer le type des paramètres db 
# et d'avoir de meilleurs contrôles de type et complétion dans vos fonctions.
from sqlalchemy.orm import Session
from todo_app import models, schemas


def get_tasks(db: Session):
    """ 
        Return All Task in Database 
    """
    return db.query(models.Task).all()


def create_task(db: Session, task: schemas.TaskCreate) -> schemas.Task:
    """
        Create a Task in database
            - task: TaskCreate
    """
    task_data = models.Task(content=task.content) #on recupere le contenu pour creer le modele
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return task_data