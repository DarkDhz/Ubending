from unittest import TestCase
from data.UserQueries import _toJson, addUserToDB, getAccountByID, getAccountByEmail, validatePasswordFormat, \
    validateLogin, updateUserProfile
import requests


class TestUserQueries(TestCase):
    user = [24, 'Test', '1234ABCD', 0, 'testmail@gmail.com', None, None]

    def test__to_json(self):
        self.assertEqual(_toJson(self.user), {'user_id': 24, 'username': 'Test', 'password': '1234ABCD',
                                    'admin': 0, 'mail': 'testmail@gmail.com', 'location': None,
                                    'userphoto': None}, 'The JSON do not match')

    def test_add_user_to_db(self):
        response = addUserToDB(self.user[1], self.user[4], self.user[2])
        self.assertEqual(response, None, "Couldn't add user to db")
        #TODO: Delete user

    def test_get_account_by_email(self):
        # We first add a user to the db
        req = addUserToDB(self.user[1], self.user[4], self.user[2])
        if req is None:
            us = getAccountByEmail(self.user[4])

        self.assertEqual(req, None, "Couldn't add user to db")
        self.assertEqual(us['mail'], _toJson(self.user)['mail'])

        # We now delete the user from db
        #self.user.delete_user()

        # Let's try to find that user again
        #req2 = getAccountByEmail(self.user[4])
        #self.assertEqual(req2, None)

    def test_get_account_by_id(self):
        us = getAccountByID(24)
        self.assertEqual(us['user_id'], 24)

    def test_validate_password_format(self):
        pass1 = '1234ABCD'
        pass2 = '123abc'
        pass3 = 'abcdefgh'
        pass4 = 'abcd1234'

        self.assertEqual(validatePasswordFormat(pass1, pass2), 1, 'Checking for different passwords')
        self.assertEqual(validatePasswordFormat(pass2, pass2), 2, 'Checking for password length')
        self.assertEqual(validatePasswordFormat(pass3, pass3), 3, 'Checking for uppercase letters')
        self.assertEqual(validatePasswordFormat(pass4, pass4), 4, 'Checking for numbers')
        self.assertEqual(validatePasswordFormat(pass1, pass1), 0, 'Password must check all requirements')

    def test_validate_login(self):
        account1 = ['potato', 'abcd1234'] # Wrong email
        account2 = ['2test@gmail.com', 'wrongPass'] # Wrong password
        account3 = ['2test@gmail.com', '123bdhewbdehfvgfvASVCFDgvfj']

        self.assertEqual(validateLogin(account1[0], account1[1]), 404, 'Email does not exist')
        self.assertEqual(validateLogin(account2[0], account2[1]), 400, 'Wrong password')
        self.assertTrue(validateLogin(account3[0], account3[1]), 'Login successful')

    def test_update_user_profile(self):
        self.fail()
        '''data = []
        
        # First lets try to update a user that does not exist
        self.assertEqual(updateUserProfile(0, data), 404, 'User does not exist')
        
        # Now lets update the data of an existing user
        self.assertEqual(updateUserProfile())'''

class TestUserRequests(TestCase):
    user = [25, 'Test2', '1234ABCD', 0, 'testmail2@gmail.com', None, None]

    def test_register(self):
        url = 'http://127.0.0.1:5000/register'
        myobj = {'username': 'Test2', 'mail': 'testmail2@gmail.com', 'password': '1234ABCD',
                 'repeat_password': '1234ABCD'}
        x = requests.post(url, data=myobj)

        self.assertEqual(200, x.status_code)
        self.assertEqual(x.json(), {'message': "Account created succesfully"})

        # Now let's try to register an existing user
        y = requests.post(url, data=myobj)
        self.assertEqual(400, y.status_code)
        self.assertEqual(y.json(), {'message': 'Email already registered.'})

    def test_login(self):
        url = 'http://127.0.0.1:5000/login'
        myobj1 = {'mail': 'potato_mail', 'password': '123bdhewbdehfvgfvASVCFDgvfj'}
        myobj2 = {'mail': '2test@gmail.com', 'password': 'abcd1234'}
        myobj3 = {'mail': '2test@gmail.com', 'password': '123bdhewbdehfvgfvASVCFDgvfj'}
        x = requests.post(url, data=myobj1)
        y = requests.post(url, data=myobj2)
        z = requests.post(url, data=myobj3)

        # Login as a user that does not exist
        self.assertEqual(404, x.status_code)
        self.assertEqual(x.json(), {'message': 'user not found'})

        # Login with an invalid password
        self.assertEqual(400, y.status_code)
        self.assertEqual(y.json(), {'message': 'invalid password'})

        # Successful login
        self.assertEqual(200, z.status_code)

    def test_get_account(self):
        url = 'http://127.0.0.1:5000/userinfo'
        myobj = {'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNjY0OTEzNywiZXhwIjoxNjM2NjQ5NzM3fQ.eyJ1c2VyX2lkIjozfQ.U4fjXix65nT_1xqVKQGVKZoh818kh0Rc1zlUSLMtLnkHOktZ4Rm13YCImedCnZNxS6lTbiI6YSdReBJcCJZ7hQ'}
        x = requests.get(url, data=myobj)

        self.assertEqual(200, x.status_code)
