from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    created_at: datetime = datetime.now()
    completed: bool = False
