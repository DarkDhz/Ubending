from unittest import TestCase
from data.CategoryQueries import *


class TestCategoryQueries(TestCase):
    def test__to_json(self):
        self.fail()

    def test_get_all_categories(self):
        allCategories = [{'id': 1, 'name': 'Cars'},
                         {'id': 2, 'name': 'Bikes'},
                         {'id': 3, 'name': 'Toys'},
                         {'id': 4, 'name': 'Home'},
                         {'id': 5, 'name': 'Sports'},
                         {'id': 6, 'name': 'Technology'},
                         {'id': 7, 'name': 'Videogames'},
                         {'id': 8, 'name': 'Clothes'},
                         {'id': 9, 'name': 'Plants'},
                         {'id': 10, 'name': 'Books & Music'},
                         {'id': 11, 'name': 'Cinema'},
                         {'id': 12, 'name': 'Pet adoption'}]

        self.assertEqual(getAllCategories(), allCategories, "Error with getAllCategories().")

    def test_get_category_name_by_id(self):
        self.fail()

    def test__category_to_json(self):
        self.fail()

    def test_get_category_by_id(self):
        self.fail()
