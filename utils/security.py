from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

secret_key = "ubendinglaostia1234"


def hash_password(password):
    return pwd_context.encrypt(password)


def verify_password(password, hash):
    return pwd_context.verify(password, hash)


def generate_auth_token(user_id, expiration=600):
    s = Serializer(secret_key, expires_in=expiration)
    return s.dumps({'username': user_id})


def verify_auth_token(cls, token):
    s = Serializer(secret_key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token

    #TODO REPLACE WITH MYSQL NOT POSTGRESS
    user = cls.query.filter_by(username=data['username']).first()

    return user
