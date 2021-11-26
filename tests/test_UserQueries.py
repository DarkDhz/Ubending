from unittest import TestCase
from data.UserQueries import *
from data.UserQueries import _toJson
from passlib.apps import custom_app_context as pwd_context
import requests


class TestUserQueries(TestCase):
    user = [24, 'Test', '1234ABCD', 0, 'testmail@gmail.com', None, None]

    def test__to_json(self):
        self.assertEqual(_toJson(self.user), {'user_id': 24, 'username': 'Test', 'password': '1234ABCD',
                                              'admin': 0, 'mail': 'testmail@gmail.com', 'location': None,
                                              'userphoto': None}, 'The JSON do not match')

    def test_add_user_to_db(self):
        addUserToDB(self.user[1], self.user[4], self.user[2])
        response = getAccountByEmail(self.user[4])
        self.assertEqual(response['mail'], 'testmail@gmail.com', "Couldn't add user to db")  # User added successfully
        # Delete user
        deleteUserFromDB(response['user_id'])


    def test_delete_user_from_db(self):
        # Add user to db
        addUserToDB("deleteTest", "deleteMail@gmail.com", self.user[2])
        response = getAccountByEmail("deleteMail@gmail.com")
        self.assertEqual(response['mail'], "deleteMail@gmail.com")  # Check that user exists

        # Delete user and try to recover it
        deleteUserFromDB(response['user_id'])
        response2 = getAccountByEmail("deleteMail@gmail.com")
        self.assertEqual(response2, 404) # User deleted successfully

    def test_get_account_by_email(self):
        # We first add a user to the db
        addUserToDB("getMailTest", "getByMail2@gmail.com", self.user[2])
        us = getAccountByEmail("getByMail2@gmail.com")
        # self.assertEqual(req, None, "Couldn't add user to db")
        self.assertEqual(us['mail'], "getByMail2@gmail.com")

        # We now delete the user from db
        deleteUserFromDB(us['user_id'])

        # Let's try to find that user again
        req2 = getAccountByEmail("getByMail2@gmail.com")
        self.assertEqual(req2, 404, 'User should not exist')


    def test_get_account_by_id(self):
        # Add user to db
        addUserToDB("getIdTest", "getIdMail@gmail.com", self.user[2])
        us = getAccountByEmail("getIdMail@gmail.com")
        self.assertEqual(us['mail'], "getIdMail@gmail.com")  # Check that user has been added
        # Get user by id
        response = getAccountByID(us['user_id'])
        self.assertEqual(us, response, 'Users do not match')
        deleteUserFromDB(us['user_id'])

        # Let's try to find that user again
        req2 = getAccountByID(us['user_id'])
        self.assertEqual(req2, 404, 'user should be deleted')

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
        account1 = ['potato', 'abcd1234']  # Wrong email
        account2 = ['testingreal@gmail.com', 'wrongPass']  # Wrong password
        account3 = ['testingreal@gmail.com', '123bdhewbdehfvgfvASVCFDgvfj']

        self.assertEqual(validateLogin(account1[0], account1[1]), 404, 'Email does not exist')
        self.assertEqual(validateLogin(account2[0], account2[1]), 400, 'Wrong password')
        self.assertTrue(validateLogin(account3[0], account3[1]), 'Login successful')


    def test_update_user_profile(self):
        # Add user to db
        addUserToDB("updateUserTest", "updateUserMail2@gmail.com", self.user[2])
        us = getAccountByEmail("updateUserMail2@gmail.com")
        self.assertEqual(us['mail'], "updateUserMail2@gmail.com")  # Check that user has been added

        # Create default data sets
        data1 = {}
        data2 = {'token': us['user_id'], 'username': 'NewName', 'password': 'newPassword1',
                 'repeat_password': 'newPassword1', 'location': None}

        # First lets try to update the user with no data
        self.assertEqual(updateUserProfile(us['user_id'], data1), 404, 'User does not exist')

        # Now lets update the user with new data
        updateUserProfile(us['user_id'], data2)
        us2 = getAccountByID(us['user_id'])
        # Check that the info updated correctly
        self.assertEqual(us2['username'], 'NewName', 'Name did not update correctly')
        self.assertTrue(verify_password('newPassword1', us2['password']), 'Password did not update properly')
        # Delete user from db
        deleteUserFromDB(us['user_id'])


class TestUserRequests(TestCase):
    '''
    def test_register(self):
        url = 'http://127.0.0.1:5000/register'
        myobj = {'username': 'TestAccount', 'mail': 'testmail3@gmail.com', 'password': '1234ABCD',
                 'repeat_password': '1234ABCD'}
        x = requests.post(url, data=myobj)
        self.assertEqual(200, x.status_code)
        self.assertEqual(x.json(), {'message': "Account created succesfully"})
        # Now let's try to register an existing user
        y = requests.post(url, data=myobj)
        self.assertEqual(400, y.status_code)
        self.assertEqual(y.json(), {'message': 'Email already registered.'})
        # Finally, let's delete the test user
        user = getAccountByEmail('testmail3@gmail.com')
        print(user)
        deleteUserFromDB(user['user_id'])
        # Let's try to find that user again
        req2 = getAccountByEmail('testmail3@gmail.com')
        self.assertEqual(req2, 404, 'user should be deleted')


    def test_login(self):

        url = 'http://127.0.0.1:5000/login'
        myobj1 = {'mail': 'potato_mail', 'password': '123bdhewbdehfvgfvASVCFDgvfj'}
        myobj2 = {'mail': 'testingreal@gmail.com', 'password': 'abcd1234'}
        myobj3 = {'mail': 'testingreal@gmail.com', 'password': '123bdhewbdehfvgfvASVCFDgvfj'}
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

    '''


