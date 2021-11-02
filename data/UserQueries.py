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

def getAccountByUsername(username):
    mycursor = db.cursor()

    query = "SELECT * FROM Users WHERE username = %s"
    values = (username,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))

def verifyPassword(username, password):
    #return pwd_context.verify(password, self.password)
    user = getAccountByUsername(username)
    return password == user[2]


def generate_auth_token(self, expiration=600):
    s = Serializer(current_app.secret_key, expires_in=expiration)
    return s.dumps({'username': self.username})
