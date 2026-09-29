import hashlib
import uuid

# Базовый класс, представляющий пользователя.
class User:

    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        pass

    @staticmethod
    def hash_password(password):
        pass

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """

    def get_details(self):
        pass