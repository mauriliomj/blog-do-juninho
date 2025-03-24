from src.infrastructure.models import UserModel
from django.contrib.auth.hashers import make_password

class UserService:
    @staticmethod
    def create_user(username: str, email: str, password: str):
        hashed_password = make_password(password)
        user = UserModel.objects.create(username = username, email = email, password = hashed_password)
        return user
