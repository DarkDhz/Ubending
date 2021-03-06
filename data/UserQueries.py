import re

from utils.security import hash_password, verify_password, generate_auth_token, get_reset_token
import mysql.connector as connection

def _toJson(elem):
    return {'user_id': elem[0], 'username': elem[1], 'password': elem[2],
            'admin': elem[3], 'mail': elem[4], 'location': elem[5],
            'userphoto': elem[6]}


def getAccountByEmail(email):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    mycursor = db.cursor()

    query = "SELECT * FROM Users WHERE mail = %s"
    values = (email,)

    mycursor.execute(query, values)

    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()
    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))


def getAccountByID(user_id):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    cursor = db.cursor()

    query = "SELECT * FROM Users WHERE user_id = %s"
    values = (user_id,)

    cursor.execute(query, values)

    result = cursor.fetchall()

    cursor.close()
    db.close()
    if len(result) == 0:
        return 404

    return _toJson(list(result[0]))


def validatePasswordFormat(password, repeat_password):
    if password != repeat_password:
        return 1
    elif len(password) < 8:
        return 2
    elif re.search('[0-9]', password) is None:
        return 3
    elif re.search('[A-Z]', password) is None:
        return 4

    return 0


def addUserToDB(username, email, password):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    mycursor = db.cursor()
    query = "INSERT INTO Users (username, password, mail, admin) " \
            "VALUES (%s, %s, %s, 0)"

    password = hash_password(password)
    values = (username, password, email)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return mycursor.lastrowid


def deleteUserFromDB(user_id):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    mycursor = db.cursor()
    query = "DELETE FROM Users WHERE user_id = " + str(user_id)
    mycursor.execute(query)
    db.commit()
    mycursor.close()
    db.close()

    return mycursor.lastrowid


def validateLogin(mail, password):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    mycursor = db.cursor()
    query = "SELECT * FROM Users WHERE mail = %s"

    values = (mail,)

    mycursor.execute(query, values)
    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()
    if len(myresult) == 0:
        return 404

    if verify_password(password, myresult[0][2]):
        return generate_auth_token(myresult[0][0])
    else:
        return 400


def validateEmail(mail):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    mycursor = db.cursor()
    query = "SELECT * FROM Users WHERE mail = %s"

    values = (mail,)

    mycursor.execute(query, values)
    myresult = mycursor.fetchall()
    mycursor.close()
    db.close()

    if len(myresult) == 0:
        return 404
    return get_reset_token(myresult[0][0])


def updatePassword(user_id, password):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    mycursor = db.cursor()
    query = "UPDATE Users SET password = %s WHERE user_id = %s"
    values = (hash_password(password), user_id['user_id'])
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()


def updateUserProfile(user_id, data):
    db = connection.connect(host="54.36.191.29", user="root", password="ubending", database="Ubending")
    cursor = db.cursor()
    if len(data) == 0 or data is None:
        return 404

    if data['password'] != '':
        if data['repeat_password'] != '':
            result = validatePasswordFormat(data['password'], data['repeat_password'])
            if result != 0:
                return result
            else:
                password = hash_password(data['password'])
                __updateValue('password', password, user_id, cursor)
        else:
            return 5

    if data['repeat_password'] != '' and data['password'] == '':
        return 6

    if data['username'] is not None and data['username'] != '':
        __updateValue('username', data['username'], user_id, cursor)

    if data['location'] is not None and data['location'] != '':
        __updateValue('location', data['location'], user_id, cursor)

    if data['userphoto'] is not None and data['userphoto'] != '':
        __updateValue('userphoto', data['userphoto'], user_id, cursor)

    db.commit()
    cursor.close()
    db.close()


def __updateValue(item, value, user_id, cursor):

    query = "UPDATE Users SET " + item + " = %s WHERE user_id = %s"
    values = (value, user_id)
    cursor.execute(query, values)


"""
REGISTER

import requests
url = 'http://127.0.0.1:5000/register'
myobj = {'username': 'hola', 'mail': 'testingreal@gmail.com', 'password': '123bdhewbdehfvgfvASVCFDgvfj', 'repeat_password': '123bdhewbdehfvgfvASVCFDgvfj'}
x = requests.post(url, data=myobj)
x.json()

LOGIN

import requests
url = 'http://127.0.0.1:5000/login'
myobj = {'mail': 'testingreal@gmail.com', 'password': '123bdhewbdehfvgfvASVCFDgvfj'}
x = requests.post(url, data=myobj)
x.json()

USERINFO

import requests
url = 'http://127.0.0.1:5000/userinfo'
myobj = {'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNjY0OTEzNywiZXhwIjoxNjM2NjQ5NzM3fQ.eyJ1c2VyX2lkIjozfQ.U4fjXix65nT_1xqVKQGVKZoh818kh0Rc1zlUSLMtLnkHOktZ4Rm13YCImedCnZNxS6lTbiI6YSdReBJcCJZ7hQ'}
x = requests.get(url, data=myobj)
x.json()

import requests
url = 'http://127.0.0.1:5000/userinfo'
myobj = {'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNjY0NTYzMiwiZXhwIjoxNjM2NjQ2MjMyfQ.eyJ1c2VyX2lkIjozfQ.icu6kea246nGoBsiuCyBtWiGWkBjiNQq08uxQ1qRGtWy8KGOIfpBI6wmRNAu7rQjOZCKv0wUYG_29DUry1Ifmg', 'username': 'Roberto'}
x = requests.put(url, data=myobj)
x.json()

RESET REQUEST

import requests
url1 = 'http://127.0.0.1:5000/register'
myobj1 = {'username': 'David', 'mail': 'daviddelapaz5@gmail.com', 'password': '1234ABCD', 'repeat_password': '1234ABCD'}
x = requests.post(url1, data=myobj1)
x.json()
url2 = 'http://127.0.0.1:5000/reset_password'
myobj2 = {'mail': 'daviddelapaz5@gmail.com'}
y = requests.post(url2, data=myobj2)
y.json()
"""
