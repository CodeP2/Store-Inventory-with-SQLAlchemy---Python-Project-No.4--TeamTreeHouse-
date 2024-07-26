## Important Information Read This:

**Before we start I need to explain of why I do have 2 folders in my repository the reason for that is one is an extended code with using different imports and such and the other is for purely exceed expectation.**

Important Note I did create more files because I want my code to be at least more easier to read.
Instead of being a nightmare to read.

Explaination how the code works:
    
    * inventory_db.py:
        - autorincrement=True used to ensure uniqe id's.
    
    * Export_to_csv.py:
        - instead of using sqlite3 to connect to my database I use sqlalchemy which uses engine to connect: 
            with engine.connect() as connection:
                connection.execute(some_table.insert(), {"x": 7, "y": "this is some data"})
                connection.execute(
                some_other_table.insert(), {"q": 8, "p": "this is some more data"}
            )

            connection.commit()  # commit the transaction
        
        in my case I execute my query to find all entries from my database
        - .fetchall() give me specifically rows form database while .keys() headers
        - custom file name with added "_backup" string
    
    * import_csv.py:
        - added IntegrityError which is Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails.
    
    * search_entry.py:
        - added global var so if the user want to keep looking it will loop but if they decide not to it will return user to main menu without anoying ("I have to leave 2 menus!")


Personal Notes:

    * in inventory_db.py:
        - for price I would rather use decimal in sql alchemy Numeric reason for that is:
            
            1. price clarity and easier to read (499 vs 4.99)
            2. It will be required in a job scenario
            3. its a better pratice overall

        links: 
            - https://docs.python.org/3/library/decimal.html#module-decimal
            - https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Numeric

    * in all files for exeeds_expectation_code:
        
        -I was trying to use only sqlalchemy module instead of other similar modules like:
            
            - sqlite3
            - mysql.connector
            - psycopg2
            - pyodbc
            - cx_Oracle

        -I was trying to use only csv module instead of other similar modules like:

            - pandas
            - vaex
            - polars
            - databricks.koalas
            - PySpark
            - cuDF (RAPIDS)
            - dask.dataframe

        - all of this modules are a bit different but in a way similar but one might better to use for large data and so on and forth


While updating this README file I'm not sure how much I should explain more of my code or give even more links to documents for python or sqlalchemy because I feel like there's all ready a lot I have been using code from my previous project so I know what it does with the difference of using only csv and sqlalchemy only in this one but other than that like looking for entries and such its just the same code as I was already doing in my previous project so again I feel like there's no need to eplain more about it unless I will be asked to which if I have I will explain my code more if needed.


Links: 
- https://github.com/CodeP2/SQL-Alchemy-Practice-Python
- https://docs.python.org/3/library/sqlite3.html
- https://docs.sqlalchemy.org/en/20/core/connections.html#module-sqlalchemy.engine
- https://docs.sqlalchemy.org/en/20/errors.html
- https://docs.python.org/3/library/functions.html#getattr
- https://docs.sqlalchemy.org/en/20/orm/contextual.html#sqlalchemy.orm.scoped_session.rollback
- https://docs.python.org/3/library/os.path.html#module-os.path
