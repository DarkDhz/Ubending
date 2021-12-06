from unittest import TestCase
from data.ProductQueries import _toJson, convertState, getAllProductsOfUserByID, getProductById, getProductByIds, \
    addProduct, deleteProduct, updateProduct, followProduct, unfollowProduct, getFollowingProduct, \
    getFollowingProductsList
from data.UserQueries import *
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
        # CREATE TESTING USER AND THE TWO TESTING PRODUCTS
        userID = addUserToDB("userPostingProduct-TESTAddProduct", "userpostingtest@gmail.com", "aaa")
        data0 = {"name": "PC", "description": "New PC", "price": 1200, "state": 0, "image": None, "category_id": 2}
        data1 = {"name": "testing", "description": "test", "price": 3, "state": 0, "image": None, "category_id": 2}
        productID0 = addProduct(userID, data0)
        productID1 = addProduct(userID, data1)

        # DEFINE PRODUCT TEST LIST
        testProductList = [{'category_id': 'Bikes',
                            'description': 'New PC',
                            'image': None,
                            'name': 'PC',
                            'owner_id': userID,
                            'price': 1200,
                            'product_id': productID0,
                            'state': 'Brandnew'},
                           {'category_id': 'Bikes',
                            'description': 'test',
                            'image': None,
                            'name': 'testing',
                            'owner_id': userID,
                            'price': 3,
                            'product_id': productID1,
                            'state': 'Brandnew'}]

        # SEARCH ITEMS FOR NON-EXISTING USER
        productList = getAllProductsOfUserByID(0)
        self.assertEqual(404, productList)

        # SEARCH PRODUCTS FOR EXISTING USER
        productList = getAllProductsOfUserByID(userID)
        self.assertEqual(testProductList, productList)

        # DELETE PRODUCTS
        deleteProduct(productID0, userID)
        deleteProduct(productID1, userID)

        # DELETE TESTING USER
        deleteUserFromDB(userID)

    def test_get_product_by_id(self):
        # First search a product that does not exist
        item = getProductById(0)
        self.assertEqual(404, item)

        # Now search for 1st product
        # TODO: Look for an item id that exists

    def test_get_product_by_ids(self):
        # First search a product from a user that does not exist
        item = getProductByIds(0, 1)
        self.assertEqual(404, item)

        # Now search product for existing user
        # TODO: Do item ids even exist? Like seriously

    def test_add_product(self):
        userID = addUserToDB("userPostingProduct-TESTAddProduct", "userpostingtest@gmail.com", "aaa")
        data = {"name": "PC", "description": "New PC", "price": 1200, "state": 0, "image": None, "category_id": 2}
        productID = addProduct(userID, data)
        product = getProductById(productID)

        self.assertEqual(data["name"], product["name"], "Not same name.")
        self.assertEqual(data["description"], product["description"], "Not same description.")
        self.assertEqual(data["price"], product["price"], "Not same price.")
        self.assertEqual("Brandnew", product["state"], "Not same state.")
        self.assertEqual(data["image"], product["image"], "Not same image.")
        self.assertEqual("Bikes", product["category_id"], "Not same category_id.")

        deleteProduct(productID, userID)
        deleteUserFromDB(userID)

    def test_delete_product(self):
        userID = addUserToDB("userDeletingProduct-TESTDeleteProduct", "userdeletingtest@gmail.com", "aaa")
        data = {"name": "PC", "description": "New PC", "price": 1200, "state": 0, "image": "1", "category_id": 2}

        productID = addProduct(userID, data)
        productDeleted = deleteProduct(productID, userID)

        self.assertEqual(productDeleted, None, "Product does exist.")

        deleteUserFromDB(userID)

    def test_update_product(self):
        userID = addUserToDB("userUpdatingProduct-TESTUpdateProduct", "userupdatingtest@gmail.com", "aaa")

        data = {"name": "PC", "description": "New PC", "price": 1200, "state": 0, "image": None, "category_id": 2}
        productID = addProduct(userID, data)

        newData = {"name": "Bike", "description": "Old used bike", "price": 200, "state": 1, "image": None,
                   "category_id": 2}
        updateProduct(productID, userID, newData)

        product = getProductById(productID)

        self.assertEqual(newData["name"], product["name"], "Not same name.")
        self.assertEqual(newData["description"], product["description"], "Not same description.")
        self.assertEqual(newData["price"], product["price"], "Not same price.")
        self.assertEqual("Used", product["state"], "Not same state.")
        self.assertEqual(newData["image"], product["image"], "Not same image.")
        self.assertEqual("Bikes", product["category_id"], "Not same category_id.")

        deleteProduct(productID, userID)
        deleteUserFromDB(userID)


