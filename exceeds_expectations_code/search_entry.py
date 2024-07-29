from error_messages import press_enter, integer_error_massage, menu_choice_error
from inventory_db import session, Product


keep_searching = True # global variable for search_by_id loop


def change_global_to_false():
    global keep_searching
    keep_searching = False

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
                confirm_keep_searching("Would you like to continue looking for more products?(Y/N)")
            else:
                print("Index not found!")
                press_enter()
        except ValueError:
            integer_error_massage(index_string)


def confirm_keep_searching(message):
    global keep_searching

    question = input(f"{message}\n>  ").lower()
    while keep_searching:
        if question in ["y", "n"]:
            break
        else:
            menu_choice_error("Y/N")
            question = input(f"{message}\n>  ").lower()
    if question == "y":
        print("Looking for the next product...")
        press_enter()
    else:
        print("Returning to main menu...")
        press_enter()
        change_global_to_false()
