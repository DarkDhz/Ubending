from flask import url_for
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from flask_mail import Message
#from main import mail_svr
import main

secret_key = "ubendinglaostia1234"
email_user = 'ubending.social@gmail.com'
email_pass = 'ubending2021'

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


def get_reset_token(user_id, expires_sec=1800):
    s = Serializer(secret_key, expires_sec) # Token expires in 30min
    return s.dumps({'user_id': user_id})


def verify_reset_token(token):
    s = Serializer(secret_key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token

    return data['user_id']


def send_reset_email(user_id, mail):
    token = get_reset_token(user_id)
    msg = Message('Password Reset Request',
                  sender='noreply@ubending.com',
                  recipients=[mail])
    msg.body = f'''To reset your password visit the following link:
{url_for('resetrequest', token=token, _external=True)}

If you did not make this request, please ignore this email and no changes will be made.
'''
    main.mail_svr.send(msg)
