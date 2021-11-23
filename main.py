import os

from flask import Flask, request, send_from_directory, render_template
from flask_restful import Api
from app.database import host, user, password, database
from app.resources.Product import *
from app.resources.MyProducts import *
from app.resources.User import *
from app.resources.Category import *
from app.resources.Search import *
from utils.security import secret_key, email_user, email_pass
from flask_cors import CORS
from config import config
from decouple import config as config_decouple
from flask_mail import Mail

app = Flask(__name__)
environment = config['development']
if config_decouple('PRODUCTION', cast=bool, default=False):
    environment = config['production']

app.config.from_object(environment)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SECRET_KEY'] = secret_key
app.config['PRODUCTS_IMAGES'] = UPLOAD_FOLDER_PRODUCTS
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = email_user
app.config['MAIL_PASSWORD'] = email_pass
api = Api(app)
mail_svr = Mail(app)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/reset")
@app.route("/recover")
@app.route("/home")
@app.route("/user-products")
@app.route("/login-signup")
@app.route('/')
def mainPage():
    return render_template("index.html")


# CATEGORY INFO RESOURCES
api.add_resource(CategoryListResource, '/categories', '/categories/', methods=['GET'])
api.add_resource(CategoryResource, '/category/<int:category_id>', methods=['GET'])

# SEARCH ENGINE RESOURCES

api.add_resource(SearchEngine, '/api/search', '/api/search', methods=['POST'])

# USER INFO RESOURCES
api.add_resource(UserLogin, '/login', '/login/', methods=['POST'])
api.add_resource(UserRegister, '/register', '/register/', methods=['POST'])
api.add_resource(ResetRequest, '/reset_password', '/reset_password/', methods=['POST'])
api.add_resource(ResetPassword, '/reset_password/<token>', '/reset_password/<token>/', methods=['POST'])
api.add_resource(UserAccount, '/api/userinfo/<string:token>')

# PRODUCTS RESOURCES
api.add_resource(ProductResource, '/product/<int:product_id>')

# MY PRODUCTS RESOURCES
api.add_resource(MyProductResource, '/myproduct/<int:product_id>/<string:token>', '/myproduct/<string:token>')
api.add_resource(MyProductListResource, '/myproducts/<string:token>', methods=['GET'])


if __name__ == '__main__':
    '''
    import os

    directory = os.path.dirname(app.config['PRODUCTS_IMAGES'] + "/test.txt")

    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    '''
    app.run(port=5000, debug=True)

