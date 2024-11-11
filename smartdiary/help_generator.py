from prettytable import PrettyTable


def help_menu_generation():
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
    table_help.add_row(["add-tag", "Add a tag to a note"])
    table_help.add_row(["edit-note", "Edit a note for a contact"])
    table_help.add_row(["remove-tag", "Remove tag from note"])
    table_help.add_row(["find-by-tag", "Find notes by tag"])

    return table_help