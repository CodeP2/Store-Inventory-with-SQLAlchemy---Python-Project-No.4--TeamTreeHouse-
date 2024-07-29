def data_convertion_error_message(err, user_input, example):
    """
    custom error message for input convertion
    """
    print(f"""\r#########Error###########
          \r#Incorrect format -> {err}
          \r#Your's Input: >{user_input}<
          \r#Example: {example}
          \r##########################
          """)
    press_enter()


def integer_error_massage(user_input):
    """
    custom error message for integers
    """
    print(f"""\r#########Error###########
          \r#The input is not a number!
          \r#Your input: {user_input}
          \r#Example of a correct input: 1
          \r##########################
          """)
    press_enter()


def menu_choice_error(options):
    """
    custom error message for menu choice
    """
    print(f"""\r#########Error###########
          \rIncorrect Choice!
          \rcorrect choices are: {options}
          \r##########################
           """)
    press_enter()


def file_not_found_error_message(folder, file, err):
    print(f""""\r#########Error###########
          \rProvided folder or file is incorrect/does not exist
          \rfolder input: >{folder}<
          \rfile input: >{file}<
          \rError message: {err}
          \rPlease try again and follow guidelines!
          \r##########################""")
    press_enter()
    

def press_enter():
    """
    stop program so user can read an error message
    """
    input("Press enter to continue...")
