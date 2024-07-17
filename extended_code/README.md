Before we start I need to explain to why did I use for product_price is:

- Numeric in database but converted as DECIMAL instead of Integer
- Integer does not take 3.99 for example as an argument therefore I have to change the price to 399
- using Integer instead of Numeric is miss leading because people who are not a programer prefer to understand the information form just reading instead of figuring out if its 399 or 3.99

the reason for that is the practice for working with real world databases

Explaination how the code works:
- autorincrement=True used to ensure uniqe id's 


for this project code I will also be using my repository for SQL alchemy database as from where I did learned how to use said code the only difference might be using csv import instead of panda import for importing inventory.csv file to my database.

Links: 
- https://github.com/CodeP2/SQL-Alchemy-Practice-Python