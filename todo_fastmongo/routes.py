from fastapi import APIRouter

from todo_fastmongo.database import collection
from todo_fastmongo.models import Task

router = APIRouter()


@router.post('/tasks/', response_model=Task)
async def create_task(task: Task):
    task_data = dict(task)
    collection.insert_one(task_data)
    task.created_at = task_data['created_at']
    return task
