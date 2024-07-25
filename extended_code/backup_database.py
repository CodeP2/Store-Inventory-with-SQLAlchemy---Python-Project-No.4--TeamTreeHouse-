import menus
from error_messages import menu_choice_error, file_not_found, table_not_found
from Inventory_db import engine
import pandas as pd
import sqlite3
import os


def connect_to_database():
    """
    Ask for user to provide the name of the file of database 
    then it checks if said file does not exist using os.path.isfile()
    if it does not it returns a custom error 
    if the file does exist passes get_name to sqlite3.connect to establish a connection with a database
    and returns it
    """
    while True:
        get_name = input("Provide your database file name\n(Example: Inventory.db)\n>  ").strip()
        if not os.path.isfile(get_name):
            file_not_found(get_name)
            continue
        else:
            conn = sqlite3.connect(get_name)
            return conn


def get_entries(conn):
    """
    Ask user for the name of the table that does exist in database file
    if the table exist inside of the database file
    it selects everything from the database table and returns it
    if the table does not exist it returns a custom error
    """
    while True:
        table_name = input("Provide Table name\n(Example: Products)\n>  ")
        if check_if_table_exist(conn, table_name):
            query = f"Select * From {table_name}"
            return query
        else:
            table_not_found(table_name)
            continue


def check_if_table_exist(conn, table_name):
    """
    checks if the table exist using query to select names of existing tables
    creating curosr so it will allow program to use query to look for all of the table names
    if the cursor finds the existing table using table_name it returns only that table's name
    otherwise it returns bool False if this provided table does not exist
    """
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
    cursor = conn.cursor()
    cursor.execute(query, (table_name,))
    return cursor.fetchone() is not None


def back_up_database_csv(query, conn, file_name):
    """
    reads provided query and connection to database with panda
    and then makes a backup exporting the file as csv
    """
    df = pd.read_sql_query(query, conn)
    df.to_csv(f"{file_name}_backup.csv", index=False)


def menu():
    while True:
        menus.menu_b()
        try:
            option = input(">  ").strip()
            option = int(option)
            if option == 1:
                connection = connect_to_database()
                query = get_entries(connection)
                file_name = input("provide your backup file name\n>  ")
                back_up_database_csv(query, connection, file_name)
            elif option == 2:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            menu_choice_error("1, 2")
