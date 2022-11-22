from fastapi.templating import Jinja2Templates

# On sert nos fichiers HTML dans ...
templates = Jinja2Templates(directory="templates")

from .home import router as home_router