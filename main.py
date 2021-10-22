from flask import Flask, render_template
from flask_restful import Api
from app.resources.Product import ProductResource, UserProductResource, UserProductListResource
from app.resources.User import UserAccount, UserLogin
from flask import session
from utils.security import secret_key
from flask_cors import CORS
from config import config
from decouple import config as config_decouple
from app.resources.Category import CategoryListResource

# https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions

app = Flask(__name__)
environment = config['development']
if config_decouple('PRODUCTION', cast=bool, default=False):
    environment = config['production']

app.config.from_object(environment)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SECRET_KEY'] = secret_key
api = Api(app)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def mainPage():
    return render_template("index.html")


api.add_resource(CategoryListResource, '/categories', methods=['GET'])
api.add_resource(UserLogin, '/login', methods=['POST'])
api.add_resource(UserAccount, '/user/<int:user_id>')
api.add_resource(ProductResource, '/product/<int:product_id>')
api.add_resource(UserProductResource, '/user/<int:user_id>/product/<int:product_id>', "/user/<int:user_id>/product")
api.add_resource(UserProductListResource, '/user/<int:user_id>/products', methods=['GET'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
