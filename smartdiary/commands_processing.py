from smartdiary.address_book import *
from smartdiary.notes_book import *
from smartdiary.decorators import *

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
        if (record.edit_email(email)) == True:
            return "Email added."
        else:
            return ('Invalid email format. Please enter a valid email address.') 
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

from datetime import datetime, timedelta

@input_error
def get_upcoming_birthdays(args : list[str], book : AddressBook) -> AddressBook:
    period = 7
    if len(args) >= 1:
        period = int(args[0])
    congrat_book = book.get_upcoming_birthdays(int(period))
 
    if congrat_book:
        return congrat_book
    else:
        return None


@input_error
def add_note(args, notes : NotesBook) -> str:
    if len(args) < 1:
        raise ValueError("Please enter argument: |note|")

    return notes.add_note(" ".join(args))  

@input_error
def edit_note(args, notes) -> str:
    if len(args) < 1:
        raise ValueError("Please enter 2 arguments: |Note ID| |New content|")

    return  notes.edit_note_content(args[0], " ".join(args[1:]) )

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