from user import User

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        pass

    def get_details(self):
        pass

    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """