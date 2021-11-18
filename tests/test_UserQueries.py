from unittest import TestCase
from data import UserQueries


class Test(TestCase):
    user = []

    def test__to_json(self):
        self.fail()
        assertEqual(_toJson(user), {'user_id': 0, 'username': 'Test', 'password': '1234ABCD',
                                    'admin': 0, 'mail': testmail @ gmail.com, 'location': None,
                                    'userphoto': None})

    def test_get_account_by_email(self):
        self.fail()

    def test_get_account_by_id(self):
        self.fail()

    def test_validate_password_format(self):
        self.fail()

    def test_add_user_to_db(self):
        self.fail()

    def test_validate_login(self):
        self.fail()

    def test_update_user_profile(self):
        self.fail()
