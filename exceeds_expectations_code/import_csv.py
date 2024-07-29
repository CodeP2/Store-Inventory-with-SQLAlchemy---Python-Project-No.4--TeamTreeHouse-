import csv
import os
import datetime
import sys
import error_messages
from inventory_db import session, Product
from sqlalchemy.exc import IntegrityError


def import_csv_message():
    print("""*Important Information*
          
          \rWhen providing a folder name or file name, please follow those guidelines:

          \r1. To move to previous folder (aka level up) please use '../' notion, where:
          \r\t- if your current folder is 'Folder_one/Folder_two', using '../' will refer to 'Folder_one'.

          \r2. if the file is in the same folder as application, simply press enter when prompted for folder name.

          \rif you haven't moved files or folders, use the following:

          \r- When asked for folder name: ../store-inventory
          \r- When asked for file name: inventory.csv""")
    error_messages.press_enter()


def get_file(folder, file):
    """
    Takes folder path Ex. ../new_folder and file name Ex. file.csv
    takes the path to main file 
    and using sys.argv[1] and sys.argv[2] for the path
    while executing '../' to drop to previous folder
    path might be different depending on where the file is 
    but to save time I will provide path if the file is not moved
    folder: ../store-inventory  AND  file: inventory.csv
    """
    script_file = os.path.dirname(__file__)
    join_path = os.path.join(script_file, folder, file)
    return os.path.normpath(join_path)


def read_csv_file(path):
    """
    opens csv file and reads as dict it while 
    other functions converts data and inserts it to the database
    """
    with open(path, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile) # using DictReader instead of a next() to get "headers from a getgo"

        for row in reader:
            conver_data(row)
            insert_data(row)       


def conver_data(row):
    """
    takes all of the data as strings for specific dict keys to be converted to datetime and integers
    """
    row = get_int_price(row)
    row["product_quantity"] = int(row["product_quantity"])
    row["date_updated"] = datetime.datetime.strptime(row["date_updated"], "%m/%d/%Y").date()
    return row


def get_int_price(row):
    """
    converts specifically price to an Integer
    """
    row["product_price"] = row["product_price"].replace("$", "") #using .replace() to remove currency sign
    row["product_price"] = row["product_price"].split(".") 
    row["product_price"] = "".join(row["product_price"])
    row["product_price"] = int(row["product_price"])
    return row


def insert_data(row):
    """
    Inserts data and making sure not to add a duplicate to a database
    instead it overwrites changed entry in a database if thier update date is newer
    if the update date is old it skips the entry
    additionally checks if the price or quantity was changed in case update happend on the same day
    if theres any changes then it updates the quantity and/or price
    displays what entries are updated, added or skipped
    """
    try:
        existing_product = session.query(Product).filter_by(product_name=row["product_name"]).first()

        csv_date = row["date_updated"]
        csv_price = row["product_price"]
        csv_quantity = row["product_quantity"]

        if existing_product:
            
            price_changed = existing_product.product_price != csv_price
            quantity_changed = existing_product.product_quantity != csv_quantity
            
            if existing_product.date_updated < csv_date:
                existing_product.product_name = row["product_name"]
                existing_product.product_quantity = row["product_quantity"]
                existing_product.product_price = row["product_price"]
                existing_product.date_updated = row["date_updated"]
                session.commit()
                print(f"Product updated! {row['product_name']}")
            
            elif price_changed or quantity_changed:
                existing_product.product_quantity = csv_quantity
                existing_product.product_price = csv_price
                session.commit()
                print(f"Entry price/quantity Updated for {row['product_name']}")
            
            else:
                print(f"Entry skiped! {row['product_name']} is updated")
        
        else:
            product = Product(
               product_name=row["product_name"],
               product_quantity=row["product_quantity"],
               product_price=row["product_price"],
               date_updated=row["date_updated"]
            )
            session.add(product)
            print(f"Entry added! {row['product_name']}")
        session.commit()
    
    except IntegrityError:
        session.rollback()
        print(f"IntegrityError for: {row['product_name']}")           


if __name__ == "__main__":
    pass
