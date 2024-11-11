from colorama import Fore

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