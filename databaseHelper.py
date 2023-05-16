import sqlite3 
import os



def openDatabase():
    if "excelerators.db"  not in os.listdir():
        
        open("excelerators.db" , "wb").close()
        setUpTables()
    database = sqlite3.connect("excelerators.db")
    cursor.commit()
    return database


def setUpTables():
    database = sqlite3.connect("excelerators.db")
    cursor = database.cursor()
    query1 = """
        create table members(
            member_id int , 
            name varchar(50) ,
            department varchar(20),
            semester int , 
            position varchar(50) 
        )
    """
    cursor.execute(query1)


def getAllData():
    cursor.execute("select * from members")
    data = cursor.fetchall()
    print(data)


def insertMember(data):
    query = """

    insert into members
    values(
        default ,
        data['name'],
        data['dept'],
        data['sem'],
        data['position']

    )
    
    """
    cursor.execute(data)
    cursor.commit()
    

database = openDatabase()
cursor = database.cursor()