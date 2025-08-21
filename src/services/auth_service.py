from domain.models.user import User
from infrastructure.repositories.iuser_repository import IUserRepository
from typing import Optional, List
import jwt

class AuthService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository
        # Secret key để tạo JWT, nên được lưu trong biến môi trường
        self.secret_key = 'your-super-secret-key'

    def register_user(self, user_data: dict) -> User:
        user = User(id=None, **user_data)
        # TODO: Mã hóa mật khẩu trước khi lưu
        return self.repository.add(user)

    def login_user(self, credentials: dict) -> Optional[str]:
        # TODO: Lấy user từ DB và kiểm tra mật khẩu
        user = self.repository.get_by_email(credentials.get('email'))
        if user and user.password == credentials.get('password'):
            # TODO: Tạo JWT token
            payload = {'user_id': user.id}
            token = jwt.encode(payload, self.secret_key, algorithm='HS256')
            return token
        return None
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    def list_all_users(self) -> List[User]:
        return self.repository.list()
    
    def update_user(self, user_id: int, user_data: dict) -> Optional[User]:
        user = self.repository.get_by_id(user_id)
        if user:
            # TODO: Cập nhật thông tin user và lưu vào DB
            # user.update_from_dict(user_data)
            return self.repository.update(user)
        return None