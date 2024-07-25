import Inventory_db
import error_messages


def exceute_yes_no(text_variation, csv=False, *args):
    """
    Controls if the user wants to commit changes while checking
    for csv file passed in if there is it uses .to_sql method to
    transfer those files to a database
    """
    question = input(f"Are you sure you want to {text_variation}?(Y/N):\n").strip().lower()
    while question not in ["y", "n"]:
        error_messages.menu_choice_error("Y/N")
        question = input(f"Are you sure you want to {text_variation}?(Y/N):\n").strip().lower()
    if question == "y":
        if csv:
            df_unique, table_name, engine = args
            df_unique.to_sql(table_name, engine, if_exists="append", index=False)
        else:
            Inventory_db.session.commit()
            print("Product added!")
    else:
        pass
