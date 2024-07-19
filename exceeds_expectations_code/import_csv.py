import csv
import os
import datetime
import sys
import sqlite3

"""
getting the path to a csv file
with sys.argv[x] to get folder, file name
joining paths with ../folder and file name
while resolving any ../ with normpath
"""
def get_file(folder, file):
    script_file = os.path.dirname(__file__)
    join_path = os.path.join(script_file, folder, file)
    return os.path.normpath(join_path)


def read_csv_file(path):
    with open(path, "r", newline="") as csvfile:
        lines = []
        reader = csv.DictReader(csvfile) # using DictReader instead of a next() to get "headers from a getgo"

        for row in reader:
            conver_data(row)
            lines.append(row)
        
    return lines


"""
converting data passed from read_csv_file() function
"""
def conver_data(row):
    
    row["product_quantity"] = int(row["product_quantity"])
    row["date_updated"] = datetime.datetime.strptime(row["date_updated"], "%m/%d/%Y").date()
    return row


"""
Connecting to database using sqlite3
"""
def connect_to_database(data_base_name):
        connection = sqlite3.connect(data_base_name) #connects to a database here it connects localy
        return connection.cursor() # creates a "cursor" for me so I can execute SQL commands


def insert_data_to_database(data_to_phrase, cursor, sql_database):
    for row in data_to_phrase:
        values = (row["product_name"], row["product_quantity"], row["product_price"], row["date_updated"])
        cursor.execute("SELECT COUNT(*) FROM Products WHERE product_name = ?", (row["product_name"],))
        


if __name__ == "__main__":
    folder = sys.argv[1]
    file = sys.argv[2]
    csv_file_path = get_file(folder, file)
    data_to_insert = read_csv_file(csv_file_path)
    data_base_cursor = connect_to_database("Inventory.db")
    sql = "INSERT INTO Products (product_name, product_quantity, product_price, product_updated) VALUES (?, ?, ?, ?)"
    insert_data_to_database(data_to_insert, data_base_cursor, sql)
    data_base_cursor.close()
    
