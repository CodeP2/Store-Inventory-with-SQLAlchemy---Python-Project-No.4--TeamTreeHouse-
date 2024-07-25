import menus
import error_messages
import Inventory_db
import get_entries
from error_messages import menu_choice_error, press_enter
from get_vaild_input import get_input_index, get_input_name, get_input_date, get_input_price, get_input_quantity


def query_by(entry_type, column_name, is_editing=False):
    column = getattr(Inventory_db.Product, column_name)
    find_entry = Inventory_db.session.query(Inventory_db.Product).filter(column==entry_type)
    if is_editing:
        for entry in find_entry:
            return entry
    else:
        for entry in find_entry:
            print(entry)
            press_enter()
            


def query_in_range(entry_type_1, entry_type_2, column_name):
    loop_num = 0
    column = getattr(Inventory_db.Product, column_name)
    find_entries = Inventory_db.session.query(Inventory_db.Product).filter(column.between(entry_type_1, entry_type_2)).all()
    if not find_entries:
        print("No entries was found!")
        press_enter()
    for entry in find_entries:
        loop_num += 1
        print(entry)
        if loop_num == 5:
            press_enter()
            loop_num = 0


def search_by_id(read_entry=True):
    index_list = get_entries.Index_list()
    index_number = get_input_index(index_list)
    if read_entry:
        query_by(index_number, "product_id")
    else:
        return query_by(index_number, "product_id", True)


def search_by_name():
    product_name = get_input_name()
    query_by(product_name, "product_name")


def search_by_date():
    date_updated_1, date_updated_2 = get_input_date()
    query_in_range(date_updated_1, date_updated_2, "date_updated")


def search_by_quantity():
    product_quantity_1, product_quantity_2 = get_input_quantity()
    query_in_range(product_quantity_1, product_quantity_2, "product_quantity")


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
            menu_choice_error("1, 2, 3, 4, 5, 6")
