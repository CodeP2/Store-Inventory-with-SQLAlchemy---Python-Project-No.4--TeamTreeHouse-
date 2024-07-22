import menus
import error_messages
import Inventory_db
import get_entries
from sqlalchemy import and_
from get_vaild_input import get_input_index, get_input_name, get_input_date, get_input_price, get_input_quantity


def query_by(entry_type, column_name):
    column = getattr(Inventory_db.Product, column_name)
    for entry in Inventory_db.session.query(Inventory_db.Product).filter(column==entry_type):
        print(entry)


def query_in_range(entry_type_1, entry_type_2, column_name):
    column = getattr(Inventory_db.Product, column_name)
    for entry in Inventory_db.session.query(Inventory_db.Product).filter(column.between(entry_type_1, entry_type_2)).all():
        print(entry)


def search_by_id():
    index_list = get_entries.Index_list()
    index_number = get_input_index(index_list)
    query_by(index_number, "product_id")


def search_by_name():
    product_name = get_input_name()
    query_by(product_name, "product_name")


def search_by_date():
    date_updated_1, date_updated_1 = get_input_date()
    query_in_range(date_updated_1, date_updated_1, "date_updated")


def search_by_quantity():
    product_quantity_1, product_quantity_1 = get_input_quantity
    query_in_range(product_quantity_1, product_quantity_1, "date_updated")


def search_by_price():
    product_price_1, product_price_2 = get_input_price()
    query_in_range(product_price_1, product_price_2, "product_price")


def menu():
    while True:
        menus.menu_v()
        try:
            option = int(input(">  "))
            if option == 1:
                search_by_id()
            elif option == 2:
                search_by_name()
            elif option == 3:
                search_by_date()
            elif option == 4:
                search_by_quantity()
            elif option == 5:
                search_by_price()
            elif option == 6:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5, 6")
