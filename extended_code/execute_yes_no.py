import Inventory_db
import import_csv
import error_messages


def exceute_yes_no(csv=False, cursor=None):
    question = input(f"Are you sure you want to add/edit this product?(Y/N):\n").strip().lower()
    while question not in ["y", "n"]:
        error_messages.menu_choice_error("Y/N")
        question = input(f"Are you sure you want to add/edit this product?(Y/N):\n").strip().lower()
    if question == "y":
        if csv:
            cursor.connection.commit()
            print("Product added!")
        else:
            Inventory_db.session.commit()
            print("Product added!")
    else:
        pass
