from flask import Flask
from flask_restful import Api
from resources.Product import ProductResource, UserProductResource, UserProductListResource
from resources.User import UserAccount, UserLogin
from flask import session
from utils.security import secret_key

# https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
api = Api(app)


@app.route('/')
def mainPage():
    return 'Main page of ubending!'


api.add_resource(UserLogin, '/login', methods=['POST'])
api.add_resource(UserAccount, '/user/<int:user_id>')
api.add_resource(ProductResource, '/product/<int:product_id>')
api.add_resource(UserProductResource, '/user/<int:user_id>/product/<int:product_id>', "/user/<int:user_id>/product")
api.add_resource(UserProductListResource, '/user/<int:user_id>/products', methods=['GET'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
