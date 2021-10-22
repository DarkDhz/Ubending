from app.database import db


def _toJson(data):
    return {'id': data[0], 'name': data[1]}


def getAllCategories():
    mycursor = db.cursor()

    query = "SELECT * FROM Category"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

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

    if len(myresult) == 0:
        return 404

    return myresult[0][0]