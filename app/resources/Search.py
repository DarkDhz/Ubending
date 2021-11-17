from flask_restful import Resource, reqparse
from data.SearchQueries import *


class SearchEngine(Resource):

    def get(self):
        return 404

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('category', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('from', type=int, required=False)

        data = parser.parse_args()

        if data['name'] is None and data['category'] is None:
            return {"message": "invalid search format"}, 400

        if data['name'] is None:
            result = searchByCategory(data['category'])

        if data['category'] is None:
            result = searchByName(data['name'])

        result = searchByCategoryAndName(data['category'], data['name'])

    def delete(self, id):
        return 404

    def put(self):
        return 404
