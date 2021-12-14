import mysql.connector as connection

"""
host = "sql11.freesqldatabase.com"
user = "sql11445855"
password = "Xny8nFtYVz"
database = "sql11445855"
"""

# vps
host = "54.36.191.29"
user = "root"
password = "ubending"
database = "Ubending"

"""
# vps
db_host = "54.36.191.29"
db_user = "root"
db_password = "ubending"
database = "Ubending"


"""
# arnau-local
host = "localhost"
user = "root"
password = "1234"
database = "ubending"
"""

db = connection.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=database
)


