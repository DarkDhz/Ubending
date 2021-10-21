import werkzeug
from flask_restful import Resource, reqparse
from data.ProductQueries import getProductByIds, getProductById, getAllProductsOfUserByID, updateProduct, deleteProduct, addProduct


class ProductResource(Resource):

    def get(self, product_id):
        result = getProductById(product_id=product_id)
        if result == 404:
            return {'Message': 'Product not found'}, 404
        else:
            return result, 200

    def post(self, product_id, user_id):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('product_id', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('owner_id', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
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
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        parser.add_argument('category', type=int)

        data = parser.parse_args()

        updateProduct(owner_id=user_id, product_id=product_id, data=data)
        # https://www.py4u.net/discuss/140647

        return 200


class UserProductListResource(Resource):

    def get(self, user_id):
        result = getAllProductsOfUserByID(user_id=user_id)
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
