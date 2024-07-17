import error_messages


def main_menu_message():
    pass


def main_menu():
    while True:
        main_menu_message()
        option = input(">  ").lower().strip()
        if option == "v":
            pass
        elif option == "a":
            pass
        elif option == "b":
            pass
        elif option == "x":
            break
        else:
            error_messages.menu_choice_error("v, a, b, x")



if __name__ == "__main__":
    main_menu()
