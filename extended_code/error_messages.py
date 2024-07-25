def data_convertion_error_message(err, user_input, example):
    print(f"""\r#########Error###########
          \r#Incorrect format -> {err}
          \r#Your's Input: >{user_input}<
          \r#Example: {example}
          \r##########################
          """)
    press_enter()


def integer_error_massage(user_input):
    print(f"""\r#########Error###########
          \r#The input is not a number!
          \r#Your input: {user_input}
          \r#Example of a correct input: 1
          \r##########################
          """)
    press_enter()


def menu_choice_error(options):
    print(f"""\r#########Error###########
          \rIncorrect Choice!
          \rcorrect choices are: {options}
          \r##########################
           """)
    press_enter()


def file_not_found(user_input):
    print(f"""Error: file not found!
          \ryour input: >{user_input}<""")
    press_enter()


def table_not_found(user_input):
    print(f"""Error: Table name not found!
          \ryour input: >{user_input}<""")
    press_enter()


def press_enter():
    input("Press enter to continue...")
