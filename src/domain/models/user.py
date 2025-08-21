from datetime import datetime
from typing import Optional

class User:
    def __init__(self, id: Optional[int], email: str, password: str, name: Optional[str] = None, role: str = "Customer", created_at: Optional[datetime] = None, updated_at: Optional[datetime] = None):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.role = role
        self.created_at = created_at if created_at else datetime.utcnow()
        self.updated_at = updated_at if updated_at else datetime.utcnow()