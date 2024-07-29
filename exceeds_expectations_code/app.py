import error_messages
import search_entry as se
import add_or_update_entry as aoue
import check_if_exist
import export_to_csv


def main_menu_message():
    print("""Welcome to Inventory Program
          \rv) Search product by id
          \ra) Add a new product
          \rb) backup your database entries
          \rx) Exit Program
          """)


def main_menu():
    while True:
        main_menu_message()
        option = input(">  ").lower().strip()
        if option == "v":
            se.search_by_id()
        elif option == "a":
            aoue.add_or_update_product()
        elif option == "b":
            export_to_csv.back_up_to_csv()
        elif option == "x":
            break
        else:
            error_messages.menu_choice_error("v, a, b, x")



if __name__ == "__main__":

    check_if_exist.check_database_exists()

    main_menu()
