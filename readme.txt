main.py

Here's the explanation in plain text format:

Let me break down this code which appears to be a contact management system (Address Book). 
Here's a clear explanation of its main components and functionality:

Imports and Decorator:

Uses re and pickle modules
Includes a custom input_error decorator that handles common errors (KeyError, IndexError, ValueError)
The decorator wraps functions to provide error handling without modifying the original functions

Data Persistence Functions:
Uses pickle for saving and loading the address book data
save_data: Writes the address book to a file in binary format
load_data: Reads from a file or creates new AddressBook if file doesn't exist
Default filename is "addressbook.pkl"

Command Processing:
parse_input function splits user input into command and arguments
Converts command to lowercase and strips whitespace
Returns command and remaining arguments separately

Core Functions:
add_contact: Creates new or updates existing contacts
add_phone: Adds another phone number to existing contact
add_birthday: Sets birthday for a contact
change_contact: Updates phone number for existing contact
show_phone: Displays contact's phone numbers
show_birthday: Shows contact's birthday
get_upcoming_birthdays: Lists approaching birthdays

Main Function:
Loads existing address book data at startup
Runs continuous loop for command input
Processes various commands
Saves data when exiting

Available Commands:
hello - Shows welcome message
add name phone - Creates new contact
all - Lists all contacts
phone name - Shows specific contact's phone
change name new_phone - Updates phone number
add-phone name phone - Adds additional phone
add-birthday name DD.MM.YYYY - Sets contact birthday
show-birthday name - Displays contact birthday
birthdays - Shows upcoming birthdays
close/exit - Ends program

Example Usage:
First command: add John 1234567890
Second command: add-birthday John 01.01.1990
Third command: show-birthday John
Fourth command: phone John
Fifth command: all

The program includes comprehensive error handling and automatically saves changes to a file. 
When started again, it loads the saved data, maintaining persistence between sessions.

___________________________________________________________________________
address_book.py

ADDRESS BOOK CODE EXPLANATION
BASE CLASSES

Field - Basic building block:
Stores a single value
Provides string representation

Name and Phone - Specialized fields:
Name is simple extension of Field
Phone adds validation to ensure 10-digit format
Phone validates using regular expression pattern

BIRTHDAY HANDLING
Birthday class features:
Converts string dates to datetime objects
Expects format "DD.MM.YYYY"
Validates date format

RECORD CLASS
Main contact entry features:
Stores name, multiple phones, and optional birthday Methods for managing phones:
add_phone()
remove_phone()
edit_phone()
find_phone()
Birthday management with add_birthday()

ADDRESS BOOK CLASS
Main container features:
Inherits from UserDict for dictionary-like behavior

Stores Records by name Methods:
Adding records
Finding records by name
Deleting records
Getting upcoming birthdays

EXAMPLE USAGE:
Create address book
book = AddressBook()

Add new contact
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_birthday("15.05.1990")
book.add_record(john_record)

Find contact
john = book.find("John")

Get upcoming birthdays
upcoming = book.get_upcoming_birthdays()

KEY FEATURES:
Phone validation (10 digits)
Date validation (DD.MM.YYYY)
Multiple phone numbers per contact
Birthday tracking and notifications
Weekend birthday handling (moves to Monday)
Contact management (add/remove/edit)

ERROR HANDLING:
Phone format validation
Date format validation
Record existence checks
Copy functionality for records

Note: You can copy this text directly and save it to a .txt file using any text editor while maintaining 
the formatting