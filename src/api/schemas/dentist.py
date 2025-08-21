from marshmallow import Schema, fields

class DentistResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    specialty = fields.Str()

class AvailabilitySchema(Schema):
    start_time = fields.Str(required=True)
    end_time = fields.Str(required=True)
    date = fields.Str(required=True)