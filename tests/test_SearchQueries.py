from unittest import TestCase
from data.SearchQueries import *
from data.UserQueries import *
from data.ProductQueries import *


class TestSearchQueries(TestCase):
    def test_search_by_category(self):
        technologyItems = [{'product_id': 17, 'owner_id': 1, 'name': 'Auriculares',
                            'description': 'not des', 'price': 70, 'state': 'Destroyed',
                            'image': 'jpeg', 'category_id': 'Technology'}, {'product_id': 18,
                                                                            'owner_id': 1, 'name': 'SmartWatch',
                                                                            'description': 'asdasd',
                                                                            'price': 2000, 'state': 'Destroyed',
                                                                            'image': 'jpeg',
                                                                            'category_id': 'Technology'}]
        self.assertEqual(searchByCategory(6)[:2], technologyItems)

    def test_search_by_name(self):
        # SEARCH FOR UNEXISTING PRODUCT
        self.assertEqual(searchByName("UnexistingProduct_FBJKSFHBJBFJKBJFBGKJBSFGBMSJKFHJKGSD"), 404)

        # SEARCH FOR EXISTING PRODUCT
        smartwatch = [{'product_id': 18, 'owner_id': 1, 'name': 'SmartWatch', 'description': 'asdasd', 'price': 2000,
                       'state': 'Destroyed', 'image': 'jpeg', 'category_id': 'Technology'}]
        self.assertEqual(searchByName("SmartWatch"), smartwatch)

        # user and product should be created for testing purposes and then deleted when deleteProduct(productID, userID) and deleteUser(userID) work fine

    def test_search_by_category_and_name(self):
        # SEARCH FOR UNEXISTING PRODUCT OR A PRODUCT WITHIN A WRONG CATEGORY
        self.assertEqual(searchByCategoryAndName(2, "SmartWatch"), 404)
        self.assertEqual(searchByCategoryAndName(6, "Unexisting_SmartWatch"), 404)

        # SEARCH FOR EXISTING PRODUCT
        smartwatch = [
            {'product_id': 18, 'owner_id': 1, 'name': 'SmartWatch', 'description': 'asdasd', 'price': 2000, 'state': 'Destroyed',
             'image': 'jpeg', 'category_id': 'Technology'}]
        self.assertEqual(searchByCategoryAndName(6, "SmartWatch"), smartwatch)
