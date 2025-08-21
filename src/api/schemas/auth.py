from marshmallow import Schema, fields

class RegisterSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    name = fields.Str()

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class UserResponseSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Email(required=True)
    name = fields.Str()
    role = fields.Str() # Guest/Customer/Dentist/Owner/Admin
    created_at = fields.Raw()
    updated_at = fields.Raw()

class UserUpdateSchema(Schema):
    name = fields.Str()
    password = fields.Str()