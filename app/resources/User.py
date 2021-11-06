from flask_restful import Resource, reqparse
from data.UserQueries import checkPasswords, getAccountByEmail, addUserToDB

class UserAccount(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self):

        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('repeat_password', type=float, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        result = getAccountByEmail(data['email'])

        if result != 404:
            return {'Email already  registered.'}

        pwCode = checkPasswords(data['password'], data['repeat_password'])

        if pwCode == 1:
            return {"Passwords do not match."}, 400
        elif pwCode == 2:
            return {"Your password must be at least 8 characters long."}, 400
        elif pwCode == 3:
            return {"Your password must have at least 1 number"}, 400
        elif pwCode == 4:
            return {"Your password must have at least 1 uppercase letter."}, 400

        try:
            addUserToDB(data['user'], data['password'])
        except:
            return {"Error creating user."}, 500

        return {'message': "Account created succesfully"}, 200

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404

class UserLogin(Resource):

    def get(self, id):
        return {'message': "Not developed yet"}, 404

    def post(self, id):
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404