from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

@dataclass
class TodoTest:
    id: uuid4
    title: str
    desc: str
    is_complete: bool
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
