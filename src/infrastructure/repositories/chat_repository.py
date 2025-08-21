from domain.models.conversation import Conversation
from domain.models.message import Message
from .ichat_repository import IChatRepository
from typing import List, Optional

class ChatRepository(IChatRepository):
    def __init__(self):
        self._conversations = []
        self._messages = []
        self._conversation_id_counter = 1
        self._message_id_counter = 1

    def add_conversation(self, conversation: Conversation) -> Conversation:
        conversation.id = self._conversation_id_counter
        self._conversation_id_counter += 1
        self._conversations.append(conversation)
        return conversation

    def list_conversations_by_user(self, user_id: int) -> List[Conversation]:
        return [c for c in self._conversations if user_id in c.participants]

    def add_message(self, message: Message) -> Message:
        message.id = self._message_id_counter
        self._message_id_counter += 1
        self._messages.append(message)
        return message

    def list_messages_by_conversation(self, conversation_id: int) -> List[Message]:
        return [m for m in self._messages if m.conversation_id == conversation_id]