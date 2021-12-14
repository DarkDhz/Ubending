from app.database import db_host, db_user, db_password, database
import mysql.connector as connection

def _toJson(data):
    return {'id': data[0], 'name': data[1]}


def getAllCategories():
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Category"
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for item in myresult:
        toReturn.append(_toJson(item))

    return toReturn


def getCategoryNameByID(id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT name FROM Category WHERE category_id = " + str(id)
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404

    return myresult[0][0]


def getCategoryByID(id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Category WHERE category_id = " + str(id)
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()
    if len(myresult) == 0:
        return 404

    return _toJson(myresult[0])
