SmartDiary: Your Personal Command-Line Assistant
SmartDiary is a command-line application that helps you manage your contacts and keep track of their birthdays. It's built with Python and utilizes a simple, intuitive interface.

Features
Contact Management:
Add new contacts with names and phone numbers.
Store multiple phone numbers for a single contact.
Edit existing contact information.
Delete contacts.

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
git clone https://github.com/your-username/smartdiary.git
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

| Command | Description | Example | |-----------------|-----------------------------------------------------------|---------------------------------------| | hello | Displays a greeting message. | hello | 
| add | Adds a new contact. | add John 1234567890 | 
| all | Lists all saved contacts. | all | 
| phone | Shows the phone number(s) of a contact. | phone John | 
| change | Updates the phone number of a contact. | change John 9876543210 | 
| add-phone | Adds an additional phone number to a contact. | add-phone John 5551234567 | 
| add-birthday | Adds a birthday to a contact. | add-birthday John 01.01.1990 | 
| show-birthday| Shows the birthday of a contact. | show-birthday John | 
| birthdays | Lists upcoming birthdays within a given period (default: 7 days). | birthdays or birthdays 14 | 
| close/exit | Exits the application. | close or exit |

Contributing
Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request. [1]

License
This project is licensed under the MIT License.

Rate this answer: 
Sources
https://github.com/isreallee82/fundit