import error_messages
import search_or_add_entry
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
            search_or_add_entry.search_by_id()
        elif option == "a":
            search_or_add_entry.add_product()
        elif option == "b":
            export_to_csv.export_to_csv()
        elif option == "x":
            break
        else:
            error_messages.menu_choice_error("v, a, b, x")



if __name__ == "__main__":
    main_menu()
