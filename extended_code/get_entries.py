def get_entry_values_by(column_name):
    return [item[0] for item in Inventory_db.session.query(column_name)]


def Index_list():
    return get_entry_values_by(getattr(Inventory_db.Product, "id"))


def collect_entries(column_name):
    empty_list = []
    column = getattr(books_holder.Books, column_name)
    for entry in books_holder.session.query(column):
        empty_list.append(entry)
    return empty_list, column


def stop_entries(entry, date=False, decimal=False):
    counter = 0
    for item in entry:
        if date:
            print(datetime.datetime.strftime(item[0], '%B %d, %Y'))
        elif decimal:
            print(float(item[0]))
        else:
            print(item[0])
        counter += 1
        if counter == 5:
            input("press enter to continue...")
            counter = 0