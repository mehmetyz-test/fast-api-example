
try:
    import tracepointdebug
    tracepointdebug.start()
except ImportError as e:
    pass
    

import uvicorn
from todo_app import app


if __name__ == "__main__":
    uvicorn.run(app)