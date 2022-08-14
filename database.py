import mysql.connector
import datetime
from tkinter import *
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    )

cursor = db.cursor()
cursor.execute("SHOW DATABASES")
#check if database is present
for x in cursor:
    if x == "testdb,":
        print("testdb exists!")
        break
else:
    #if not present create database and use
    cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
    cursor.execute("USE testdb")
    print("testdb Database created")

cursor.execute("CREATE TABLE IF NOT EXISTS pet(name VARCHAR(20) NOT NULL, owner VARCHAR(20) NOT NULL, species VARCHAR(20) NOT NULL, sex CHAR(1) NOT NULL, birth DATE NOT NULL, death DATE)")

"""for i in range(1,4):
    name = input(f"Enter#{i} pet's name: ")
    owner = input(f"Enter#{i} owner's name: ")
    species = input(f"Enter#{i} pet's specie: ")
    sex = input(f"Enter#{i} pet's sex: ")
    birth = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    death  = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO pet(name, owner, species, sex, birth, death) VALUES(%s, %s, %s, %s, %s, %s)",(name, owner, species, sex, birth, death))
    db.commit()"""

cursor.execute("SELECT * FROM pet")
records = cursor.fetchall()
for row in records:
    print(f"\n\nNAME: {row[0]}")
    print(f"OWNER: {row[1]}")
    print(f"SPECIES: {row[2]}")
    print(f"SEX: {row[3]}")
    print(f"BIRTH: {row[4]}")
    print(f"DEATH: {row[5]}\n\n")

#query = "SHOW DATABASES"
#cursor.execute(query)




