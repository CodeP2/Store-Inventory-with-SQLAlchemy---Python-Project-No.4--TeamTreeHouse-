import menus
import error_messages
import csv


def back_up_database():
    pass


def menu():
    while True:
        menus.menu_b()
        try:
            option = input(">  ")
            if option == 1:
                back_up_database()
            elif option == 2:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5")
