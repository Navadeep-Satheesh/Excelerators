import sqlite3
import os 

create_commands = [
    
]

if "database.db"  not in os.listdir() :
    file  = open("database.db" , "wb")
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    for command in create_commands:
        cursor.execute(command)
        connection.commit()
    file.close()

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

if __name__ == "__main__":
    command = ""
    while command != "exit":
        command = input("-->")
        try:
            cursor.execute(command)
            data= cursor.fetchall()
            for row in data:
                print(row)

            connection.commit()
        except Exception as e:
            print(e)


