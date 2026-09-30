from user import User

class Admin(User):

    def __init__(self, username, email, password, address):

        super().__init__(username, email, password)
        if self.username is None: return

        self.address = address

        print("Создан администратор:", self.get_details())

    def get_details(self):
        return f"Администратор: {self.username}, Email: {self.email}, Адрес: {self.address}, Хэш пароля: {self.psw_hash}"

    # Выводит список всех пользователей.
    @staticmethod
    def list_users():
        print("Список пользователей:")
        for user in User.users: print(user)

    # Удаляет пользователя по имени пользователя.
    @staticmethod
    def delete_user(username):
        print("Удаление пользователя ", username)
        for user in User.users:
            if user.username == username:
                User.users.remove(user)
