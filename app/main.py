from flask import Flask
from flask_restful import Api
from resources.Product import ProductResource, UserProductResource, UserProductListResource

# import mysql.connector

app = Flask(__name__)
api = Api(app)




@app.route('/')
def mainPage():
    return 'Main page of ubending!'


api.add_resource(ProductResource, '/product/<int:product_id>')
api.add_resource(UserProductResource, '/user/<int:user_id>/product/<int:product_id>', "/user/<int:user_id>/product")
api.add_resource(UserProductListResource, '/user/<int:user_id>/products')

if __name__ == '__main__':
    app.run(port=5000, debug=True)


