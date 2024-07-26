import datetime
from inventory_db import session, Product
from error_messages import data_convertion_error_message, menu_choice_error, press_enter


def add_or_update_product():
    """
    adds an entry to a database unless the product is in the database it takes 
    first entry with matched product name and updates it if the date_updated
    is higher than existing entry's date
    """
    product_name = input("What is the name of the product?\n>  ")
    product_quantity = get_integer("What is the quantity of the product?", "85")
    product_price = get_integer("What is the price of the product?", "12.99", True)
    date_updated = get_datetime("MM/DD/YYYY or 09/22/2015")
    
    existing_product = session.query(Product).filter_by(product_name=product_name).first() # finds existing product by its name
    # if session query will find an entry
    # That exist in database it becomes "True"
    if existing_product:
        # informs user that existing entry was found
        print(f"Existing entry found:\n{existing_product.product_name} with {existing_product.date_updated} date\n")
        #if date_updated is higher than existing entry's it prepares entry to be updated
        if date_updated > existing_product.date_updated:
            existing_product.product_quantity = product_quantity
            existing_product.product_price = product_price
            existing_product.date_updated = date_updated
            print(f"Preparing to update Entry: {product_name}\n")
        else:
            print(f"for {product_name} is already up to date no changes was made\n")
    # if there's no existing product it will add a new one
    else:
        new_product = Product(product_name=product_name, product_quantity=product_quantity, product_price=product_price, date_updated=date_updated)
        session.add(new_product)
    
    confirm_menu("Are you sure you want to add this product?(Y/N)") # makes sure a user wants to add a product to database


def get_integer(message, error_message, is_price=False):
    """
    changes string into an integer based on If user is prompted to pass a price or quantity
    """
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
    """
    converts string into a datetime object with following Month/Day/Year as a date (removing hours etc.)
    """
    while True:
        try:
            take_string = input("What is the update date for the product? (Example: MM/DD/YYYY or 09/22/2015)\n>  ").strip()
            to_date = datetime.datetime.strptime(take_string, "%m/%d/%Y").date() # make sure that datetime will be datetime.date not datetime.datetime
            return to_date
        except ValueError as err:
            data_convertion_error_message(err, take_string, error_message)


def confirm_menu(message):
    """
    This functions handles if the user is sure to add a new product to database
    """
    question = input(f"{message}\n>  ").lower()
    while True:
        if question in ["y", "n"]:
            break
        else:
            menu_choice_error("Y/N")
    if question == "y":
        session.commit()
        print("Product added/updated!")
        press_enter()
    else:
        print("Returning to main menu...")
        session.rollback()
        press_enter()
        pass
