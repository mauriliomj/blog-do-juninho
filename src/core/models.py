from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Post:
    id: Optional[int] = None
    title: str = ""
    content: str = ""
    author: User = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
