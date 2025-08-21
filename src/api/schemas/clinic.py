from marshmallow import Schema, fields

class ClinicRequestSchema(Schema):
    name = fields.Str(required=True)
    address = fields.Str(required=True)

class ClinicResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)

class ServiceRequestSchema(Schema):
    clinic_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str()

class ServiceResponseSchema(Schema):
    id = fields.Int(required=True)
    clinic_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str()