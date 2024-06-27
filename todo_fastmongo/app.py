from fastapi import FastAPI

from todo_fastmongo.routes import router as task_router

app = FastAPI()


@app.get('/')
def index():
    return {'acesse': 'localhost:8000/docs'}


app.include_router(task_router)
