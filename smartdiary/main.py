import re, pickle, os
from smartdiary.address_book import *
from smartdiary.notes_book import *

from colorama import Fore, Style
from prettytable import PrettyTable
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

'''
розбиратиме введений користувачем рядок на команду та її аргументи. 
Команди та аргументи мають бути розпізнані незалежно від регістру введення.
'''
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

'''save and load notes'''
def save_notes(book, filename : str = "notesbook.pkl"):
    path_ext = os.path.expanduser("~")
    curr_path = os.path.join(path_ext, filename)

    with open(curr_path, "wb") as f:
        pickle.dump(book, f)


def load_notes(filename : str = "notesbook.pkl") -> NotesBook:
    path_ext = os.path.expanduser("~")
    curr_path = os.path.join(path_ext, filename)
    
    try:
        with open(curr_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NotesBook()  # Повернення нової адресної книги, якщо файл не знайдено


'''save and load address book'''
def save_data(book, filename : str = "addressbook.pkl"):
    path_ext = os.path.expanduser("~")
    curr_path = os.path.join(path_ext, filename)

    with open(curr_path, "wb") as f:
        pickle.dump(book, f)


def load_data(filename : str = "addressbook.pkl"):
    path_ext = os.path.expanduser("~")
    curr_path = os.path.join(path_ext, filename)
    
    try:
        with open(curr_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

'''decorator for address book'''
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            print(Fore.BLUE + f"Error {e}.")
            return #(f"Error {e}.")

        except IndexError as e:
            print(Fore.GREEN + f"Error {e}.")
            return# (f"Error {e}.")

        except ValueError as e:
            print(Fore.RED + f"Error {e}.")
            return #(f"Error {e}.")

    return inner


def email_input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if "email" in str(e).lower():
                print(Fore.RED + "Invalid email format. Please enter a valid email address.")
            else:
                raise e
    return inner


def address_input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if "address" in str(e).lower():
                print(Fore.RED + "Invalid address format. Please enter a valid address.")
            else:
                raise e
    return inner  


@input_error
def add_contact(args : list[str], book : AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Please enter 2 arguments: |name| |phone|")
    
    name, phone = args
    record = book.find(name)

    if isinstance(record, Record):
        record.add_phone(phone)
        return "Contact updated."
    else:
        new_record = Record(name)
        new_record.add_phone(phone)
        book.add_record(new_record)   
        return "Contact added."
    
@input_error
def delete_contact(args : list[str], book : AddressBook) -> str:
    if len(args) < 1:
        raise ValueError("Please enter argument: |name|")
    
    name = args[0]

    book.delete(name)
    return "Contact deleted."


@email_input_error
def add_email(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Please enter 2 arguments: |name| |email|")
    
    name, email = args
    record = book.find(name)

    if isinstance(record, Record):
        record.edit_email(email)
        return "Email added."
    else:
        return "Name not found."


@address_input_error
def add_address(args: list[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Please enter 2 arguments: |name| |address|")
    
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)

    if isinstance(record, Record):
        record.edit_address(address)
        return "Address added."
    else:
        return "Name not found."


@input_error
def add_phone(args : list[str], book : AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Please enter 2 arguments: |name| |phone| Note: phone should be 10 digits.")
    
    name, phone = args
    record = book.find(name)

    if isinstance(record, Record):
        record.add_phone(phone)
        return "Phone added."
    
    return "Name or phone is incorrect."    


@input_error
def add_birthday(args : list[str], book : AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Please enter 2 arguments: |name| |birthday| Note: birthday should be in format DD.MM.YYYY.")
    
    name, birthday = args
    record = book.find(name)

    if isinstance(record, Record):
        record.add_birthday(birthday)
        return "Birthday added."
    
    return "Name or date is incorrect."


@input_error
def change_contact(args : list[str], book : AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Please enter 2 arguments: |name| |phone| Note: phone should be 10 digits.")
    
    name, phone = args
    record = book.find(name)
    
    if isinstance(record, Record):
        # Change the first phone if available
        if record.phones:
            record.edit_phone(record.phones[0].value, phone)
        else:
            record.add_phone(phone)
        return "Contact updated"
    else:
        add_contact(args, book)
        raise KeyError("Contact was not existed")


@input_error    
def show_phone(args : list[str], book : AddressBook) -> Record:
    if len(args) < 1:
        raise IndexError("Please enter 1 argument: |name|")
    
    record = book.find(args[0])
    
    if isinstance(record, Record):
        return record#f"{record.name.value} phones:{'; '.join(p.value for p in record.phones)}"
    else:
        raise KeyError("Please give existing name")


@input_error    
def show_birthday(args : list[str], book : AddressBook) -> str:
    if len(args) < 1:
        raise IndexError("Please enter 1 argument: |name|")
    
    record = book.find(args[0])
    
    if isinstance(record, Record):
        birthday = datetime.strftime(record.birthday.birthday, "%d.%m.%Y") if record.birthday != None else "No info"
        return f"{record.name.value} birthday is {birthday}"
    else:
        raise KeyError("Please give existing name")


@input_error
def get_upcoming_birthdays(args : list[str], book : AddressBook) -> AddressBook:
    period = 7
    if len(args) >= 1:
        period = args[0]
    congrat_book = book.get_upcoming_birthdays(period)
    if congrat_book:
        return congrat_book
    else:
        return None


@input_error
def add_note(args, notes : NotesBook) -> str:
    if len(args) < 1:
        raise ValueError("Please enter argument: |note|")

    return notes.add_note(args[0])  

@input_error
def edit_note(args, notes) -> str:
    if len(args) < 1:
        raise ValueError("Please enter 2 arguments: |Note ID| |New content|")

    return  notes.edit_note_content(args[0], args[1]) 

@input_error
def delete_note(args, notes) -> str:
    if len(args) < 1:
        raise ValueError("Please provide |Note ID|")

    index = int(args[0])
    return notes.delete_note(index)  

@input_error
def search_notes(args, notes) -> NotesBook:
    if len(args) < 1:
        raise ValueError("Please enter argument: |Word(s)|")

    return notes.search_notes_by_content(args[0]) 


@input_error
def add_tag(args, notes) -> str:
    if len(args) < 1:
        raise ValueError("Please enter argument: |Note ID| |tag|")

    return notes.add_tag_to_note(args[0], args[1]) 

@input_error
def remove_tag(args, notes) -> str:
    if len(args) < 2:
        raise ValueError("Please enter argument: |Note ID| |tag|")
    return (notes.remove_tag_from_note(args[0], args[1]))


@input_error
def find_by_tag(args, notes) -> list:
    if len(args) < 1:
        raise ValueError("Please enter argument: |tag|")
    
    return (notes.search_notes_by_tag(args[0]))


def helper():
    #створюємо таблицю - довідник, що наш бот вміє виконувати наступні команди:
    table_help = PrettyTable()
    table_help.field_names = ["Command", "Description"]
    table_help.add_row(["hello", "Greeting"])
    table_help.add_row(["close", "Exit the program"])
    table_help.add_row(["help", "Show this help"])
    table_help.add_row(["exit", "Exit the program"])
    table_help.add_row(["add", "Add new contact"])
    table_help.add_row(["delete", "Delete contact"])
    table_help.add_row(["all", "Show all contacts"])
    table_help.add_row(["phone", "Show contact's phone number"])
    table_help.add_row(["change", "Change a contact's phone number"])
    table_help.add_row(["add-birthday", "Add a birthday to a contact"])
    table_help.add_row(["add_phone", "Add a phone to a contact"])
    table_help.add_row(["add_email", "Add an email to a contact"])
    table_help.add_row(["add_address", "Add an address to a contact"])
    table_help.add_row(["birthdays", "List of employees to congratulate"])
    table_help.add_row(["show-birthday", "Show a contact's birthday"])
    table_help.add_row(["add-note", "Add a note for a contact"])
    table_help.add_row(["edit-note", "Edit a note for a contact"])
    table_help.add_row(["delete-note", "Delete a note for a contact"])
    table_help.add_row(["search-notes", "Search notes by keyword"])
    table_help.add_row(["notes", "Show all notes"])
    table_help.add_row(["remove-tag", "Remove tag from note"])
    table_help.add_row(["find-by-tag", "Find notes by tag"])

    print(table_help)
    

def main() :
    # завантажимо або новый зробимо словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
    book = load_data()
    notes = load_notes()

    # ініціалізація списку команд-підказок
    command_completer = WordCompleter(['exit','close','add', 'delete','all','phone','change','add-birthday', 'add-phone', 'birthdays', 'show-birthday', 'add_email', 'add_address', 'add-note', 'edit-note', 'delete-note', 'notes', 'search-notes', 'find-by-tag', 'add-tag', 'remove-tag'])
    # вітаємо користувача
    print(Fore.BLUE + "Welcome to the assistant bot!")  

    #виводимо підказку, що наш бот вміє виконувати наступні команди:
    helper() 

  
    while True:
        print("\n")
        text = prompt("Enter a command: ", completer=command_completer)

        table = PrettyTable()
        table.field_names = ["Name", "Phone", "email", "Address","Birthday"]

        notes_table = PrettyTable()
        notes_table.field_names = ["Note ID", "Note", "Tags", "Creation Time"]

        
        command, *args = parse_input(text.strip().lower())

        if command in ["close", "exit"]:
            print("Good bye!")
            break
            
        elif command == "add_email":
            print(add_email(args, book))
            
        elif command == "add_address":
            print(add_address(args, book))

        #виводимо підказку, що наш бот вміє виконувати наступні команди:
        elif command == "hello":
            print("How can I help you?")

        elif command == "help":
            helper()

        #  За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. 
        elif command == "add":
            print(add_contact(args, book))

        elif command == "delete":
            print(delete_contact(args, book))
 
        #За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль
        elif command == "all":
            if book:
                for record in book.data:
                    birthday = datetime.strftime(book.data[record].birthday.birthday, "%d.%m.%Y") if book.data[record].birthday != None else "No info"
                    table.add_row([book.data[record].name.value, '; '.join(p.value for p in book.data[record].phones), book.data[record].email.value if book.data[record].email != None else "No info", book.data[record].address.value if book.data[record].address != None else "No info", birthday])
                print(table)
            else: 
                print("No contacts")

        # За цією командою бот виводить у консоль номер телефону для зазначеного контакту username
        elif command == "phone":
            record = show_phone(args, book)
            birthday = datetime.strftime(record.birthday.birthday, "%d.%m.%Y") if record.birthday != None else "No info"
            table.add_row([record.name.value, '; '.join(p.value for p in record.phones), record.email.value if record.email != None else "No info", record.address.value if record.address != None else "No info", birthday])
            print(table) 

        # За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику.
        elif command == "change":
            print(change_contact(args, book))

        elif command == "add-phone":
            print(add_phone(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))
        
        elif command == "birthdays":        
            congrat_list = get_upcoming_birthdays(args, book)
            if congrat_list != None:
                for record in congrat_list.data:
                    contact = congrat_list.data[record]
                    name = contact.name.value
                    phone = ';'.join(p.value for p in contact.phones)
                    email = contact.email.value if record.email != None else "No info"
                    address = contact.address.value if record.address != None else "No info"
                    birthday = datetime.strftime(contact.birthday.birthday, "%d.%m.%Y") if contact.birthday != None else "No info"
                    table.add_row([name, phone, email, address, birthday])
                print(table)
            else:
                print("Nobody to congrat")

        elif command == "add-note":
            print(add_note(args, notes))

        elif command == "add-tag":
            print(add_tag(args, notes))

        elif command == "remove-tag":
            print(remove_tag(args, notes))

        elif command == "find-by-tag":
            temp_notes = find_by_tag(args, notes)
            if len(temp_notes) > 0:
                for record in temp_notes:
                    creation_date = datetime.strftime(record.created_at, "%d.%m.%Y") if record != None else "No info"
                    notes_table.add_row([record.id, record.content if record != None else "No info", record.tags if record != None else "No info", creation_date])
                print(notes_table)  
            else:
                print("No such notes")          

        elif command == "edit-note":
            print(edit_note(args, notes))

        elif command == "delete-note":
            print(delete_note(args, notes))

        elif command == "search-notes":
            temp_notes = search_notes(args, notes)
            if len(temp_notes) > 0:         
                for record in temp_notes:
                    creation_date = datetime.strftime(record.created_at, "%d.%m.%Y") if record != None else "No info"
                    notes_table.add_row([record.id, record.content if record != None else "No info", record.tags if record != None else "No info", creation_date])
                print(notes_table)
            else:
                print("No notes")

        elif command == "notes":
            if isinstance(notes, NotesBook):
                for record in notes.data:
                    tags = ';'.join(p for p in notes.data[record].tags)
                    creation_date = datetime.strftime(notes.data[record].created_at, "%d.%m.%Y") if notes.data[record] != None else "No info"
                    notes_table.add_row([notes.data[record].id, notes.data[record].content if notes.data[record] != None else "No info", tags, creation_date])
                print(notes_table)
            else: 
                print("No contacts")


        else:
            print("Invalid command.")
    
    save_data(book)
    save_notes(notes)

if __name__ == "__main__":
    main()