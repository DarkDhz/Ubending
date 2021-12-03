from data.CategoryQueries import getCategoryNameByID
from app.database import host, user, password, database
import mysql.connector as connection


def convertState(value):
    if value is None:
        return "Brandnew"
    if value == 0:
        return "Brandnew"
    if value == 1:
        return "Used"
    else:
        return "Destroyed"


def _toJson(elem):
    if elem[7] is not None:
        elem[7] = getCategoryNameByID(elem[7])
    if elem[5] is not None:
        elem[5] = convertState(elem[5])
    return {'product_id': elem[0], 'owner_id': elem[1], 'name': elem[2],
            'description': elem[3], 'price': elem[4], 'state': elem[5],
            'image': elem[6], 'category_id': elem[7]}


def setBuyed(user_id, product_id):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()

    query = "UPDATE Products SET buyed = 1, buyer_id = %s WHERE product_id = %s AND owner_id != %s"
    values = (user_id, product_id, user_id)
    mycursor.execute(query, values)

    if mycursor.rowcount == 0:
        return 400

    db.commit()
    mycursor.close()
    db.close()

    return 200


def getAllProductsOfUserByID(user_id):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE owner_id = %s"
    values = (user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    db.close()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for elem in myresult:
        toReturn.append(_toJson(list(elem)))
    return toReturn


def getProductById(product_id):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s"
    values = (product_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    db.close()

    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))


def getProductByIds(user_id, product_id):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    db.close()

    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))


def addProduct(user_id, data):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()
    query = "INSERT INTO Products (owner_id, name, description, price, state, image, category_id) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (
        user_id, data['name'], data['description'], data['price'], data['state'], data['image'], data['category_id'])
    mycursor.execute(query, values)
    db.commit()
    db.close()

    return mycursor.lastrowid


def deleteProduct(product_id, owner_id):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()
    query = "DELETE FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, owner_id)
    mycursor.execute(query, values)
    db.commit()
    db.close()


def updateProduct(product_id, owner_id, data):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()
    if len(data) <= 1 or data is None:
        return 404
    for item in data:
        if data[item] is not None and item != 'token':
            query = "UPDATE Products SET " + item + " = %s WHERE product_id = %s and owner_id = %s"
            values = (data[item], product_id, owner_id,)
            mycursor.execute(query, values)

    db.commit()
    db.close()


def addRating(buyer_id, product_id, value):
    product_info = getProductById(product_id)
    if product_info == 404:
        return 404

    product_owner = product_id['owner_id']

    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()

    query = "INSERT INTO Ratings (product_id, user_id, buyer_id, rating) VALUES (%s, %s, %s, %s)"
    values = (product_id, product_owner, buyer_id, value)
    mycursor.execute(query, values)

    db.commit()
    mycursor.close()
    db.close()
