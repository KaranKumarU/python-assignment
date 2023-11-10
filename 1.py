# 1. Create a table with a large number of records (you can find it with a google search or use this
# link - https://github.com/datacharmer/test_db). Use MySQL Database. One can setup MySQL on
# localhost. Write some basic queries using python. Suppose you want to process/fetch a large
# number of records using python while keeping your memory usage low. Think of approaches on
# how to accomplish this and implement it.
# Hint: Use Generator

import mysql.connector


try:
    db = mysql.connector.connect(
        host="localhost",
        user="ukarankumar",
        password="Ukaran@11.ku",
    )

except Exception as e:
    print("Error connecting to MySQL:", e)
    exit(1)

cur = db.cursor()
cur.execute("use employees")
cur.execute("SELECT * FROM employees")


def fetch_records(cursor):
    while True:
        records = cur.fetchall()
        if not records:
            break
        yield records


for record in fetch_records(cur):
    for result in record:
        print(result)
