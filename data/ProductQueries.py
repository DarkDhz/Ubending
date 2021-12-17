from data.CategoryQueries import getCategoryNameByID
from app.database import db_host, db_user, db_password, database
import mysql.connector as connection
import numpy as np


def convertState(value):
    if value is None:
        return "Brandnew"
    if value == 0:
        return "Brandnew"
    if value == 1:
        return "Used"
    else:
        return "Destroyed"


def productToJson(elem):
    if elem[7] is not None:
        elem[7] = getCategoryNameByID(elem[7])
    if elem[5] is not None:
        elem[5] = convertState(elem[5])
    return {'product_id': elem[0], 'owner_id': elem[1], 'name': elem[2],
            'description': elem[3], 'price': elem[4], 'state': elem[5],
            'image': elem[6], 'category_id': elem[7]}


def setBuyed(user_id, product_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
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
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE owner_id = %s AND buyed = 0"
    values = (user_id,) 
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for elem in myresult:
        toReturn.append(productToJson(list(elem)))
    return toReturn


def getProductById(product_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s"
    values = (product_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404

    return productToJson(list(myresult[0]))


def getProductByIds(user_id, product_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404

    return productToJson(list(myresult[0]))


def addProduct(user_id, data):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()
    query = "INSERT INTO Products (owner_id, name, description, price, state, image, category_id, buyed) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, 0)"
    values = (
        user_id, data['name'], data['description'], data['price'], data['state'], data['image'], data['category_id'])
    mycursor.execute(query, values)
    db.commit()
    lastrow = mycursor.lastrowid
    mycursor.close()
    db.close()
    return lastrow


def deleteProduct(product_id, owner_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()
    query = "DELETE FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, owner_id)
    mycursor.execute(query, values)
    # Delete products from whishlist
    query2 = "DELETE FROM ProductsFollowing WHERE product_id = %s"
    values2 = (product_id,)
    mycursor.execute(query2, values2)
    db.commit()
    mycursor.close()
    db.close()


def updateProduct(product_id, owner_id, data):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()
    if len(data) <= 1 or data is None:
        return 404
    for item in data:
        if data[item] is not None and item != 'token':
            query = "UPDATE Products SET " + item + " = %s WHERE product_id = %s and owner_id = %s"
            values = (data[item], product_id, owner_id,)
            mycursor.execute(query, values)

    db.commit()
    mycursor.close()
    db.close()


def addRating(buyer_id, product_id, value):
    if value < 0 or value > 5:
        return 404

    product_info = getProductById(product_id)
    if product_info == 404:
        return 404

    product_owner = product_info['owner_id']

    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "INSERT INTO Ratings (product_id, user_id, buyer_id, rating) VALUES (%s, %s, %s, %s)"
    values = (product_id, product_owner, buyer_id, value)
    mycursor.execute(query, values)

    db.commit()
    mycursor.close()
    db.close()
    return 201


def getMean(user_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT rating FROM Ratings WHERE user_id = %s"
    values = (user_id,)
    mycursor.execute(query, values)
    result = mycursor.fetchall()
    values = list()
    for element in result:
        values.append(element[0])

    mycursor.close()
    db.close()

    return np.mean(values)


def getFollowingProductsList(user_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM ProductsFollowing WHERE user_id = %s and buyed = 0"
    values = (user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for elem in myresult:
        item = getProductById(elem[0])
        toReturn.append(item)
    return toReturn


def followProduct(product_id, user_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    product_info = getProductById(product_id)
    if product_info == 404:
        return 404

    mycursor = db.cursor()
    query = "INSERT INTO ProductsFollowing (product_id, user_id) " \
            "VALUES (%s, %s)"
    values = (product_id, user_id)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()

    return 0


def unfollowProduct(product_id, user_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()
    query = "DELETE FROM ProductsFollowing WHERE product_id = %s and user_id = %s"
    values = (product_id, user_id)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return 0


def getFollowingProduct(user_id, product_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT * FROM ProductsFollowing WHERE product_id = %s and user_id = %s"
    values = (product_id, user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return False
    return True


def customRatingToJson(data):
    return {'product_id': data[0], 'name': data[1], 'image': data[2], 'owner': data[3]}


def getPendingToValorate(user_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT pr.product_id, pr.name, pr.image, us.username FROM Products pr " \
            "INNER JOIN Users us on pr.owner_id = us.user_id WHERE pr.buyed = 1 and pr.buyer_id = %s"

    values = (user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return 404

    toReturn = list()
    for elem in myresult:
        if not isRated(user_id, mycursor, elem[0]):
            toReturn.append(customRatingToJson(list(elem)))
    mycursor.close()
    db.close()
    return toReturn


def isRated(id, mycursor, product):
    query = "SELECT * FROM Ratings WHERE buyer_id = %s and product_id = %s"
    values = (id, product)
    mycursor.execute(query, values)
    result = mycursor.fetchall()
    if len(result) == 0:
        return False
    return True


def customRatedToJson(data):
    return {'product_id': data[0], 'name': data[1], 'image': data[2], 'valoration': data[3], 'user': data[4]}


def getAlreadyValorate(user_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "SELECT pr.product_id, pr.name, pr.image, R.rating, U.username FROM Products pr " \
            "INNER JOIN Ratings R on pr.product_id = R.product_id INNER JOIN Users U on R.buyer_id = U.user_id" \
            " WHERE pr.buyed = 1 and pr.buyer_id = %s"

    values = (user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for elem in myresult:
        toReturn.append(customRatedToJson(list(elem)))

    return toReturn


'''
# add a rating

import requests
product = 14
token = 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzODU0OTk2NywiZXhwIjoxNjQ0NTQ5OTY3fQ.eyJ1c2VyX2lkIjo5OTN9.W6pDLw17hIoJb3R5krD9lsOy2wZsjeI9PTy4SVsmkdNEFCYDcVxvUVLRDsJW16Dxo7gv2eO4jPNB_dEHK53cEQ'
url = 'http://127.0.0.1:5000/api/rate/' + str(product) + "/" + token
myobj = {'rating': 3}
x = requests.post(url, data=myobj)

# get ratings

import requests
user = 1
url = 'http://127.0.0.1:5000/api/ratings/' + str(user)
x = requests.get(url)
'''
