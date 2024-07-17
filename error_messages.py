def menu_choice_error(options):
    print(f"""\r#########Error###########
          \rIncorrect Choice!
          \rcorrect choices are: {options}
          \r##########################
           """)
    press_enter()


def press_enter():
    input("Press enter to continue...")
