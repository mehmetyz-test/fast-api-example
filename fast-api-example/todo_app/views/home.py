from fastapi import Request, APIRouter
from . import templates

router = APIRouter()

@router.get('/', include_in_schema=False)
async def get_message(request: Request):
    return templates.TemplateResponse('index.html', {
        "request": request,
        "message": "Hello Dynamo"
    })