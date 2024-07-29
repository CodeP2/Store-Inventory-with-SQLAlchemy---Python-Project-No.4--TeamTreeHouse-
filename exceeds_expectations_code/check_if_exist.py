import import_csv
import error_messages
from inventory_db import engine, start_engine
import os

def check_menu_message():
    print("""Welcome to 'store inventory with sqlalchemy' Program!
          \rchecking for existing database...
          """)
    error_messages.press_enter()
    

def import_my_file():
    """
    if the database exist the program inserts csv file to database using scripts from
    'import.csv.py' file while asking for folder or file names to get a path to a file.
    """
    while True:
        try:
            import_csv.import_csv_message()
            folder = input("Please provide folder name of csv file (Example: ../store-inventory)\n>  ")
            file = input("Please provide name of the csv file (Example: inventory.csv)\n>  ")
            file_path = import_csv.get_file(folder, file)
            import_csv.read_csv_file(file_path)
            break
        except FileNotFoundError as err:
            error_messages.file_not_found_error_message(folder, file, err)


def check_if_database_file_exist():
    """
    checks if database exist using os.path.exist
    database does not exist.
    """
    script = os.path.dirname(__file__)
    database_file = os.path.join(script, "Inventory.db")
    if os.path.exists(database_file):
        return True
    else:
        return False


def check_database_exists():
    check_menu_message()
    connection_check = check_if_database_file_exist()
    if connection_check:
        print("\nOur database exist!\n")
    else:
        print("\nOur database does not exist... creating a database.\n")
        start_engine()
    error_messages.press_enter()
    while True:
        question = input("\nWould you like to import a csv file to database?(Y/N)\n>  ").strip().lower()
        if question == "y":
            import_my_file()
        elif question == "n":
            break
        else:
            error_messages.menu_choice_error("Y/N")
    
