# 2. Define a class Person and its two child classes: Male and Female. All classes have
# a method "get_gender" which can print "Male" for Male class and "Female" for Female Class.


import mysql.connector


class Person:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def get_gender(self):
        print("Gender:", self.gender)


class Male(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "Male")


class Female(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "Female")


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
select_query = "SELECT first_name, last_name, gender FROM employees"
cur.execute(select_query)

# Fetch all records
records = cur.fetchall()

people = []

# Create instances of Male and Female based on the gender information
for record in records:
    first_name, last_name, gender = record
    if gender == "M":
        people.append(Male(first_name, last_name))
    elif gender == "F":
        people.append(Female(first_name, last_name))

# Print genders
for person in people:
    person.get_gender()
