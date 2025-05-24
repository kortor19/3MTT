import mysql.connector
from datetime import date
import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lubem",
    database="testdatabase"
)

#to execute mysql query and hold result from python code, cursor object is required
mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")
#mycursor.execute("CREATE TABLE person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("DESCRIBE person")
# for x in mycursor:
#     print(x)

#mycursor.execute("INSERT INTO person (name, age) VALUES ('bernard', 41)")

#mycursor.execute("INSERT INTO person (name, age) VALUES (%s, %s)", ("Lubem", 45))
#db.commit()

#mycursor.execute("SELECT * FROM person")

#mycursor.execute("CREATE TABLE users(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))")
#mycursor.execute("CREATE TABLE scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)")

#mycursor.execute("DESCRIBE users")
#mycursor.execute("SHOW TABLES")

#mycursor.execute(" SHOW DATABASES")

user = [
    ("Bernard", "lubem"),
    ("Joe", "Joseph")
]


user_score = [
    (50, 60),
    (80, 90)
]
#mycursor.executemany("INSERT INTO users(name, passwd) VALUES (%s, %s)", user)
mycursor.executemany("INSERT INTO scores(userId, game1, game2) VALUES (%s, %s, %s)")

db.commit()

for x in mycursor:
    print(x)

