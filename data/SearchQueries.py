from data.CategoryQueries import getCategoryNameByID
from data.ProductQueries import convertState
from app.database import db_host, db_user, db_password, database
import mysql.connector as connection


def searchToJson(elem, fllw):
    if elem[7] is not None:
        elem[7] = getCategoryNameByID(elem[7])
    if elem[5] is not None:
        elem[5] = convertState(elem[5])
    return {'product_id': elem[0], 'owner_id': elem[1], 'name': elem[2],
            'description': elem[3], 'price': elem[4], 'state': elem[5],
            'image': elem[6], 'category_id': elem[7], 'following': fllw}


def searchByCategory(category_id, start_point=0, jump=12, token=None):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    cursor = db.cursor()

    if token is None:
        query = "SELECT * FROM Products WHERE category_id = %s and buyed = 0 LIMIT %s,%s"
        values = (category_id, start_point, jump + start_point,)
    else:
        query = "SELECT * FROM Products WHERE category_id = %s and buyed = 0 and owner_id != %s LIMIT %s,%s"
        values = (token, category_id, start_point, jump + start_point,)

    cursor.execute(query, values)

    result = cursor.fetchall()
    cursor.close()

    return extractProducts(result=result, user_id=token, db=db)


def searchByName(name, start_point=0, jump=12, token=None):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    cursor = db.cursor()

    if token is None:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and buyed = 0 LIMIT %s,%s"
        values = (start_point, jump + start_point,)
    else:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and buyed = 0 and owner_id != %s LIMIT %s,%s"
        values = (token, start_point, jump + start_point,)

    cursor.execute(query, values)

    result = cursor.fetchall()
    cursor.close()

    return extractProducts(result=result, user_id=token, db=db)


def searchByCategoryAndName(category_id, name, start_point=0, jump=12, token=None):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    cursor = db.cursor()

    if token is None:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and category_id = %s and buyed = 0 LIMIT %s,%s"
        values = (category_id, start_point, jump + start_point,)
    else:
        query = "SELECT * FROM Products WHERE name LIKE '%" + name + "%' and owner_id != %s and category_id = %s and buyed = 0 LIMIT %s,%s"
        values = (token, category_id, start_point, jump + start_point,)

    cursor.execute(query, values)
    result = cursor.fetchall()

    cursor.close()

    return extractProducts(result=result, user_id=token, db=db)


def extractProducts(result, user_id, db):
    following = list()
    if len(result) == 0:
        return 404

    if user_id is not None:
        following = getFollowingQuery(user_id=user_id, db=db)

    toReturn = list()
    for elem in result:
        if user_id is None:
            toReturn.append(searchToJson(list(elem), False))
        else:
            toReturn.append(searchToJson(list(elem), checkIfFollowing(following, elem[0])))
    return toReturn


def getFollowingQuery(user_id, db):
    mycursor = db.cursor()

    query = "SELECT product_id FROM ProductsFollowing WHERE user_id = %s"
    values = (user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()
    return myresult


def checkIfFollowing(following: list, product):
    for i in range(len(following)):
        if following[i][0] == product:
            return True
    return False


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
