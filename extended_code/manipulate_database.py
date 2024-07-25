import menus
import error_messages
from menus import edit_menu
from execute_yes_no import exceute_yes_no
from search_product import search_by_id
from execute_yes_no import exceute_yes_no
from Inventory_db import Product, session
from clear_data import get_date, get_decimal, get_integer


def add_product():
    new_product_name = input("Product name: ")
    new_product_quantity = get_integer()
    new_product_price = get_decimal()
    new_date_updated = get_date()
    new_product = Product(product_name=new_product_name, date_updated=new_date_updated,\
                            product_price=new_product_price, product_quantity=new_product_quantity)
    session.add(new_product)
    exceute_yes_no("Add this product?")


def edit_product():
    entry = search_by_id(False)
    while True:
        print(f"Currently you are trying to edit:\n{entry}")
        try:
            edit_menu()
            option_string = input(">  ").strip()
            option = int(option_string)
            if option == 1:
                new_name = input("Product Name: ")
                entry.product_name = new_name
            elif option == 2:
                clean_integer = get_integer()
                entry.product_quantity = clean_integer
            elif option == 3:
                clean_decimal = get_decimal()
                entry.product_price = clean_decimal
            elif option == 4:
                    clean_date = get_date
                    entry.date_updated = clean_date
            elif option == 5:
                exceute_yes_no("edit this entry?")
                break
            elif option == 6:
                break
            else:
                error_messages.menu_choice_error("1, 2, 3, 4")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4")



def delete_product():
    while True:
        entry = search_by_id(False)
        confirm_to_delete = input("Are you sure you want to delete the Product?(Y/N)\
                            \n(WARNING: This cannot be undone)\n\n>  ")
        if confirm_to_delete.lower() == "y":
            session.delete(entry)
            session.commit()
        elif confirm_to_delete.lower() not in ["y", "n"]:
            error_messages.menu_choice_error("Y/N")
        else:
            break


def menu():
    while True:
        menus.menu_a()
        try:
            option = int(input(">  "))
            if option == 1:
                add_product()
            elif option == 2:
                edit_product()
            elif option == 3:
                delete_product()
            elif option == 4:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5")
