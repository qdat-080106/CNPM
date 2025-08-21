from flask import Blueprint, request, jsonify
from services.chat_service import ChatService
from infrastructure.repositories.chat_repository import ChatRepository
from api.schemas.chat import ConversationSchema, MessageSchema

bp = Blueprint('chat', __name__, url_prefix='/conversations')

chat_service = ChatService(ChatRepository())
conversation_schema = ConversationSchema()
message_schema = MessageSchema()

@bp.route('/', methods=['POST'])
def create_conversation():
    data = request.get_json()
    errors = conversation_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_conversation = chat_service.create_conversation(data)
    return jsonify(conversation_schema.dump(new_conversation)), 201

@bp.route('/', methods=['GET'])
def list_conversations():
    conversations = chat_service.list_conversations_for_user()
    return jsonify(conversation_schema.dump(conversations, many=True)), 200

@bp.route('/<int:conversation_id>/messages', methods=['POST'])
def send_message(conversation_id):
    data = request.get_json()
    errors = message_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_message = chat_service.send_message(conversation_id, data)
    return jsonify(message_schema.dump(new_message)), 201

@bp.route('/<int:conversation_id>/messages', methods=['GET'])
def get_messages(conversation_id):
    messages = chat_service.get_messages_by_conversation(conversation_id)
    return jsonify(message_schema.dump(messages, many=True)), 200