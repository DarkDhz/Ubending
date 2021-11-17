from app.database import db
from data.ProductQueries import _toJson

__jump = 12


def searchByCategory(category_id, start_point=0):
    cursor = db.cursor()

    query = "SELECT * FROM Products WHERE category_id = %s LIMIT %s,%s"
    values = (category_id, start_point, __jump + start_point,)
    cursor.execute(query, values)

    result = cursor.fetchall()

    if len(result) == 0:
        return 404

    toReturn = list()
    for elem in result:
        toReturn.append(_toJson(list(elem)))
    return toReturn


def searchByName(name, start_point=0):
    cursor = db.cursor()

    query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' LIMIT %s,%s"
    values = (start_point, __jump + start_point,)
    cursor.execute(query, values)

    result = cursor.fetchall()

    if len(result) == 0:
        return 404

    toReturn = list()
    for elem in result:
        toReturn.append(_toJson(list(elem)))
    return toReturn


def searchByCategoryAndName(category_id, name, start_point=0):
    return None


'''
TEST REQUESTS

# get by category
import requests
url = 'http://127.0.0.1:5000/api/search'
myobj = {'category': 1, 'from': 0}
x = requests.post(url, data=myobj)

'''
