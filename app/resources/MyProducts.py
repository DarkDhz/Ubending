from flask_restful import Resource, reqparse
from data.ProductQueries import *
from utils.security import verify_auth_token


# AUTHENTICATED
class MyProductResource(Resource):

    def get(self, product_id, token):

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

    def post(self, token):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('image', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('category_id', type=int)

        data = parser.parse_args()
        user = verify_auth_token(token)

        if user is None:
            return {'message': 'invalid token'}, 400

        # We cannot have a negative price.
        if data['price'] < 0:
            return {'message': "Price attribute cannot be negative."}, 409
        return {'product_id': addProduct(user, data)}, 200


    def delete(self, product_id, token):
        user = verify_auth_token(token)

        if user is None:
            return {'message': 'invalid token'}, 400

        product = getProductByIds(user_id=user, product_id=product_id)
        if product is not None:
            deleteProduct(product_id, user)
            return {'message': "Product with id [{}] deleted successfully".format(product_id)}, 200
        else:
            return {'message': "Product with id [{}] doest not exist".format(product_id)}, 404

    def put(self, product_id, token):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('token', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=int)
        parser.add_argument('state', type=int)
        parser.add_argument('category_id', type=int)

        data = parser.parse_args()

        user = verify_auth_token(data['token'])

        if user is None:
            return {'message': 'invalid token'}, 400

        updateProduct(owner_id=user, product_id=product_id, data=data)
        return 201


class MyProductListResource(Resource):

    def get(self, token):
        user = verify_auth_token(token)
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
