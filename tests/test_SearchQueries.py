from unittest import TestCase
from data.SearchQueries import *

class TestSearchQueries(TestCase):
    def test_search_by_category(self):
        technologyItems = [{'product_id': 17, 'owner_id': 1, 'name': 'Auriculares',
                            'description': 'not des', 'price': 70, 'state': 'Destroyed',
                            'image': 'jpeg', 'category_id': 'Technology'}, {'product_id': 18,
                            'owner_id': 1, 'name': 'SmartWatch', 'description': 'new',
                            'price': 200, 'state': 'Used', 'image': 'jpeg', 'category_id': 'Technology'}]
        self.assertEqual(searchByCategory(6), technologyItems)

    def test_search_by_name(self):
        self.fail()

    def test_search_by_category_and_name(self):
        self.fail()
