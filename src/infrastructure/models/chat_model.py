from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class ConversationModel(Base):
    __tablename__ = 'conversations'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    # participants có thể lưu dưới dạng JSON hoặc liên kết với bảng phụ
    messages = relationship("MessageModel", back_populates="conversation")

class MessageModel(Base):
    __tablename__ = 'messages'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'))
    sender_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(255), nullable=False)
    sent_at = Column(DateTime)
    conversation = relationship("ConversationModel", back_populates="messages")