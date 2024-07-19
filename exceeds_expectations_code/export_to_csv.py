import csv
from sqlalchemy import text
from inventory_db import engine


def query_a_table(table_name):
    """
    basic SQL query recives every entry from a database's name passed
    """
    query = f"""
            SELECT * FROM {table_name}
            """
    return query


def connect_to_database(query):
    """
    Connects with database and executes the query
    While fetchall() gets all of the rows as tuple from database
    And keys() all of the headers/column names
    """
    with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            columns = result.keys()
    return rows, columns


def export_to_csv(new_file_name, columns, rows):
    """
    recives new file name with required columns and rows to
    create a backup for database
    """
    with open(new_file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(columns)

        for row in rows:
            writer.writerow(row)


def back_up_to_csv():
    table_name = "Products"

    query = query_a_table(table_name) # gets everything from our table 

    rows, columns = connect_to_database(query) # passes every entry and recives them as columns and rows

    new_file_name = input("name your file.\n>  ")
    new_file = new_file_name + ".csv"
    export_to_csv(new_file, columns, rows)
