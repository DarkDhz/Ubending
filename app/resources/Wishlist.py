from flask_restful import Resource, reqparse
from utils.security import verify_auth_token
from data.ProductQueries import getFollowingProducts


class WishlistResource(Resource):

    def get(self, token):
        user = verify_auth_token(token)
        if user is None:
            return {'message': 'invalid token'}, 400

        result = getFollowingProducts(user_id=user)

        if result == 404:
            return {'Message': 'owner currently has no products on its wishlist'}, 404
        else:
            return result, 200

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404