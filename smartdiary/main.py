from smartdiary.address_book import *
from smartdiary.notes_book import *
from smartdiary.commands_processing import *
from smartdiary.help_generator import *
from smartdiary.load_save_data import *
from colorama import Fore
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


def helper():
    #створюємо таблицю - довідник, що наш бот вміє виконувати наступні команди:
    print(help_menu_generation())
    

def main() :

    # для переносу нотатку на слідуючий рядок, якщо його довжина більша за  note_line_width
    note_line_width = 50

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
                    email = contact.email.value if contact.email != None else "No info"
                    address = contact.address.value if contact.address != None else "No info"
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
                    tags = ';'.join(p for p in record.tags)
                    content = "\n".join(record.content[i:i+note_line_width] for i in range(0, len(record.content), note_line_width)) #notes.data[record].content if notes.data[record] != None else "No info"
                    creation_date = datetime.strftime(record.created_at, "%d.%m.%Y") if record != None else "No info"
                    notes_table.add_row([record.id, content, tags, creation_date])
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
                    tags = ';'.join(p for p in record.tags)
                    content = "\n".join(record.content[i:i+note_line_width] for i in range(0, len(record.content), note_line_width)) #notes.data[record].content if notes.data[record] != None else "No info"
                    creation_date = datetime.strftime(record.created_at, "%d.%m.%Y") if record != None else "No info"
                    notes_table.add_row([record.id, content, tags, creation_date])
                print(notes_table)
            else:
                print("No notes")

        elif command == "notes":
            if isinstance(notes, NotesBook):
                for record in notes.data:
                    tags = ';'.join(p for p in notes.data[record].tags)
                    content = "\n".join(notes.data[record].content[i:i+note_line_width] for i in range(0, len(notes.data[record].content), note_line_width)) #notes.data[record].content if notes.data[record] != None else "No info"
                    creation_date = datetime.strftime(notes.data[record].created_at, "%d.%m.%Y") if notes.data[record] != None else "No info"
                    notes_table.add_row([notes.data[record].id, content, tags, creation_date])
                print(notes_table)
            else: 
                print("No contacts")


        else:
            print("Invalid command.")
    
    save_data(book)
    save_notes(notes)

if __name__ == "__main__":
    main()