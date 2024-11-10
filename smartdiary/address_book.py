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
    
   
    def edit_address(self, address: str):
        self.address = Address(address)
        return "Address added/updated."

   
    def edit_email(self, email: str) -> bool:
        try:
            self.email = Email(email)
            return True
        except ValueError as e:
            return str(e)
        
    def copy_record(self):
        result = Record(self.name)
        result.phones = self.phones
        result.birthday = Birthday(self.birthday.birthday.strftime("%d.%m.%Y"))
        result.address = Address(self.address.value) if self.address else None  # Адреса контакту
        result.email = Email(self.email.value) if self.email else None  # Адреса контакту 

        return result


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