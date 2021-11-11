import os

from flask import Flask, request, send_from_directory
from flask_restful import Api

from app.resources.Product import *
from app.resources.MyProducts import *
from app.resources.User import *
from app.resources.Category import *
from app.resources.Search import *
from utils.security import secret_key
from flask_cors import CORS
from config import config
from decouple import config as config_decouple

UPLOAD_FOLDER_PRODUCTS = "/imagedata/products"
# UPLOAD_FOLDER_PRODUCTS = "C:/Users/DarkDhz/PycharmProjects/imagedata/products"

app = Flask(__name__)
environment = config['development']
if config_decouple('PRODUCTION', cast=bool, default=False):
    environment = config['production']

app.config.from_object(environment)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SECRET_KEY'] = secret_key
app.config['PRODUCTS_IMAGES'] = UPLOAD_FOLDER_PRODUCTS
api = Api(app)

CORS(app, resources={r'/*': {'origins': '*'}})

# CATEGORY INFO RESOURCES
api.add_resource(CategoryListResource, '/categories', '/categories/', methods=['GET'])
api.add_resource(CategoryResource, '/category/<int:category_id>', methods=['GET'])

# USER INFO RESOURCES
api.add_resource(UserLogin, '/login', '/login/', methods=['POST'])
api.add_resource(UserRegister, '/register', '/register/', methods=['POST'])
api.add_resource(UserAccount, '/userinfo', '/userinfo/')

# PRODUCTS RESOURCES
api.add_resource(ProductResource, '/product/<int:product_id>')

# SEARCH ENGINE RESOURCES
api.add_resource(SearchEngine, '/search', '/search/', methods=['POST'])

# MY PRODUCTS RESOURCES
api.add_resource(MyProductListResource, '/myproducts', '/myproducts/', methods=['GET'])

api.add_resource(UserProductResource, '/user/<int:user_id>/product/<int:product_id>', "/user/<int:user_id>/product")
api.add_resource(UserProductListResource, '/user/<int:user_id>/products', methods=['GET'])

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


def allowed_file(filename, extensions=None):
    if extensions is None:
        extensions = ['jpg', 'png', 'txt']
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensions


@app.route('/')
def mainPage():
    return render_template("index.html")


# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
#@app.route('/user/<int:user_id>/product/<int:product_id>/files', methods=['GET', 'POST', 'PUT'])
def upload_file(user_id, product_id):
    if request.method == 'GET':
        try:
            return send_from_directory(app.config["PRODUCTS_IMAGES"],
                                       filename="user-" + str(user_id) + "-product-" + str(product_id) + ".png",
                                       as_attachment=True), 200
        except FileNotFoundError:
            return {'message': 'file not found'}, 404
    if request.method == 'POST' or request.method == 'PUT':
        # check if the post request has the file part
        if 'file' not in request.files:
            return {'message': 'No selected file'}, 404
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return {'message': 'No selected file'}, 404
        if file and allowed_file(file.filename):
            filename = "user-" + str(user_id) + "-product-" + str(product_id) + ".png"
            file.save(os.path.join(app.config['PRODUCTS_IMAGES'], filename))

            return {'message': 'file saved'}, 201
        return {'message': 'invalid file extension'}, 404
