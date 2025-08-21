from marshmallow import Schema, fields

class ConversationRequestSchema(Schema):
    participants = fields.List(fields.Int(), required=True)

class ConversationResponseSchema(Schema):
    id = fields.Int(required=True)
    participants = fields.List(fields.Int(), required=True)

class MessageRequestSchema(Schema):
    content = fields.Str(required=True)
    sender_id = fields.Int(required=True)

class MessageResponseSchema(Schema):
    id = fields.Int(required=True)
    conversation_id = fields.Int(required=True)
    sender_id = fields.Int(required=True)
    content = fields.Str(required=True)
    sent_at = fields.Raw()