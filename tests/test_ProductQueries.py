from unittest import TestCase
from data.ProductQueries import _toJson, convertState, getAllProductsOfUserByID, getProductById, getProductByIds, addProduct, deleteProduct
import requests


class TestProductQueries(TestCase):
    product = [33, 1, 'potato', 'a really nice potato', 5.0, 1, None, None]

    def test__to_json(self):
        self.assertEqual(_toJson(self.product), {'product_id': 33, 'owner_id': 1, 'name': 'potato',
            'description': 'a really nice potato', 'price': 5.0, 'state': 'Used',
            'image': None, 'category_id': None}, 'The JSON do not match')

    def test_convert_state(self):
        self.assertEqual(convertState(0), "Brandnew")
        self.assertEqual(convertState(1), "Used")
        self.assertEqual(convertState(2), "Destroyed")

    def test_get_all_products_of_user_by_id(self):
        testProductList = [{'category_id': 'Cars',
  'description': 'test',
  'image': '10101',
  'name': 'testing',
  'owner_id': 1,
  'price': 3,
  'product_id': 4,
  'state': 'Used'},
 {'category_id': 'Cars',
  'description': 'test',
  'image': '1',
  'name': 'testing',
  'owner_id': 1,
  'price': 3,
  'product_id': 5,
  'state': 'Used'},
 {'category_id': 'Cars',
  'description': 'AALALAALA',
  'image': '1',
  'name': 'wqrq',
  'owner_id': 1,
  'price': 432,
  'product_id': 6,
  'state': 'Used'}]

        # First search items for nonexisting user
        items = getAllProductsOfUserByID(0)
        self.assertEqual(404, items)

        # Now search products for existing user
        items = getAllProductsOfUserByID(1)
        self.assertEqual(testProductList, items)

    def test_get_product_by_id(self):
        # First search a product that does not exist
        item = getProductById(0)
        self.assertEqual(404, item)

        # Now search for 1st product
        #TODO: Look for an item id that exists

    def test_get_product_by_ids(self):
        # First search a product from a user that does not exist
        item = getProductByIds(0, 1)
        self.assertEqual(404, item)

        # Now search product for existing user
        #TODO: Do item ids even exist? Like seriously

    def test_add_product(self):
        user_id = 23
        data = {"name": "PC", "description": "New PC", "price": 1200, "state": 0, "image": "1", "category_id": 2}
        lastID = addProduct(user_id, data)
        print(lastID)


        productResult = getProductById(lastID)
        print(productResult)

        self.assertEqual(data["name"], productResult["name"], "name")
        self.assertEqual(data["description"], productResult["description"], "desc")
        self.assertEqual(data["price"], productResult["price"], "price")
        self.assertEqual("Brandnew", productResult["state"], "state")
        self.assertEqual(data["image"], productResult["image"], "image")
        self.assertEqual("Bikes", productResult["category_id"], "category_id")

        deleteProduct(lastID)

    def test_delete_product(self):
        user_id = 1
        data = {"name": "PC", "description": "New PC", "price": 1200, "state": "new", "image": 1, "category_id": 2}
        addProduct(user_id, data)

        lastID = 5
        deleteProduct(lastID)
        product5 = getProductById(lastID)

        self.assertEqual(product5, None)

    def test_update_product(self):
        self.fail()
