import csv
import os
import datetime
import sys
from inventory_db import session, Product
from sqlalchemy.exc import IntegrityError


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
    takes all of the data as strings to be converted to datetime and integers
    """
    row = get_int_price(row)
    row["product_quantity"] = int(row["product_quantity"])
    row["date_updated"] = datetime.datetime.strptime(row["date_updated"], "%m/%d/%Y").date()
    return row


def get_int_price(row):
    """
    converts specifically price to Integer
    """
    row["product_price"] = row["product_price"].replace("$", "") #using .replace() to remove currency sign
    row["product_price"] = row["product_price"].split(".") 
    row["product_price"] = "".join(row["product_price"])
    row["product_price"] = int(row["product_price"])
    return row


def insert_data(row):
    """
    Inserts data and making sure not to add a duplicate
    existing_product takes my row's name and date to check if the product is all ready
    in the database if it not it adds automatically to database while printing out added entry
    if the entry is in the all ready in the database it skips the entry
    and checks for IntegrityError which checks if the entry is NULL, column that does not exist
    or if theres a duplicate with unique constrait 
    """
    try:
        existing_product = session.query(Product).filter_by(product_name=row["product_name"], date_updated=row["date_updated"]).first()

        if not existing_product:
            product = Product(
               product_name=row["product_name"],
               product_quantity=row["product_quantity"],
               product_price=row["product_price"],
               date_updated=row["date_updated"]
            )
            session.add(product)
            session.commit()
            print(f"Entry added! {row['product_name']}")
        else:
            print(f"Entry all ready exist! {row['product_name']}")
    except IntegrityError:
        session.rollback()
        print(f"IntegrityError for: {row['product_name']}")           


if __name__ == "__main__":
    folder = sys.argv[1]
    file = sys.argv[2]
    csv_file_path = get_file(folder, file)
    
    data_to_insert = read_csv_file(csv_file_path)
