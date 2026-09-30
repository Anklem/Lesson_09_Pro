from AuthenticationService import AuthenticationService

# Реализуйте регистрацию пользователей с проверкой уникальности имени пользователя и хешированием паролей.
auth_service = AuthenticationService()
customer1 = auth_service.register("Иванов", "ivanov@mail.ru", "ivanov", "Kostroma", False)
customer2 = auth_service.register("Петров", "petrov@mail.ru", "petrov", "Ryazan", False)
customer3 = auth_service.register("Сидоров", "sidorov@mail.ru", "sidorov", "Moscow", False)
customer4 = auth_service.register("Американский шпион", "ivanov@mail.ru", "ivanov", "Kostroma", False)
customer5 = auth_service.register("Британский шпион", "ivanov@mail.ru", "ivanov", "Kostroma", False)
customer6 = auth_service.register("ИваНоВ", "ivanov@mail.ru", "ivanov", "Kostroma", False)

print()
admin1 = auth_service.register("Админов", "admin@mail.ru", "adminov", "Siberia", True)
admin2 = auth_service.register("Системов", "sys@mail.ru", "sys", "Ryazan", True)
admin3 = auth_service.register("Американский шпион", "ivanov@mail.ru", "sys", "NY", True)
admin4 = auth_service.register("АДМИНОВ", "adm@mail.ru", "adm", "London", True)

# Реализуйте аутентификацию пользователей с проверкой пароля.
print()
auth_service.login("Американский шпион", "12345")
auth_service.login("Иванов", "12345")
auth_service.login("Иванов", "ivanov")

# Реализуйте управление сессиями, чтобы отслеживать текущего вошедшего пользователя.
print()
print("Текущий пользователь:", auth_service.get_current_user())
auth_service.login("Петров", "petrov")
print("Текущий пользователь:", auth_service.get_current_user())
auth_service.logout()
print("Текущий пользователь:", auth_service.get_current_user())

# Реализуйте функции для управления пользователями (просмотр списка пользователей, удаление пользователей) только для админа.
print()
admin1.list_users()

print()
admin2.delete_user("Петров")
admin2.delete_user("Неизвестный")

print()
admin1.list_users()
