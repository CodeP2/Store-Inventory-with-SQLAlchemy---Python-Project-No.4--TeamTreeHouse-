import datetime
from error_messages import data_convertion_error_message, menu_choice_error, press_enter
from inventory_db import session, Product
from get_input_or_confirm_changes import get_datetime, get_integer, confirm_menu


def add_or_update_product():

    current_time = datetime.datetime.now().date()

    product_name = input("What is the name of the product?\n>  ")
    product_quantity = get_integer("What is the quantity of the product?", "85")
    product_price = get_integer("What is the price of the product?", "12.99", True)
    date_updated = get_datetime("MM/DD/YYYY or 09/22/2015")

    new_product = Product(product_name=product_name, product_quantity=product_quantity, product_price=product_price, date_updated=date_updated)
    
    session.add(new_product)
    
    confirm_menu("Are you sure you want to add this product?(Y/N)") # makes sure a user wants to add a product to database
