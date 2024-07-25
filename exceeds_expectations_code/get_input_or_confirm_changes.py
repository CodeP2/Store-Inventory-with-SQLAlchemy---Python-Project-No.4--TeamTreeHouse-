import datetime
from inventory_db import session
from error_messages import data_convertion_error_message, menu_choice_error, press_enter


def get_integer(message, error_message, is_price=False):
    while True:
        try:
            take_string = input(f"{message}\n>  ").strip()
            if is_price: # checks if I want to convert price if not it moves to the next part
                take_string = take_string.replace(".", "") # removes dot so it can be converted to int
            to_integer = int(take_string)
            if type(to_integer) is int:
                return to_integer
            else:
                print(f"Incorrect Format! Example: {error_message}")
        except ValueError as err:
            data_convertion_error_message(err, take_string, f"{error_message}")


def get_datetime(error_message):
    while True:
        try:
            take_string = input("What is the update date for the product? (Example: MM/DD/YYYY or 09/22/2015)\n>  ").strip()
            to_date = datetime.datetime.strptime(take_string, "%m/%d/%Y")
            return to_date
        except ValueError as err:
            data_convertion_error_message(err, take_string, error_message)


def confirm_menu(message, search_id=False):
    """
    This functions handles if the user is sure to add a new product to database
    Or if they want to keep searching for products
    """
    global keep_searching
    question = input(f"{message}\n>  ").lower()
    while True:
        if question in ["y", "n"]:
            break
        else:
            menu_choice_error("Y/N")
    if question == "y":
        session.commit()
        print("Product added!")
        press_enter()
    elif question == "y" and search_id:
        print("Looking for the next product...")
        press_enter()
    elif question == "n" and search_id:
        print("Returning to main menu...")
        press_enter()
        keep_searching = False
    else:
        print("Returning to main menu...")
        press_enter()
        pass
