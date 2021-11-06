import re
from app.database import db
from flask import g, current_app
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

def _toJson(elem):
    if elem[6] is not None:
        elem[6] = elem[6].decode('ascii')
    return {'user_id': elem[0], 'username': elem[1], 'password': elem[2],
            'admin': elem[3], 'mail': elem[4], 'location': elem[5],
            'userphoto': elem[6]}

def getAccountByEmail(email):
    mycursor = db.cursor()

    query = "SELECT * FROM Users WHERE email = %s"
    values = (email,)

def checkPasswords(password, repeat_password):
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
    query = "INSERT INTO User (username, password, mail) " \
            "VALUES (%s, %s, %s)"
    values = (username, email, password)
    mycursor.execute(query, values)
    db.commit()

def verifyPassword(username, password):
    #return pwd_context.verify(password, self.password)
    user = getAccountByUsername(username)
    return password == user[2]


def generate_auth_token(self, expiration=600):
    s = Serializer(current_app.secret_key, expires_in=expiration)
    return s.dumps({'username': self.username})

