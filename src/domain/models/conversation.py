from datetime import datetime
from typing import Optional, List

class Conversation:
    def __init__(self, id: Optional[int], participants: List[int]):
        self.id = id
        self.participants = participants