import menus
import error_messages


def add_product():
    pass


def edit_product():
    pass


def delete_product():
    pass


def menu():
    while True:
        menus.menu_a()
        try:
            option = input(">  ")
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5")
