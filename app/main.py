from flask import Flask
from flask_restful import Resource, Api

from resources.Product import ProductResource

# import mysql.connector

app = Flask(__name__)
api = Api(app)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)


@app.route('/')
def mainPage():
    return 'Main page of ubending!'


api.add_resource(ProductResource, '/product/<int:id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
