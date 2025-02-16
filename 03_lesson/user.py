class User: # Объявление класса с именем User

    def __init__(self, first_name, last_name): # Определение конструтора класса
        self.lastUser = last_name # Сохранение фамилии в параметре объекта
        self.firstUser = first_name # Сохранение имени в параметре объекта

    def get_last_name(self): # Определение метода для получения фамилии
        print(self.lastUser) # Печать фамилии

    def get_first_name(self): # Определение метода для получения имени
        print(self.firstUser) # Печать имени

    def get_full_name(self): # Определение метода для получения полного имени
        print(f"{self.firstUser} {self.lastUser}") # Формирование строки с ИО и печать ее




