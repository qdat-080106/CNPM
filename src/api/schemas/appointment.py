from marshmallow import Schema, fields

class AppointmentRequestSchema(Schema):
    dentist_id = fields.Int(required=True)
    clinic_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    date = fields.Str(required=True)
    time = fields.Str(required=True)

class AppointmentResponseSchema(Schema):
    id = fields.Int(required=True)
    dentist_id = fields.Int(required=True)
    clinic_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    date = fields.Str(required=True)
    time = fields.Str(required=True)
    result = fields.Str()

class AppointmentResultSchema(Schema):
    result = fields.Str(required=True)