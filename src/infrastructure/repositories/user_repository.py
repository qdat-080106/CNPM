from domain.models.user import User
from .iuser_repository import IUserRepository
from typing import List, Optional
from infrastructure.models.user_model import UserModel

# Đây là một repository đơn giản, không dùng database
class UserRepository(IUserRepository):
    def __init__(self):
        self._users = []
        self._id_counter = 1

    def add(self, user: User) -> User:
        user.id = self._id_counter
        self._id_counter += 1
        self._users.append(user)
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def get_by_email(self, email: str) -> Optional[User]:
        for user in self._users:
            if user.email == email:
                return user
        return None

    def list(self) -> List[User]:
        return self._users

    def update(self, user: User) -> User:
        for idx, u in enumerate(self._users):
            if u.id == user.id:
                self._users[idx] = user
                return user
        raise ValueError('User not found')

    def delete(self, user_id: int) -> None:
        self._users = [u for u in self._users if u.id != user_id]