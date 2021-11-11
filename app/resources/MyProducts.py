from flask_restful import Resource, reqparse
from data.ProductQueries import *
from utils.security import verify_auth_token

# NO AUTHENTICATHED

class UserProductResource(Resource):

    def get(self, user_id, product_id):
        result = getProductByIds(user_id=user_id, product_id=product_id)
        if result == 404:
            return {'Message': 'Product or owner not found'}, 404
        else:
            return result, 200

    def post(self, user_id):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('image', type=int)
        parser.add_argument('category_id', type=int)

        data = parser.parse_args()
        # We cannot have a negative price.
        if data['price'] < 0:
            return {'message': "Price attribute cannot be negative."}, 409
        addProduct(user_id, data)
        return {'message': "Product added successfully"}, 200

    def delete(self, user_id, product_id):
        product = getProductByIds(user_id=user_id, product_id=product_id)
        if product is not None:
            deleteProduct(product_id, user_id)
            return {'message': "Product with id [{}] deleted successfully".format(product_id)}, 200
        else:
            return {'message': "Product with id [{}] doest not exist".format(product_id)}, 404

    def put(self, user_id, product_id):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('name', type=str, help="This field cannot be left blank")
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=int)
        parser.add_argument('state', type=int)
        parser.add_argument('category', type=int)

        data = parser.parse_args()

        updateProduct(owner_id=user_id, product_id=product_id, data=data)
        return 201


class UserProductListResource(Resource):

    def get(self, user_id):
        result = getAllProductsOfUserByID(user_id=user_id)
        if result == 404:
            return {'Message': 'owner has no products or do not exist'}, 404
        else:
            return result, 200

    def post(self, id):
        return 404

    def delete(self, id):
        return 404

    def put(self):
        return 404

# AUTHENTICATED

class MyProductResource(Resource):

    def get(self, product_id):

        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('token', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        user = verify_auth_token(data['token'])

        if user is None:
            return {'message': 'invalid token'}, 400

        result = getProductByIds(user_id=user, product_id=product_id)
        if result == 404:
            return {'Message': 'Product or owner not found'}, 404
        else:
            return result, 200

    def post(self):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('token', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('category_id', type=int)

        data = parser.parse_args()

        user = verify_auth_token(data['token'])

        if user is None:
            return {'message': 'invalid token'}, 400

        # We cannot have a negative price.
        if data['price'] < 0:
            return {'message': "Price attribute cannot be negative."}, 409
        addProduct(user, data)
        return {'message': "Product added successfully"}, 200

    def delete(self, product_id):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('token', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        user = verify_auth_token(data['token'])

        if user is None:
            return {'message': 'invalid token'}, 400

        product = getProductByIds(user_id=user, product_id=product_id)
        if product is not None:
            deleteProduct(product_id, user)
            return {'message': "Product with id [{}] deleted successfully".format(product_id)}, 200
        else:
            return {'message': "Product with id [{}] doest not exist".format(product_id)}, 404

    def put(self, product_id):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('token', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=int)
        parser.add_argument('state', type=int)
        parser.add_argument('category', type=int)

        data = parser.parse_args()

        user = verify_auth_token(data['token'])

        if user is None:
            return {'message': 'invalid token'}, 400

        updateProduct(owner_id=user, product_id=product_id, data=data)
        return 201


class MyProductListResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('token', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        user = verify_auth_token(data['token'])

        if user is None:
            return {'message': 'invalid token'}, 400

        result = getAllProductsOfUserByID(user_id=user)

        if result == 404:
            return {'Message': 'owner has no products or do not exist'}, 404
        else:
            return result, 200

    def post(self, id):
        return 404

    def delete(self, id):
        return 404

    def put(self):
        return 404