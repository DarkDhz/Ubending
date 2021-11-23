from app.database import host, user, password, database
from app.database import db


def _toJson(data):
    return {'id': data[0], 'name': data[1]}


def getAllCategories():
    mycursor = db.cursor()

    query = "SELECT * FROM Category"
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    mycursor.close()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for item in myresult:
        toReturn.append(_toJson(item))

    return toReturn


def getCategoryNameByID(id):
    mycursor = db.cursor()

    query = "SELECT name FROM Category WHERE category_id = " + str(id)
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    mycursor.close()

    if len(myresult) == 0:
        return 404

    return myresult[0][0]


def _categoryToJSON(data):
    return {"id": data[0], "name": data[1]}


def getCategoryByID(id):
    mycursor = db.cursor()

    query = "SELECT * FROM Category WHERE category_id = " + str(id)
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    mycursor.close()
    if len(myresult) == 0:
        return 404

    return _categoryToJSON(myresult[0])
