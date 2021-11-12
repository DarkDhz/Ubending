from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

secret_key = "ubendinglaostia1234"


'''
@auth.verify_password
def verify_password(token, password):
    user = AccountsModel.verify_auth_token(token)
    if user is not None:
        g.user = user
        return user
@auth.get_user_roles
def get_user_roles(user):
    if user.is_admin == 1:
        return ['admin']
    else:
        return ['user']
'''


def hash_password(password):
    return pwd_context.encrypt(password)


def verify_password(password, hash):
    return pwd_context.verify(password, hash)


def generate_auth_token(user_id, expiration=6000000):
    s = Serializer(secret_key, expires_in=expiration)
    return s.dumps({'user_id': user_id})


def verify_auth_token(token):
    s = Serializer(secret_key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token

    return data['user_id']
