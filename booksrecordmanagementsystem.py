#Importing Required Modules for the program

from os import system

#Importing mysql connector

import mysql.connector

#Creating database

def create_database():
    con = mysql.connector.connect(host="localhost", user="root", password="ahmed")
    c = con.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS BOOKS;")
create_database()

#Creating table

def create_table():
    con = mysql.connector.connect(host="localhost", user="root", password="ahmed", database="Books")
    c = con.cursor()
    c.execute("SHOW TABLES;")
    data = c.fetchall()
    for i in data:
        if(i == ('bookdata',)):
            break
    else:
        c.execute("CREATE TABLE bookdata(Id INT(11) PRIMARY KEY, Book_Name VARCHAR(1000), Author VARCHAR(70), Publisher Char(100), Edition VARCHAR(15), Pages INT, Copies INT, Quantity BIGINT(20))")
create_table()

#Making Connection

con = mysql.connector.connect(host="localhost", user="root", password="ahmed", database="Books")

#Function to Add_Book

def Add_Book():
    print("{:>60}".format("-->>Add Book Record<<--"))
    Id = input("Enter Book Id: ")
    Book_Name = input("Enter Book Name: ")
    Author = input("Enter Author: ")
    Publisher = input("Enter Publisher: ")
    Edition = input("Enter Edition: ")
    Pages = input("Enter Pages: ")
    Copies = input("Enter Copies: ")
    Quantity = input("Enter Quantity: ")
    data = (Id, Book_Name, Author, Publisher, Edition, Pages, Copies, Quantity)
    #Inserting Book Details in bookdata
    
    sql = 'insert into bookdata values(%s,%s,%s,%s,%s,%s,%s,%s)' 
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key to Continue...")
    menu()

#Function to Display_Employ

def Display_Book():
    print("{:>60}".format("-->>Displaying All Books Records<<--"))
    #query to select all rows from Books (bookdata) Table
    
    sql = 'select * from bookdata'
    c = con.cursor()
    c.execute(sql)

    #Fetching all details of all the Books
    
    r = c.fetchall()
    for i in r:
        print("**********************************")
        print("Id: ", i[0])
        print("Book Name: ", i[1])
        print("Author: ", i[2])
        print("Publisher: ", i[3])
        print("Edition: ", i[4])
        print("Pages: ", i[5])
        print("Copies: ", i[6])
        print("Quantity: ", i[7])
        print("**********************************")
        print("\n")
    press = input("Press Any key to continue...")
    menu()    

#Function to Update_Book
def Update_Book():
    print("{:>60}".format("-->>Update Book Record<<--"))
    Id = input("Enter Id: ")
    print("What do you want to Update? ")
    print("1. Name")
    print("2. Author")
    print("3. Publisher")
    print("4. Edition")
    print("5. Pages")
    print("6. Copies")
    print("7. Quantity")
    ch = int(input("Enter your Update Preference Number from Above (1,2,3,4,5,6,7): "))
    if ch == 1:
        Name = input("Enter Name: ")
        sql = 'UPDATE bookdata set Book_Name = %s where Id = %s'
        data = (Name, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Name")
        print("1. Want to Update more Records\n2. Go back to Menu")
        cho = int(input("Press 1 or 2: "))
        if cho == 1:
            Update_Book()
        else:
            menu()
    elif ch == 2:
        Author = input("Enter Author: ")
        sql = 'UPDATE bookdata set Author = %s where Id = %s'
        data = (Author, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Author")
        print("1. Want to Update more Records\n2. Go back to Menu")
        cho = int(input("Press 1 or 2: "))
        if cho == 1:
            Update_Book()
        else:
            menu()
    elif ch == 3:
        Publisher = input("Enter Publisher: ")
        sql = 'UPDATE bookdata set Publisher = %s where Id = %s'
        data = (Publisher, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Publisher")
        print("1. Want to Update more Records\n2. Go back to Menu")
        cho = int(input("Press 1 or 2: "))
        if cho == 1:
            Update_Book()
        else:
            menu()
    elif ch == 4:
        Edition = input("Enter Edition: ")
        sql = 'UPDATE bookdata set Edition = %s where Id = %s'
        data = (Edition, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Edition")
        print("1. Want to Update more Records\n2. Go back to Menu")
        cho = int(input("Press 1 or 2: "))
        if cho == 1:
            Update_Book()
        else:
            menu()
    elif ch == 5:
        pages = input("Enter Pages: ")
        sql = 'UPDATE bookdata set pages = %s where Id = %s'
        data = (pages, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Pages")
        print("1. Want to Update more Records\n2. Go back to Menu")
        cho = int(input("Press 1 or 2: "))
        if cho == 1:
            Update_Book()
        else:
            menu()
    elif ch == 6:
        copies = input("Enter Copies: ")
        sql = 'UPDATE bookdata set copies = %s where Id = %s'
        data = (copies, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Copies")
        print("1. Want to Update more Records\n2. Go back to Menu")
        cho = int(input("Press 1 or 2: "))
        if cho == 1:
            Update_Book()
        else:
            menu()
    elif ch == 7:
        quantity = input("Enter Quantity: ")
        sql = 'UPDATE bookdata set quantity = %s where Id = %s'
        data = (quantity, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Quantity")
        print("1. Want to Update more Records\n2. Go back to Menu")
        cho = int(input("Press 1 or 2: "))
        if cho == 1:
            Update_Book()
        else:
            menu()
    else:
        print("Invalid Choice\nTry Again")
        menu()

#Function to Remove_Book
def Remove_Book():
    print("{:>60}".format("-->> Remove Book Record <<--"))
    Id = input("Enter Id: ")
    sql = 'delete from bookdata where id = %s'
    data = (Id,)
    c = con.cursor()
    #executing the sql query
    c.execute(sql, data)
    #commit method to make changes in the empdata table
    con.commit()
    print("Book Record Removed")
    press = input("Press Any key To Continue...")
    menu()

#Function to Search_Book
def Search_Book():
    print("{:>60}".format("-->> Search Book Record <<--"))
    Id = input("Enter Id: ")
    sql = 'select * from bookdata where id = %s'
    data = (Id,)
    c = con.cursor()
    c.execute(sql, data)
    r = c.fetchall()
    for i in r:
        print("**********************************")
        print("Id: ", i[0])
        print("Book Name: ", i[1])
        print("Author: ", i[2])
        print("Publisher: ", i[3])
        print("Edition: ", i[4])
        print("Pages: ", i[5])
        print("Copies: ", i[6])
        print("Quantity: ", i[7])
        print("**********************************")
        print("\n")
    press = input("Press Any key to continue...")
    menu()

#Menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("******************************************"))
    print("{:>60}".format("--> Books Records Management System <--"))
    print("{:>60}".format("******************************************"))
    print("1. Add Book")
    print("2. Display All Book Records")
    print("3. Update Book Record")
    print("4. Remove Book Record")
    print("5. Search Book Record")
    print("6. Exit\n")
    print("{:>60}".format("--> Choice Options: [1/2/3/4/5/6] <--"))

    ch = int(input("Enter your Choice :"))
    if ch == 1:
        system("cls")
        Add_Book()
    elif ch == 2:
        system("cls")
        Display_Book()
    elif ch == 3:
        system("cls")
        Update_Book()
    elif ch == 4:
        system("cls")
        Remove_Book()
    elif ch == 5:
        system("cls")
        Search_Book()
    elif ch == 6:
        system("cls")
        print("{:>60}".format("Exiting..."))
    else:
        print("Invalid Choice!")
        press = input("Press Any key to continue...")
        menu()
        
#Calling menu funtion
menu()


