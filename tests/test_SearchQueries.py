from unittest import TestCase
from data.SearchQueries import *
from data.UserQueries import *
from data.ProductQueries import *

class TestSearchQueries(TestCase):
    def test_search_by_category(self):
        technologyItems = [{'product_id': 17, 'owner_id': 1, 'name': 'Auriculares',
                            'description': 'not des', 'price': 70, 'state': 'Destroyed',
                            'image': 'jpeg', 'category_id': 'Technology'}, {'product_id': 18,
                            'owner_id': 1, 'name': 'SmartWatch', 'description': 'new',
                            'price': 200, 'state': 'Used', 'image': 'jpeg', 'category_id': 'Technology'}]
        self.assertEqual(searchByCategory(6), technologyItems)

    def test_search_by_name(self):
        # SEARCH FOR UNEXISTING PRODUCT
        self.assertEqual(searchByName("UnexistingProduct_FBJKSFHBJBFJKBJFBGKJBSFGBMSJKFHJKGSD"), 404)

        # SEARCH FOR EXISTING PRODUCT
        smartwatch = [{'product_id': 18, 'owner_id': 1, 'name': 'SmartWatch', 'description': 'new', 'price': 200, 'state': 'Used', 'image': 'jpeg', 'category_id': 'Technology'}]
        self.assertEqual(searchByName("SmartWatch"), smartwatch)

        # user and product should be created for testing purposes and then deleted when deleteProduct(productID, userID) and deleteUser(userID) work fine

    def test_search_by_category_and_name(self):
        self.fail()

