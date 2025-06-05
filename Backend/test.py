# Sandbox programs
# For learning do incorporate certain features into our program

import psycopg2
from dotenv import load_dotenv
import os
#import hashlib

def DB_Connect():
    print("Executing db access test...")
    load_dotenv()

    # Fetch variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    # Connect to the database
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        print("Connection successful!")

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Example query
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        print("Current Time:", result)
        
        #cursor.execute("DROP TABLE Transactions;")
        #cursor.execute("DROP TABLE hashedpasses;")
        
        #cursor.execute("DROP TABLE users;")
        

        #CREATE TYPE IF NOT EXISTS user_type AS ENUM ('Client', 'Admin');
        # IF NOT EXISTS so that we dont make duplicate "TestPerson" tables
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Users (
                    ID SERIAL PRIMARY KEY,
                    username VARCHAR(255),
                    account_created DATE,
                    role user_type NOT NULL
                    );""")
        connection.commit()
        print("Users table created...")
        
        # Planning on using SHA-1 hashing, which requires 40 characters of space
        #Recheck if the ID is even necessary??
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS HashedPasses (
                       ID INT PRIMARY KEY,
                       hash CHAR(40),
                       FOREIGN KEY (ID) REFERENCES Users(ID),
                       secure_id INT UNIQUE
                       );""")
        connection.commit()
        print("HashedPasses table created...")

        #CREATE TYPE transaction_type AS ENUM ('out', 'in');
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS Transactions (
                       TransactionID SERIAL PRIMARY KEY,
                       user_id INT,
                       transaction_date DATE,
                       FOREIGN KEY (user_id) REFERENCES HashedPasses(secure_id),
                       transaction_amount money,
                       transaction_type transaction_type NOT NULL
                       );""")
        connection.commit()
        print("Transactions table created...")
        print("All tables created successfully! Check Supabase for Tables")

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")

    except Exception as e:
        print(f"Failed to connect: {e}")
    
def check_psycopg():
    print("Module path:", psycopg2.__file__)
    print("Type:", type(psycopg2))
    print("Has attribute cursor?", hasattr(psycopg2, "cursor"))
    
def create_account():
    username = input("Enter a Username: ")
    name = input("Enter your full name: ")
    password = input("Enter a password: ")
    #Access the db, and check if the username exists. If so, do not make the account
    
    #if does not yet exist, 
    
    
    print("account created!")

#def access_account():