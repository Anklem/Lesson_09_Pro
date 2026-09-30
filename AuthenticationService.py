# Сервис для управления регистрацией и аутентификацией пользователей.
from admin import Admin
from customer import Customer
from user import User

class AuthenticationService:

    def __init__(self):
        self.current_user = None  # Текущий вошедший пользователь

    # Регистрация нового пользователя
    def register(self, username, email, password, address, is_admin=False):
        if is_admin:
            return Admin(username, email, password, address)
        else:
            return Customer(username, email, password, address)

    # Аутентификация пользователя
    def login(self, username, password):

        login_user = User.get_user(username)
        if login_user is None:
            print(f"Регистрация: Ошибка: пользователь '{username}' не существует")
            return

        if not User.check_password(password):
            print(f"Регистрация: Ошибка: пользователь '{username}' ввел неправильный пароль")
            return

        self.current_user = login_user
        print(f"Регистрация: Пользователь '{username}' успешно зарегистрирован!\nДетали: {login_user.get_details()}")

    # Выход пользователя из системы
    def logout(self):
        print("Разрегистрация текущего пользователя")
        self.current_user = None

    # Возвращает текущего вошедшего пользователя
    def get_current_user(self):
        return "Активного пользователя нет" if self.current_user is None else self.current_user
