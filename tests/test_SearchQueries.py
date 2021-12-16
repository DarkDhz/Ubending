from unittest import TestCase
from data.SearchQueries import *
from data.UserQueries import *
from data.ProductQueries import *


class TestSearchQueries(TestCase):
    def test_search_by_category(self):
        technologyItems = {'category_id': 'Technology', 'description': 'Lo vendo porque no lo uso', 'image': 'jpeg',
                           'name': 'Reloj', 'owner_id': 3, 'price': 200, 'product_id': 1, 'state': 'Brandnew', 'following': False}
        self.assertEqual(searchByCategory(6)[0], technologyItems)

    def test_search_by_name(self):
        # SEARCH FOR UNEXISTING PRODUCT
        self.assertEqual(searchByName("UnexistingProduct_FBJKSFHBJBFJKBJFBGKJBSFGBMSJKFHJKGSD"), 404)

        # SEARCH FOR EXISTING PRODUCT
        smartwatch = {'category_id': 'Technology', 'description': 'Lo vendo porque no lo uso', 'image': 'jpeg',
                           'name': 'Reloj', 'owner_id': 3, 'price': 200, 'product_id': 1, 'state': 'Brandnew', 'following': False}
        self.assertEqual(searchByName("Reloj")[0], smartwatch)

        # user and product should be created for testing purposes and then deleted when deleteProduct(productID, userID) and deleteUser(userID) work fine

    def test_search_by_category_and_name(self):
        # SEARCH FOR UNEXISTING PRODUCT OR A PRODUCT WITHIN A WRONG CATEGORY
        self.assertEqual(searchByCategoryAndName(2, "SmartWatch"), 404)
        self.assertEqual(searchByCategoryAndName(6, "Unexisting_SmartWatch"), 404)

        # SEARCH FOR EXISTING PRODUCT
        smartwatch = {'category_id': 'Technology', 'description': 'Lo vendo porque no lo uso', 'image': 'jpeg',
                      'name': 'Reloj', 'owner_id': 3, 'price': 200, 'product_id': 1, 'state': 'Brandnew', 'following': False}
        self.assertEqual(searchByCategoryAndName(6, smartwatch['name'])[0], smartwatch)
