import mysql.connector as connection


host = "sql11.freesqldatabase.com"
user = "sql11445855"
password = "Xny8nFtYVz"
database = "sql11445855"

"""
# db-aux
host = "sql11.freesqldatabase.com"
user = "sql11453270"
password = "iedWsHbbSd"
database = "sql11453270"

"""
"""
# arnau-local
host = "localhost"
user = "root"
password = "1234"
database = "ubending"
"""

db = connection.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


