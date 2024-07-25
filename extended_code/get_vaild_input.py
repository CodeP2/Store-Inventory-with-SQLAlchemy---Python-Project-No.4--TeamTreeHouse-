import clear_data
import error_messages


def get_input_index(index_list):
    while True:
        try:
            print(f"Options: {index_list}")
            string_input = input(f"{prompt_message('id')}\n>  ").strip()
            user_input = int(string_input)
            if user_input in index_list:
                return user_input
            else:
                input(f"Invalid input!\nYour input: {user_input}\nPress enter to continue...")
        except ValueError:
            error_messages.integer_error_massage(string_input)



def get_input_name():
    user_input = input(prompt_message("name")).strip()
    return user_input


def get_input_date():
    print(prompt_message("date"))
    user_input1 = clear_data.get_date()
    print(prompt_message_second("date"))
    user_input2 = clear_data.get_date()
    return user_input1, user_input2


def get_input_price():
    print(prompt_message("price"))
    user_input1 = clear_data.get_decimal()
    print(prompt_message_second("price"))
    user_input2 = clear_data.get_decimal()
    return user_input1, user_input2


def get_input_quantity():
    print(prompt_message("quantity"))
    user_input1 = clear_data.get_integer()
    print(prompt_message_second("quantity"))
    user_input2 = clear_data.get_integer()
    return user_input1, user_input2


def prompt_message(option):
    if option == "id":
        return "What is the product id?"
    elif option == "name":
        return "What is the product name?"
    elif option == "date":
        return "Please provide the first product update date"
    elif option == "quantity":
        return "Please provide the first product quantity"
    elif option == "price":
        return "Please provide the first product price"
    else:
        return None

def prompt_message_second(option):
    if option == "date":
        return "Please provide the second product update date"
    elif option == "quantity":
        return "Please provide the second product quantity"
    elif option == "price":
        return "Please provide the second product price"
    else:
        return None
