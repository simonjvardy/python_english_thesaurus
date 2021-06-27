import mysql.connector
from decouple import config

# Pull environment variables from .env file
USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
DATABASE = config('DATABASE')

# mysql connection credentials
con = mysql.connector.connect(
    user=USERNAME,
    password=PASSWORD,
    host=HOST,
    database=DATABASE
)

cursor = con.cursor()


def translate(word):
    """
    Function to take the user input word and search the dictionary keys to
    return the associated value.
    Queries a cloud based mysql database using SQL statements to return the
    dictionary table results.
    """

    # Converts the input word to lower case to match with the database field.
    word = word.lower()

    query = cursor.execute(
        "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()

    if results:
        for result in results:
            print(result[0])
    else:
        print("No word found!")


# User input request - enter a word to look up
user_input = input("Enter word: ")

# Fuction call with the user input as an argument
translate(user_input)