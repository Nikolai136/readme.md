from user import User

# Создание экземпляров класса User
user = User('Иван', 'Иванов') # Передаем имена при создании объекта

# Вызов методов
user.get_first_name() # Вызов метода для печати имени
user.get_last_name() # Вызов метода для печати фамилии
user.get_full_name() # Вызов метода для печати полного имени

my_user = User ("Анна", "Петрова")

my_user.get_first_name() # Вызов метода для печати имени
my_user.get_last_name() # Вызов метода для печати фамилии
my_user.get_full_name() # Вызов метода для печати полного имени