from flask_restful import Resource, reqparse
from utils.security import verify_auth_token
from data.ProductQueries import getFollowingProductsList, unfollowProduct, getFollowingProduct


class WishlistResource(Resource):

    def get(self, token):
        user = verify_auth_token(token)
        if user is None:
            return {'message': 'invalid token'}, 400

        result = getFollowingProductsList(user_id=user)

        if result == 404:
            return {'Message': 'owner currently has no products on its wishlist'}, 404
        else:
            return result, 200

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, product_id, token):
        user = verify_auth_token(token)

        if user is None:
            return {'message': 'invalid token'}, 400

        isBeingFollowed = getFollowingProduct(user_id=user, product_id=product_id)
        if isBeingFollowed:
            unfollowProduct(product_id, user)
            return {'message': "Product with id [{}] removed from wishlist".format(product_id)}, 200
        else:
            return {'message': "Product with id [{}] doest not exist".format(product_id)}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404