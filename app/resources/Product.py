import werkzeug
from flask_restful import Resource, reqparse
from lock import lock
from data.ProductQueries import getProductById, setBuyed, addRating, getMean
from utils.security import verify_auth_token


class BuyProduct(Resource):

    def post(self, product_id, token):

        user = verify_auth_token(token)

        if user is None:
            return {'message': 'invalid token'}, 400

        with lock.lock:
            result = setBuyed(user_id=user, product_id=product_id)

            if result == 200:
                return {"message": "Product buy success"}, 200
            elif result == 400:
                return {"message": "You can't buy your own product or product already bought"}, 400
            return {"message": "Error buying product"}, 400


class ProductResource(Resource):

    def get(self, product_id):
        result = getProductById(product_id=product_id)
        if result == 404:
            return {'Message': 'Product not found'}, 404
        else:
            return result, 200


class RateProductResource(Resource):

    def post(self, token, product_id):
        user = verify_auth_token(token)

        if user is None:
            return {'message': 'invalid token'}, 400

        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('rating', type=int)

        data = parser.parse_args()

        with lock.lock:
            result = addRating(buyer_id=user, product_id=product_id, value=data['rating'])

            if result == 404:
                return {'message': 'error adding valoration'}, 500

            return {'message': "Rating added"}, 201


class RatingsProductResource(Resource):

    def get(self, user_id):
        mean_value = getMean(user_id=user_id)

        return {'value': mean_value}, 200
