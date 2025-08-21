from datetime import datetime
from typing import Optional, List

class Message:
    def __init__(self, id: Optional[int], conversation_id: int, sender_id: int, content: str, sent_at: Optional[datetime] = None):
        self.id = id
        self.conversation_id = conversation_id
        self.sender_id = sender_id
        self.content = content
        self.sent_at = sent_at if sent_at else datetime.utcnow()