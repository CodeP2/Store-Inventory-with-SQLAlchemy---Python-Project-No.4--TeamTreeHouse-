import menus
import error_messages
import Inventory_db

def get_entry_values_by(column_name):
    return [item[0] for item in Inventory_db.session.query(column_name)]


def Index_list():
    return get_entry_values_by(getattr(Inventory_db.Product, "id"))


def search_by_id():
    index_list = entries_by_x.Index_list()
    index_number = get_valid_imput("What is the book's id?", index_list, "Index not found!", True, index_list)
    query_by(index_number, "id")


def search_by_date():
    pass


def search_by_name():
    pass


def menu():
    while True:
        menus.menu_v()
        try:
            option = input(">  ")
            if option == 1:
                search_by_id()
            elif option == 2:
                search_by_date
            elif option == 3:
                search_by_name
            elif option == 4:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5")
