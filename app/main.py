from flask import Flask
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)


@app.route('/')
def mainPage():
    return 'Main page of ubending!'


if __name__ == '__main__':

    app.run()
