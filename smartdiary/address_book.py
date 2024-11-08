#Розробіть систему для управління адресною книгою.

from collections import UserDict
import re
from datetime import datetime, timedelta

class Birthday:
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних та перетворіть рядок на об'єкт datetime
            self.birthday = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        
# Клас для адреси контакту, успадковує Field
class Address(Field):
    def __init__(self, address):
        super().__init__(address)

# Клас для електронної пошти з валідацією формату
class Email(Field):
    def __init__(self, email):
        super().__init__(email)
        if not self.__validate():
            raise ValueError("Invalid email format.")

    def __validate(self) -> bool:
        # Валідація формату email
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.value))


""" валідацію номера телефону (має бути перевірка на 10 цифр) """
class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
        super().__init__(phone)
        if not self.__validate():
            raise ValueError("Invalid phone format. Expected 10 ")


    def __validate (self) -> bool:
         return bool(re.fullmatch(r'\d{10}', self.phone))

# class Запис:
#     """Клас для текстових заміток."""
#     def __init__(self, текст):
#         self.текст = текст

#     def __str__(self):
#         return self.текст

# class КеруванняЗаписами:
#     """Клас для керування замітками: додавання, редагування, видалення."""
#     def __init__(self):
#         self.записи = {}

#     def додати_запис(self, назва, текст):
#         self.записи[назва] = Запис(текст)
#         return f"Запис '{назва}' додано."

#     def редагувати_запис(self, назва, новий_текст):
#         if назва in self.записи:
#             self.записи[назва].текст = новий_текст
#             return f"Запис '{назва}' оновлено."
#         return f"Запис '{назва}' не знайдено."

#     def видалити_запис(self, назва):
#         if назва in self.записи:
#             del self.записи[назва]
#             return f"Запис '{назва}' видалено."
#         return f"Запис '{назва}' не знайдено."

#     def знайти_запис(self, назва):
#         return self.записи.get(назва, "Запис не знайдено.")

#     def показати_всі_записи(self):
#         return "\n".join(f"{назва}: {запис}" for назва, запис in self.записи.items())         
         

"""Реалізовано зберігання об'єкта Name в окремому атрибуті.
Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - 
edit_phone/пошуку об'єктів Phone - find_phone.
"""
# Клас для зберігання інформації про контакт
class Record:
    def __init__(self, name, address=None, email=None, birthday=None):
        self.name = Name(name)  # Ім'я контакту
        self.phones = []  # Список телефонних номерів
        self.address = Address(address) if address else None  # Адреса контакту
        self.email = Email(email) if email else None  # Електронна пошта
        self.birthday = Birthday(birthday) if birthday else None  # День народження

    def __str__(self):
        # Формування рядкового представлення контакту
        birthday = self.birthday.birthday.strftime("%d.%m.%Y") if self.birthday else "No info"
        address = self.address.value if self.address else "No info"
        email = self.email.value if self.email else "No info"
        phones = "; ".join(p.value for p in self.phones)
        return f"Name: {self.name.value}, Phones: {phones}, Address: {address}, Email: {email}, Birthday: {birthday}"


    def add_birthday(self, birthday : str):
        birth_date = Birthday(birthday)
        self.birthday = birth_date


    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return "Phone removed."
        return "Phone not found."


    def edit_phone(self, old_phone: str, new_phone: str):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return "Phone updated."
        return "Phone not found."
    
   
    def add_address(self, address: str):
        self.address = Address(address)
        return "Address added/updated."

   
    def add_email(self, email: str):
        try:
            self.email = Email(email)
            return "Email added/updated."
        except ValueError as e:
            return str(e)
    # def додати_запис(self, назва, текст):
    #     return self.записи.додати_запис(назва, текст)

    # def редагувати_запис(self, назва, новий_текст):
    #     return self.записи.редагувати_запис(назва, новий_текст)

    # def видалити_запис(self, назва):
    #     return self.записи.видалити_запис(назва)

    # def знайти_запис(self, назва):
    #     return self.записи.знайти_запис(назва)

    # def показати_всі_записи(self):
    #     return self.записи.показати_всі_записи()

# class AddressBook(UserDict):
#     def add_record(self, record):
#         self.data[record.name.значення] = record

#     def find(self, name):
#         return self.data.get(name, "Запис не знайдено.")

#     def delete(self, name):
#         if name in self.data:
#             del self.data[name]
#             return "Запис видалено."
#         return "Запис не знайдено."        


#     def find_phone(self, phone: str) -> str:
#         for p in self.phones:
#             if p.value == phone:
#                 return p.value
#         return "Phone not found."


#     def copy_record(self):
#         result = Record(self.name)

#         result.phones = self.phones
#         result.address = self.address
#         result.email = self.email
#         result.birthday = Birthday(self.birthday.birthday.strftime("%d.%m.%Y"))

#         return result


class AddressBook(UserDict):
    def add_record (self, record : Record):
        self.data[record.name.value] = record #,  додає запис до self.data.
    

    def find(self, name : str): #,  знаходить запис за ім'ям.
        return self.data.get(name, "Record not found.")


    def get_upcoming_birthdays(self, period : int = 7):
    
        today = datetime.today().date()

        users_to_congrat = AddressBook()

        try :
            for title in self.data:
                user = self.data[title]
                if user.birthday != None:
                    user_birthday = user.birthday.birthday
            
                    # Empoyee's birthday this year
                    user_birthday = user_birthday.replace(year=today.year)
            
                    # NewYear case
                    if (user_birthday < today) : 
                        user_birthday = user_birthday.replace(year=today.year + 1)

                    # How many days before birthday
                    days_before = (user_birthday - today).days
                    
                    # If current week
                    if (0<= days_before <= period) :
                        # If on weekends 
                        if (user_birthday.weekday() >=5) :
                            user_birthday += timedelta(days=(period -user_birthday.weekday()))

                        temp = user.copy_record()
                        temp.add_birthday(user_birthday.strftime("%d.%m.%Y"))
                        users_to_congrat.add_record(temp)
            return users_to_congrat
            
        except:
            print("Error")
            return self


    def delete(self, name : str): # видаляє запис за ім'ям.

        if name in self.data:
            del self.data[name]
            return "Record deleted."
        return "Record not found."