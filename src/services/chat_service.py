from domain.models.conversation import Conversation
from domain.models.message import Message
from infrastructure.repositories.ichat_repository import IChatRepository
from typing import List, Optional

class ChatService:
    def __init__(self, repository: IChatRepository):
        self.repository = repository

    def create_conversation(self, conversation_data: dict) -> Conversation:
        conversation = Conversation(id=None, **conversation_data)
        return self.repository.add_conversation(conversation)

    def list_conversations_for_user(self, user_id: int) -> List[Conversation]:
        # TODO: Lấy danh sách cuộc hội thoại của 1 user
        return self.repository.list_conversations_by_user(user_id)

    def send_message(self, conversation_id: int, message_data: dict) -> Message:
        message = Message(id=None, conversation_id=conversation_id, **message_data)
        return self.repository.add_message(message)

    def get_messages_by_conversation(self, conversation_id: int) -> List[Message]:
        return self.repository.list_messages_by_conversation(conversation_id)