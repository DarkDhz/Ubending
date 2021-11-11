import re
from app.database import db
from utils.security import hash_password, verify_password, generate_auth_token


def _toJson(elem):
    if elem[6] is not None:
        elem[6] = elem[6].decode('ascii')
    return {'user_id': elem[0], 'username': elem[1], 'password': elem[2],
            'admin': elem[3], 'mail': elem[4], 'location': elem[5],
            'userphoto': elem[6]}


def getAccountByEmail(email):
    mycursor = db.cursor()

    query = "SELECT * FROM Users WHERE mail = %s"
    values = (email,)

    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))


def getAccountByID(user_id):
    cursor = db.cursor()

    query = "SELECT * FROM Users WHERE user_id = %s"
    values = (user_id,)

    cursor.execute(query, values)

    result = cursor.fetchall()

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
    mycursor = db.cursor()
    query = "INSERT INTO Users (username, password, mail, admin) " \
            "VALUES (%s, %s, %s, 0)"

    password = hash_password(password)
    values = (username, password, email)
    mycursor.execute(query, values)
    db.commit()


def validateLogin(mail, password):
    mycursor = db.cursor()
    query = "SELECT * FROM Users WHERE mail = %s"

    values = (mail,)

    mycursor.execute(query, values)
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    if verify_password(password, myresult[0][2]):
        return generate_auth_token(myresult[0][0])
    else:
        return 400


def updateUserProfile(user_id, data):
    if len(data) == 0 or data is None:
        return 404

    cursor = db.cursor()

    for item in data:
        if data[item] is not None and item != 'token':
            query = "UPDATE Users SET " + item + " = %s WHERE user_id = %s"
            values = (data[item], user_id)
            cursor.execute(query, values)

    db.commit()


"""
REGISTER

import requests
url = 'http://127.0.0.1:5000/register'
myobj = {'username': 'hola', 'mail': '2test@gmail.com', 'password': '123bdhewbdehfvgfvASVCFDgvfj', 'repeat_password': '123bdhewbdehfvgfvASVCFDgvfj'}
x = requests.post(url, data=myobj)
x.json()

LOGIN

import requests
url = 'http://127.0.0.1:5000/login'
myobj = {'mail': '2test@gmail.com', 'password': '123bdhewbdehfvgfvASVCFDgvfj'}
x = requests.post(url, data=myobj)
x.json()

USERINFO

import requests
url = 'http://127.0.0.1:5000/userinfo'
myobj = {'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNjY0MzI2NywiZXhwIjoxNjM2NjQzODY3fQ.eyJ1c2VyX2lkIjozfQ.TrwAJqBiEdIjoslKRvcB4CQ0pkRtZ4WvNqWU-eMgcdhEREAsoXL9fvSfj81D6R0VAbzeAolUCwNYFvWCCsyKnQ'}
x = requests.get(url, data=myobj)
x.json()

import requests
url = 'http://127.0.0.1:5000/userinfo'
myobj = {'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNjY0NTYzMiwiZXhwIjoxNjM2NjQ2MjMyfQ.eyJ1c2VyX2lkIjozfQ.icu6kea246nGoBsiuCyBtWiGWkBjiNQq08uxQ1qRGtWy8KGOIfpBI6wmRNAu7rQjOZCKv0wUYG_29DUry1Ifmg', 'username': 'Roberto'}
x = requests.put(url, data=myobj)
x.json()


"""
