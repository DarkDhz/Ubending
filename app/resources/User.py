from flask_restful import Resource, reqparse
from data.UserQueries import getAccountByUsername, verifyPassword, generate_auth_token


class UserAccount(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404

class UserLogin(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and their type
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()
        result = getAccountByUsername(data['username'])
        if result == 404:
            return {'Message': 'Username does not exist'}, 404
        if not verifyPassword(data["password"]):
            return {"message": "Invalid password."}, 400

        token = generate_auth_token()
        return {'token': token.decode('ascii')}, 200

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404