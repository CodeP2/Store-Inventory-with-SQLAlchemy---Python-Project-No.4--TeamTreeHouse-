import datetime
from error_messages import data_convertion_error_message, menu_choice_error, press_enter, integer_error_massage
from inventory_db import session, Product


keep_searching = True # global variable for search_by_id loop


def add_product():
    product_name = input("What is the name of the product?\n>  ")
    product_quantity = get_integer("What is the quantity of the product?", "85")
    product_price = get_integer("What is the price of the product?", "12.99", True)
    date_updated = get_datetime("MM/DD/YYYY or 09/22/2015")
    new_product = Product(product_name=product_name, product_quantity=product_quantity, product_price=product_price, date_updated=date_updated)
    session.add(new_product)
    accept_or_reject_menu("Are you sure you want to add this product?(Y/N)") # makes sure a user wants to add a product to database


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


def get_entry_values_by(column_name):
    """
    This function is more of future proofing if I would like to update this code
    to search for different types of columns and return only this specific column like names only
    """
    return [item[0] for item in session.query(column_name)]


def id_list():
    """
    its not required code if working with only one database
    but I can modify it it use it on different databases to get
    thier id's
    """
    return get_entry_values_by(getattr(Product, "product_id"))


def query_by(entry_type ,column_name):
    """
    In case of expanding this code I made query by function
    where getattr dynamically access in this case 'product_id' 
    attribute of the Product Object
    and getting access to entry for example id = 3 with entry type
    """
    column = getattr(Product, column_name)
    for entry in session.query(Product).filter(column==entry_type):
        print(entry)


def search_by_id():
    """
    global variable keep_searching ensures the flow of the 
    while "True" loop for the user to have an option 
    If they want to continue looking for the new product 
    Or go back to main menu
    """
    global keep_searching
    while keep_searching:
        try:
            index_list = id_list()
            print(f"Options: {index_list}")
            index_string = input("What is the book's id?\n>  ").strip()
            index_number = int(index_string)
            if index_number in index_list:
                query_by(index_number, "product_id")
                press_enter()
                accept_or_reject_menu("Would you like to continue looking for more products?(Y/N)", True)
            else:
                print("Index not found!")
                press_enter()
        except ValueError:
            integer_error_massage(index_string)


def accept_or_reject_menu(message, search_id=False):
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
