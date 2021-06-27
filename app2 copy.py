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

word = input("Enter the word: ")

query = cursor.execute(
    "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")
