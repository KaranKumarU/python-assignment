# Bonus: Make class Person an abstract class and make get_gender an abstract method in the same class.
# The two child classes must inherit and implement get_gender. i.e., When trying to initialize an
# object of class Person, the program must throw an error.


from abc import ABC, abstractmethod
import mysql.connector


class Person(ABC):
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "Male")

    def get_gender(self):
        print("Gender: Male")


class Female(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "Female")

    def get_gender(self):
        print("Gender: Female")


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
