from user import User

class Customer(User):

    def __init__(self, username, email, password, address):

        super().__init__(username, email, password)
        if self.username is None: return

        self.address = address

        print("Создан покупатель: ", self.get_details())

    def get_details(self):
        return f"Покупатель: {self.username}, Email: {self.email}, Адрес: {self.address}, Хэш пароля: {self.psw_hash}"