"""
class TestProductRequests(TestCase):
    def test_get_product(self):
        # CREATE A USER
        url0 = 'http://127.0.0.1:5000/register'
        myobj0 = {'username': 'ProductsTesting', 'mail': 'producttesting@gmail.com', 'password': '1234ABCD', 'repeat_password': '1234ABCD'}
        x = requests.post(url0, data=myobj0)
        testUser = getAccountByEmail('producttesting@gmail.com')
        userID = testUser['user_id']

        # DEFINE A PRODUCT
        data = {"name": "PC", "description": "New PC", "price": 1200, "state": 0, "image": "1", "category_id": 2}
        productID = addProduct(userID, data)

        # GET PRODUCT REQUEST
        url = 'http://127.0.0.1:5000/user/' + str(userID) + '/product'
        print(url)
        myobj = {'price': 1200, 'name': 'PC', 'description': 'New PC', 'state': 0}
        x = requests.post(url, data=myobj)

        self.assertEqual(200, x.status_code, "Product doesn't exist.")
        self.assertEqual(x.json(), myobj)

        # DELETE PRODUCT AND USER
        deleteProduct(productID, userID)
        deleteUserFromDB(userID)

        # ATTEMPT TO GET DELETED PRODUCT (EXPECTING A 404)
        url = 'http://127.0.0.1:5000/user/' + str(userID) + '/product'
        myobj = {'price': 1200, 'name': 'PC', 'description': 'New PC', 'state': 0}
        x = requests.post(url, data=myobj)

        self.assertEqual(404, x.status_code, "Product does exist.")
"""

"""
# get a product
url = 'http://127.0.0.1:5000/user/3/product'
myobj = {'price': '299', 'name': 'testing', 'description': 'hola', 'state': 0}
x = requests.post(url, data=myobj)


url = 'http://127.0.0.1:5000/user/1/product/1'
myobj = {'price': '299', 'name': 'testing'}
x = requests.put(url, data=myobj)
import requests
url = 'http://127.0.0.1:5000/user/1/product/2/files'
files = {'file': open('readme.txt','rb')}
values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
r = requests.put(url, files=files, data=values)
import requests
url = 'http://127.0.0.1:5000/user/1/product/1/files'
x = requests.get(url)
print(x.content)


import requests
url = 'http://127.0.0.1:5000/myproducts'
myobj = {'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNjY0OTEzNywiZXhwIjoxNjM2NjQ5NzM3fQ.eyJ1c2VyX2lkIjozfQ.U4fjXix65nT_1xqVKQGVKZoh818kh0Rc1zlUSLMtLnkHOktZ4Rm13YCImedCnZNxS6lTbiI6YSdReBJcCJZ7hQ'}
x = requests.get(url, data=myobj)
x.json()
"""
class TestWhishlist(TestCase):
    # GET TESTING USER
    userID = getAccountByEmail('testingreal@gmail.com')['user_id']
    data1 = {"name": "PC1", "description": "New PC", "price": 1200, "state": 0, "image": "1", "category_id": 2}
    data2 = {"name": "PC2", "description": "Old PC", "price": 600, "state": 2, "image": "10", "category_id": 2}
    data3 = {"name": "PC3", "description": "Average PC", "price": 900, "state": 1, "image": "101", "category_id": 2}

    def test_get_following_products_list(self):
        # Add some products to user whishlist
        p1 = addProduct(self.userID, self.data1)
        p2 = addProduct(self.userID, self.data2)
        p3 = addProduct(self.userID, self.data3)

        followProduct(p1, self.userID)
        followProduct(p2, self.userID)
        followProduct(p3, self.userID)

        # Get product list
        result = getFollowingProductsList(self.userID)
        print(result)

        # Delete products
        deleteProduct(p1, self.userID)
        deleteProduct(p2, self.userID)
        deleteProduct(p3, self.userID)

        self.fail()
'''
    def test_follow_product(self):
        result = followProduct(self.p1, self.userID)
        self.assertEqual(0, result, "selected product doesn't exist")
        #deleteProduct(self.p1, self.userID)

    def test_unfollow_product(self):
        #self.fail()
        result = unfollowProduct(self.p2, self.userID)
        self.assertEqual(0, result, "unfollow product")
        # Check that product isn't being followed anymore
        obj = getFollowingProduct(self.userID, self.p1)
        self.assertFalse(obj)

    def test_get_following_product(self):
        # Follow a product
        result = followProduct(self.p2, self.userID)
        self.assertEqual(0, result, "selected product doesn't exist")

        # Get product
        myobj = getFollowingProduct(self.userID, self.p2)
        self.assertTrue(myobj)

        # Remove product
        unfollowProduct(self.p2, self.userID)
'''


