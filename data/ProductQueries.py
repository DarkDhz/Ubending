from app.database import db
from data.CategoryQueries import getCategoryNameByID

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
    if elem[6] is not None:
        elem[6] = elem[6].decode('ascii')
    if elem[7] is not None:
        elem[7] = getCategoryNameByID(elem[7])
    if elem[5] is not None:
        elem[5] = convertState(elem[5])
    return {'product_id': elem[0], 'owner_id': elem[1], 'name': elem[2],
            'description': elem[3], 'price': elem[4], 'state': elem[5],
            'image': elem[6], 'category_id': elem[7]}


def getAllProductsOfUserByID(user_id):
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE owner_id = %s"
    values = (user_id,)
    print(user_id)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for elem in myresult:
        toReturn.append(_toJson(list(elem)))
    return toReturn


def getProductById(product_id):
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s"
    values = (product_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))


def getProductByIds(user_id, product_id):
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))


def addProduct(user_id, data):
    mycursor = db.cursor()
    print(data)
    query = "INSERT INTO Products (owner_id, name, description, price, state, image, category_id) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (user_id, data['name'], data['description'], data['price'], data['state'], data['image'], data['category_id'])
    mycursor.execute(query, values)
    db.commit()

def deleteProduct(product_id, owner_id):

    mycursor = db.cursor()
    query = "DELETE FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, owner_id)
    mycursor.execute(query, values)
    db.commit()


def updateProduct(product_id, owner_id, data):
    mycursor = db.cursor()
    print(data)
    for item in data:
        if data[item] is not None:
            query = "UPDATE Products SET " + item + " = %s WHERE product_id = %s and owner_id = %s"
            values = (data[item], product_id, owner_id,)
            mycursor.execute(query, values)

    db.commit()
    # myresult = mycursor.fetchall()
    # print(myresult)

"""
import requests
url = 'http://127.0.0.1:5000/user/3/product'
myobj = {'price': '299', 'name': 'testing', 'description': 'hola', 'state': 0}
x = requests.post(url, data=myobj)
"""




