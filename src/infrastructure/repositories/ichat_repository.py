from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.conversation import Conversation
from domain.models.message import Message

class IChatRepository(ABC):
    @abstractmethod
    def add_conversation(self, conversation: Conversation) -> Conversation:
        pass

    @abstractmethod
    def list_conversations_by_user(self, user_id: int) -> List[Conversation]:
        pass

    @abstractmethod
    def add_message(self, message: Message) -> Message:
        pass

    @abstractmethod
    def list_messages_by_conversation(self, conversation_id: int) -> List[Message]:
        pass