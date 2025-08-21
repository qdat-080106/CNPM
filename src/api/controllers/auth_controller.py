from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from infrastructure.repositories.user_repository import UserRepository
from api.schemas.auth import RegisterSchema, LoginSchema, UserResponseSchema, UserUpdateSchema

bp = Blueprint('auth', __name__, url_prefix='/auth')
bp_user = Blueprint('user', __name__, url_prefix='/users')

auth_service = AuthService(UserRepository())
register_schema = RegisterSchema()
login_schema = LoginSchema()
user_response_schema = UserResponseSchema()
user_update_schema = UserUpdateSchema()

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = register_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    user = auth_service.register_user(data)
    return jsonify(user_response_schema.dump(user)), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    errors = login_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    token = auth_service.login_user(data)
    if not token:
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'token': token}), 200

@bp.route('/profile', methods=['GET'])
def get_profile():
    # Giả định có middleware để lấy user_id từ token JWT
    user_id = 1 # Thay thế bằng logic thực tế
    user = auth_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user_response_schema.dump(user)), 200

@bp_user.route('/', methods=['GET'])
def list_users():
    # Giả định có middleware để kiểm tra quyền Admin
    users = auth_service.list_all_users()
    return jsonify(user_response_schema.dump(users, many=True)), 200

@bp_user.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    errors = user_update_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    updated_user = auth_service.update_user(user_id, data)
    if not updated_user:
        return jsonify({'message': 'User not found or not authorized'}), 404
    return jsonify(user_response_schema.dump(updated_user)), 200