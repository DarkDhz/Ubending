from flask_restful import Resource, reqparse
from data.UserQueries import checkPasswords, getAccountByEmail, addUserToDB, validateLogin


class UserAccount(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self):

        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('mail', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('repeat_password', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()
        result = getAccountByEmail(data['mail'])

        if result != 404:

            return {'message': 'Email already registered.'}, 400

        pwCode = checkPasswords(data['password'], data['repeat_password'])

        if pwCode == 1:
            return {"Passwords do not match."}, 400
        elif pwCode == 2:
            return {"Your password must be at least 8 characters long."}, 400
        elif pwCode == 3:
            return {"Your password must have at least 1 number"}, 400
        elif pwCode == 4:
            return {"Your password must have at least 1 uppercase letter."}, 400
        addUserToDB(data['username'], data['mail'], data['password'])

        return {'message': "Account created succesfully"}, 200

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
        parser.add_argument('mail', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        result = validateLogin(mail=data['mail'], password=data['password'])

        if result == 404:
            return {'message': 'user not found'}, 404
        if result == 400:
            return {'message': 'invalid password'}, 400
        return {'token': result.decode('ascii')}, 200


    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404
