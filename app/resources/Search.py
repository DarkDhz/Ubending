from flask_restful import Resource, reqparse
from data.SearchQueries import *


class SearchEngine(Resource):

    def get(self):
        return 404

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=False, help="This field cannot be left blank")
        # category must be the id
        parser.add_argument('category', type=int, required=False, help="This field cannot be left blank")
        parser.add_argument('from', type=int, required=False)

        data = parser.parse_args()

        start_point = 0

        if data['from'] is not None:
            start_point = data['from']

        if data['name'] is None and data['category'] is None:
            return {"message": "invalid search format"}, 400

        if data['name'] is None:
            result = searchByCategory(category_id=data['category'], start_point=start_point)
            if result == 404:
                return {"message": "No products found"}, 400
            return result, 200

        if data['category'] is None:
            result = searchByName(name=data['name'], start_point=start_point)
            if result == 404:
                return {"message": "No products found"}, 400
            return result, 200

        result = searchByCategoryAndName(category_id=data['category'], name=data['name'], start_point=start_point)
        if result == 404:
            return {"message": "No products found"}, 400
        return result, 200

    def delete(self, id):
        return 404

    def put(self):
        return 404
