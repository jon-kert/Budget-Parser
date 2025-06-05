import test
import hashlib
import os
import psycopg2
from dotenv import load_dotenv

#test.check_psycopg()
test.DB_Connect()   #-- all tables have been created - use as reference for executing SQL Commands

def main_DB_Connect():
    return False

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    #Check if @ Exists
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        cursor = connection.cursor()
        
        cursor.execute("""IF EXISTS (SELECT 1 FROM Users WHERE ID = %s)
                                    THEN 'TRUE'
                                    ELSE 'FALSE' 
                                    END
                                """, username)
        U_exists = cursor.fetchone()
        
        cursor.execute("") #fetch ID associated with Username
        ID = cursor.fetchone()
        
        hashed = hashPass(password)
        cursor.execute("", hashed) # check if hash associated with ID is correct
        P_correct = cursor.fetchone()
        
        cursor.execute("") #Get the secure ID
        Secure_ID = cursor.fetchone()
        
        
        #Pass the Secure_ID Into the transaction/homepage function
        # Potential security risks - ultimately aim to keep ID only accessible through the backend

    except Exception as e:
        print(f"Failed to connect: {e}")    
    