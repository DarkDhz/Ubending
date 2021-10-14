from flask import Flask
from flask_restful import Api
from resources.Product import ProductResource

# import mysql.connector

app = Flask(__name__)
api = Api(app)




@app.route('/')
def mainPage():
    return 'Main page of ubending!'


api.add_resource(ProductResource, '/user/<int:user_id>/product/<int:product_id>', "/user/<int:user_id>/product")

if __name__ == '__main__':
    app.run(port=5000, debug=True)


