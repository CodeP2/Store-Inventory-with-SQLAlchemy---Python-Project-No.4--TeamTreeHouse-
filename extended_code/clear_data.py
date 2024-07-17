import error_messages
import datetime
from decimal import Decimal, InvalidOperation


def get_date():
        while True:
            try:
                get_date = input("Product updated (Example: 09/28/2015): ")
                segments = [segment.strip() for segment in get_date.split("/")]
                joined_segments = "/".join(segments)
                date = datetime.datetime.strptime(joined_segments, '"%m/%d/%Y"').date()
                return date
            except ValueError as err:
                error_messages.data_convertion_error_message(err, get_date, "")


def get_decimal():
    while True:
        try:
            get_decimal = input("Product price (Example: 12.99): ")
            striped_get_decimal = get_decimal.strip()
            decimal_value = Decimal(striped_get_decimal)
            if decimal_value.as_tuple().exponent < -2:
                raise ValueError("More than two decimal spaces")
            return decimal_value
        except (InvalidOperation, ValueError) as err:
            error_messages.data_convertion_error_message(err, get_decimal, "19.99 (where . is a period not a comma and no currency sign!)")


def get_integer():
    while True:
        try:
            get_string = input("Product quantitiy (Example: 85): ").strip()
            get_integer = int(get_string)
            return get_integer
        except ValueError as err:
            error_messages.data_convertion_error_message(err, get_string, "85")
