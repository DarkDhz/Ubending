import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS UBending")
# Products
mycursor.execute("CREATE TABLE IF NOT EXISTS Products (productID INTEGER AUTO_INCREMENT, owner INTEGER, name VARCHAR(255), "
                 "desc VARCHAR(255), price INTEGER, location VARCHAR(255), state INTEGER,"
                 "image LONGBLOB, idCategory INTEGER"
                 ", PRIMARY KEY (productID))")
# Users
mycursor.execute("CREATE TABLE IF NOT EXISTS Users (userID INTEGER AUTO_INCREMENT, username VARCHAR(255)"
                 " password VARCHAR(255), mail VARCHAR(255), location VARCHAR(255), userphoto LONGBLOB"
                 ", PRIMARY KEY (userID))")
# Following
mycursor.execute("CREATE Table IF NOT EXISTS ProductsFollowing (productID INTEGER, userID INTEGER)")
# Categories
mycursor.execute("CREATE TABLE IF NOT EXISTS Category (categoryID INTEGER AUTO_INCREMENT, name VARCHAR(255)"
                 ", PRIMARY KEY (categoryID))")
sql = "INSERT INTO customers (name) VALUES (%s, %s)"
val = "Cars"
mycursor.execute(sql, val)
val = "Electro"
mycursor.execute(sql, val)

# myresult = mycursor.fetchall()
# print(myresult)
