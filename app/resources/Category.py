from flask_restful import Resource
from data.CategoryQueries import getAllCategories, getCategoryByID


class CategoryListResource(Resource):

    def get(self):
        result = getAllCategories()
        if result == 404:
            return {'Message': 'Error'}, 404
        else:
            return result, 200

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, user_id, product_id):

        return {'message': "Not developed yet"}, 404


# TODO
class CategoryResource(Resource):

    def get(self, category_id):
        result = getCategoryByID(category_id)
        if result == 404:
            return {'Message': 'owner has no products or do not exist'}, 404
        else:
            return result, 200


    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, user_id, product_id):
        return {'message': "Not developed yet"}, 404
