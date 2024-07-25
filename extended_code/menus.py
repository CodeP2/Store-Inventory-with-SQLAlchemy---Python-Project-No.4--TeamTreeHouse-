def main_menu():
    print("""Inventory Program Main Menu 
          \rv) Search product
          \ra) Add, Edit or Delete a new product
          \rb) backup your database entries
          \rx) Exit Program
        """)


def menu_v():
    print("""Search Product Menu
          \r1) Search by id
          \r2) Search by name
          \r3) Search by update date
          \r4) Search by quantity
          \r5) Search by price
          \r6) Exit Menu
          """)


def menu_a():
    print("""Add/Edit/Delete Product Menu
          \r1) Add a new Product
          \r2) Edit a product
          \r3) Delete a product
          \r4) Exit Menu
          """)


def menu_b():
    print("""Back-up Database Menu
          \r1) To back-up your database
          \r2) Exit Menu
          """)


def edit_menu():
    print(""""What kind of entry would you like to change?
          \r1) Product Name
          \r2) Product Quantity
          \r3) Product Price
          \r4) Date updated
          \r5) Finish editing and exit menu
          \r6) Exit Menu
          """)
