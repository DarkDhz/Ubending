from flask_restful import Resource, reqparse
from data.ProductQueries import getProductByIds, deleteProduct, addProduct


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
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('image', type=str)
        parser.add_argument('category_id', type=int)

        data = parser.parse_args()
        # We cannot have a negative price.
        if data['price'] < 0:
            return {'message': "Price attribute cannot be negative."}, 409
        addProduct(data)
        return {'message': "Product added successfully"}, 200

    def delete(self, user_id, product_id):
        product = getProductByIds(user_id=user_id, product_id=product_id)
        if product is not None:
            deleteProduct(product_id)
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
