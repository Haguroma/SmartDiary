import os, pickle
from smartdiary.notes_book import *
from smartdiary.address_book import *

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