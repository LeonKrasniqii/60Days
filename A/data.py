import sqlite3
from icecream import ic as print

# Step 1 - Setup / Initialize Database
def get_connection(costumerdb):
    try:
        return sqlite3.connect(costumerdb)
    except Exception as e:
        print(f"Error: {e}")
        raise

# Step 2 - Create a table in the database
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """
    try:
        with connection:
            connection.execute(query)
        print("Table was recreated")
    except Exception as e:
        print(e)

# Step 3 - Add user to database
def insert_user(connection,name:str,age:int,email:str):
    query = "INSERT INTO users (name,age,email) VALUES (?,?,?)"
    try:
        with connection:
            connection.execute(query, (name,age,email))
        print(f"User: {name} was added to your database!")
    except Exception as e:
        print(e)

# Main Function Wrapper
def main():
    connection = get_connection("customer.db")

    try:
#Create table
        create_table(connection)

        start = input("Enter Option (Add,Delete,Update,Search,Add Many):").lower()
        if start == 'add':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            insert_user(connection,name,age,email)
    finally:
        connection.close()


if __name__ =="__main__":
    main()


# Commit our command
# conn.commit()

# Close our connection
# conn.close()