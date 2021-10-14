from flask_restful import Resource, reqparse
from data.ProductQueries import getProductByIds


class ProductResource(Resource):

    def get(self, user_id, product_id):
        # define all input parameters need and its type
        result = getProductByIds(user_id=user_id, product_id=product_id)
        if result == 404:
            return {'Message': 'Product or owner not found'}, 404
        else:
            return result, 200

    def post(self, id):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('product_id', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('owner_id', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return {'message': "Not developed yet"}, 404

    def delete(self, user_id, product_id):
        product = getProductByIds(user_id=user_id, product_id=product_id)
        if product is not None:
            product.delete_from_db()
            return {'message': "Product with id [{}] deleted successfully".format(product_id)}, 200
        else:
            return {'message': "Product with id [{}] doest not exist".format(product_id)}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404


class ProductListResource(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404


class UserProductResource(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404


class UserProductListResource(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404
