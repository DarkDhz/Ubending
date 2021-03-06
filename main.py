from flask import Flask, render_template
from flask_restful import Api
from app.resources.Product import *
from app.resources.MyProducts import *
from app.resources.User import *
from app.resources.Category import *
from app.resources.Search import *
from app.resources.Wishlist import *
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

app.config['MAIL_SERVER'] = 'ssl0.ovh.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ubending@darkhorizon.es'
app.config['MAIL_PASSWORD'] = 'ubending2021'
api = Api(app)
mail_svr = Mail(app)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/user-profile")
@app.route("/reset")
@app.route("/reviews")
@app.route("/recover")
@app.route("/home")
@app.route("/user-products")
@app.route("/login-signup")
@app.route("/products")
@app.route("/wishlist")
@app.route('/')
def mainPage():
    return render_template('index.html', static_url_path='', static_folder='dist', template_folder='dist')


# CATEGORY INFO RESOURCES
api.add_resource(CategoryListResource, '/categories', '/categories/', methods=['GET'])
api.add_resource(CategoryResource, '/category/<int:category_id>', methods=['GET'])

# SEARCH ENGINE RESOURCES

api.add_resource(SearchEngine, '/api/search/<string:token>', methods=['POST'])

# USER INFO RESOURCES
api.add_resource(UserLogin, '/login', '/login/', methods=['POST'])
api.add_resource(UserRegister, '/register', '/register/', methods=['POST'])
api.add_resource(ResetRequest, '/api/reset_password', '/api/reset_password/', methods=['POST'])
api.add_resource(ResetPassword, '/api/reset_password/<string:token>', methods=['POST'])
api.add_resource(UserAccount, '/api/userinfo/<string:token>', '/api/useradmin/<int:user_id>')

# PRODUCTS RESOURCES
api.add_resource(ProductResource, '/product/<int:product_id>')

# MY PRODUCTS RESOURCES
api.add_resource(MyProductResource, '/myproduct/<int:product_id>/<string:token>', '/myproduct/<string:token>')
api.add_resource(MyProductListResource, '/myproducts/<string:token>', methods=['GET'])


# WISHLIST RESOURCES
api.add_resource(WishlistResource, '/api/wishlist/<string:token>', '/api/wishlist/<string:token>/<int:product_id>')

# BUY PRODUCT RESOURCE
api.add_resource(BuyProduct, '/api/buy/<int:product_id>/<string:token>', methods=['POST'])

# RATE ENDPOINT
api.add_resource(RatingsProductResource, '/api/ratings/<int:user_id>', methods=['GET'])
api.add_resource(ToRateProductListResource, '/api/to_rate/<string:token>', methods=['GET'])
api.add_resource(RatedProductListResource, '/api/rated/<string:token>', methods=['GET'])
api.add_resource(RateProductResource, '/api/rate/<int:product_id>/<string:token>', methods=['POST'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
