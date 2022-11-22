from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine

# Creation de la base de donnees
models.Base.metadata.create_all(bind=engine)

# On cree notre app
app = FastAPI()

# On sert nos fichiers statiques dans ...
app.mount('/static', StaticFiles(directory="static"), name="static")

# On importe nos routes
from .api import task_router
from .views import home_router

# On inclus les routes
app.include_router(task_router)
app.include_router(home_router)