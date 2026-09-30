import hashlib

# Базовый класс, представляющий пользователя.
class User:

    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):

        if not self.check_username(username):
            self.username = None
            print(f'Создание пользователя {username}: пользователь с таким именем уже существует')
            return

        if not self.check_password(password):
            self.username = None
            print(f'Создание пользователя {username}: пользователь с таким паролем уже существует')
            return

        self.address = None
        self.username = username
        self.email = email
        self.psw_hash = User.hash_password(password)

        self.users.append(self)

    def __str__(self):
        return f"Пользователь: {self.username}, email: {self.email}, адрес: {self.address}, хэш пароля: {self.psw_hash}"

    @staticmethod
    def get_user(username):
        return next((u for u in User.users if u.username.lower() == username.lower()), None)

    @staticmethod
    def hash_password(password):
        hash_obj = hashlib.sha256(password.encode('utf-8'))
        return hash_obj.hexdigest()

    # Проверка уникальности пароля
    @staticmethod
    def check_password(password):
        p_hash = User.hash_password(password)
        return all(user.psw_hash != p_hash for user in User.users)

    # Проверка уникальности имени пользователя
    @staticmethod
    def check_username(user_name):
        return all(user.username.lower() != user_name.lower() for user in User.users)

    def get_details(self):
        return f"Пользователь: {self.username}, email: {self.email}, хэш пароля: {self.psw_hash}"
