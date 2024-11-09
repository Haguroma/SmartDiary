SmartDiary: Your Personal Command-Line Assistant
SmartDiary is a command-line application that helps you manage your contacts and keep track of their birthdays. It's built with Python and utilizes a simple, intuitive interface.

Features
Contact Management:
Add new contacts with names and phone numbers.
Store multiple phone numbers for a single contact.
Search for contacts by name.
Add email addresses to contacts.
Add addresses to contacts.
Edit existing contact information.
Delete contacts.

Notes Management:
Add new notes.
Store multiple tags for a single note.
Search for notes by keyword or tag.
Delete note.

Birthday Tracking:
Add birthdays to contacts.
Get reminders for upcoming birthdays within a specified period.
Handles weekend birthdays by shifting reminders to the following Monday.

Data Persistence:
Automatically saves and loads your contact data using pickle.

User-Friendly Interface:
Provides clear prompts and helpful error messages.
Offers command autocompletion for ease of use.
Installation

Clone the repository:
git clone https://github.com/Haguroma/SmartDiary.git
cd smartdiary

Create and activate a virtual environment (recommended):
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install the required packages:
pip install -r requirements.txt

Usage
Run the application:
python -m smartdiary


Follow the on-screen prompts and use the available commands:

| Command | Description | Example | 
|-------------------------------------------------------------|
| hello | Displays a greeting message. | hello | 
| add | Adds a new contact. | add John 1234567890 | 
| all | Lists all saved contacts. | all | 
| phone | Shows the phone number(s) of a contact. | phone John | 
| change | Updates the phone number of a contact. | change John 9876543210 | 
| add-phone | Adds an additional phone number to a contact. | add-phone John 5551234567 | 
| add-birthday | Adds a birthday to a contact. | add-birthday John 01.01.1990 | 
| show-birthday| Shows the birthday of a contact. | show-birthday John | 
| birthdays | Lists upcoming birthdays within a given period (default: 7 days). | birthdays or birthdays 14 | 
| add-email | Adds an email address to a contact. | add_email John john@gmail.com |
| add-address | Adds an address to a contact. | add_address John 123 Main St, City, Country |
| add-note | Adds a note to a contact. | add_note John work on this task |
| edit-note | Edit a note for a contact | edit-note 5 new_note |
| delete-note | Delete a note for a contact | delete-note 5 |
| search-notes | Search notes by keyword | search-notes word | 
| notes | Shows all notes for a contact. | notes | 
| close/exit | Exits the application. | close or exit |
| remove-tag | Removes a tag from a note | remove-tag tag |
| add-tag | Adds a tag to note | add-tag 1 tag |
| find-by-tag | Finds notes by tag | find-by-tag tag |

Contributing
Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request. [1]

License
This project is licensed under the MIT License.

Rate this answer: 
Sources
https://github.com/isreallee82/fundit