import csv
import os
import datetime
import sys
import pandas as pd
import Inventory_db
import execute_yes_no


def get_file(folder, file):
    """
    it takes the path to a csv file
    with sys.argv[x] where argumets are:
    folder name is folder and file is file name
    and the code supports ../ as it does remove "stacking" with normpath
    when running the script
    """
    script_file = os.path.dirname(__file__)
    join_path = os.path.join(script_file, folder, file)
    return os.path.normpath(join_path)


def read_csv_file(path):
    """
    This code takes path to a file and opens the file
    creates an empty 
    reading it as a dictionary using csv.DictReader()
    then it takes each row and passes the row to convert dirty data
    and appends to empty list called lines and returns it
    """
    with open(path, "r", newline="") as csvfile:
        lines = []
        reader = csv.DictReader(csvfile) # using DictReader instead of a next() to get "headers from a getgo"

        for row in reader:
            conver_data(row)
            lines.append(row)
        
    return lines


def conver_data(row):
    """
    The function recives dictionary as a single "row"
    if a list of dict is passed it has to be passed one element of the list
    then it converts specific data with a key being a column name
    """
    row["product_price"] = float(row["product_price"].replace("$", "")) #using .replace() to remove currency sign
    row["product_quantity"] = int(row["product_quantity"])
    row["date_updated"] = datetime.datetime.strptime(row["date_updated"], "%m/%d/%Y").date()
    return row


def check_for_duplicates(df, table_name, columns, engine):
    """
    checks for duplicates in the proveded Dataframe in existing SQL table
    I reads the sql table with provided engine and table's name
    then it does check if those entries exist in the table
    if there's duplicates they are stored as NaN
    """
    existing_data = pd.read_sql_table(f"{table_name}", engine)
    df_unique = df[~df[columns].isin(existing_data[columns])]
    return df_unique


def import_as_database(df, table_name, columns, engine):
    """
    This code imports dict to a database unsuring no duplicates will be passed
    removes rows with NaN values with specified colums
    passes and checks for duplicates in check_for_duplicates function
    removes remaining NaN values
    If theres no unique rows to insert user will recive a prompt otherwise it appends rows
    """
    df = df.dropna(subset=columns)
    df_unique = check_for_duplicates(df, table_name, columns, engine)
    df_unique = df_unique.dropna(subset=columns)
    if df_unique.empty:
        input("the entries all ready exist!\npress enter to continue...")
    else:
        execute_yes_no.exceute_yes_no("to add this file to database?", True, df_unique, table_name, engine)    


def to_data_frame(csv_dict):
    return pd.DataFrame(csv_dict)


if __name__ == "__main__":
    folder = sys.argv[1]
    file = sys.argv[2]
    csv_file_path = get_file(folder, file)
    
    data_to_insert = read_csv_file(csv_file_path)

    import_as_database(to_data_frame(data_to_insert), "Products", ["product_name", "product_price", "product_quantity","date_updated"], Inventory_db.engine)  
