import werkzeug
from flask_restful import Resource, reqparse

import lock
from data.ProductQueries import getProductById


class ProductResource(Resource):

    def get(self, product_id):
        result = getProductById(product_id=product_id)
        if result == 404:
            return {'Message': 'Product not found'}, 404
        else:
            return result, 200

    def post(self, product_id, user_id):
        return {'message': "Not developed yet"}, 404

    def delete(self, user_id, product_id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        with lock.lock:
            return {'message': "Not developed yet"}, 404


class ProductListResource(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self, id):
        with lock.lock:
            return {'message': "Not developed yet"}, 404

    def delete(self, id):
        with lock.lock:
            return {'message': "Not developed yet"}, 404

    def put(self, id):
        with lock.lock:
            return {'message': "Not developed yet"}, 404
