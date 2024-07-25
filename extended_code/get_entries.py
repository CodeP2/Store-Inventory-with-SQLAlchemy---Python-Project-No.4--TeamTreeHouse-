import datetime
import Inventory_db


def get_entry_values_by(column_name):
    """
    returns entries from a database as a list while preventing list within a list
    """
    return [item[0] for item in Inventory_db.session.query(column_name)]


def Index_list():
    """
    gets attribute from database called 'product_id' and passing it and returning
    """
    return get_entry_values_by(getattr(Inventory_db.Product, "product_id"))


def product_name_list():
    product_names, column_names = collect_entries("product_name")
    stop_entries(product_names)
    return get_entry_values_by(column_names)


def collect_entries(column_name):
    """
    collect all entries form the databased that match the column name
    """
    empty_list = []
    column = getattr(Inventory_db.Product, column_name)
    for entry in Inventory_db.session.query(column):
        empty_list.append(entry)
    return empty_list, column


def stop_entries(entry, date=False, decimal=False):
    """
    recives the list and prints it in a nice format while stopping every 5 entries
    """
    counter = 0
    for item in entry:
        if date:
            print(datetime.datetime.strftime(item[0], '%B %d, %Y'))
        elif decimal:
            print(float(item[0]))
        else:
            print(item[0])
        counter += 1
        if counter == 5:
            input("press enter to continue...")
            counter = 0
