from data.ProductQueries import productToJson
from app.database import host, user, password, database
import mysql.connector as connection


def searchByCategory(category_id, start_point=0, jump=12, token=None):
    db = connection.connect(host=host, user=user, password=password, database=database)
    cursor = db.cursor()

    if token is None:
        query = "SELECT * FROM Products WHERE category_id = %s and buyed = 0 LIMIT %s,%s"
        values = (category_id, start_point, jump + start_point,)
    else:
        query = "SELECT * FROM Products WHERE category_id = %s and buyed = 0 and owner_id != %s LIMIT %s,%s"
        values = (token, category_id, start_point, jump + start_point,)

    cursor.execute(query, values)

    result = cursor.fetchall()
    db.close()

    if len(result) == 0:
        return 404

    toReturn = list()
    for elem in result:
        toReturn.append(productToJson(list(elem)))
    return toReturn


def searchByName(name, start_point=0, jump=12, token=None):
    db = connection.connect(host=host, user=user, password=password, database=database)
    cursor = db.cursor()

    if token is None:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and buyed = 0 LIMIT %s,%s"
        values = (start_point, jump + start_point,)
    else:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and buyed = 0 and owner_id != %s LIMIT %s,%s"
        values = (token, start_point, jump + start_point,)

    cursor.execute(query, values)

    result = cursor.fetchall()
    db.close()
    if len(result) == 0:
        return 404

    toReturn = list()
    for elem in result:
        toReturn.append(productToJson(list(elem)))
    return toReturn


def searchByCategoryAndName(category_id, name, start_point=0, jump=12, token=None):
    db = connection.connect(host=host, user=user, password=password, database=database)
    cursor = db.cursor()

    if token is None:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and category_id = %s and buyed = 0 LIMIT %s,%s"
        values = (category_id, start_point, jump + start_point,)
    else:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and category_id = %s and buyed = 0 and owner_id != %s LIMIT %s,%s"
        values = (token, category_id, start_point, jump + start_point,)

    cursor.execute(query, values)

    result = cursor.fetchall()
    db.close()
    if len(result) == 0:
        return 404

    toReturn = list()
    for elem in result:
        toReturn.append(productToJson(list(elem)))
    return toReturn


'''
TEST REQUESTS

# get by category
import requests
url = 'http://127.0.0.1:5000/api/search'
myobj = {'category': 1, 'from': 0}
x = requests.post(url, data=myobj)

# get by name
import requests
url = 'http://127.0.0.1:5000/api/search'
myobj = {'name': 'tes', 'from': 0}
x = requests.post(url, data=myobj)

# get by name and category
import requests
url = 'http://127.0.0.1:5000/api/search'
myobj = {'name': 'tes', 'category': 1, 'from': 0}
x = requests.post(url, data=myobj)

'''
