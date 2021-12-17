from app.database import db_host, db_user, db_password, database
import mysql.connector as connection


def removeRatings(buyer_id):
    db = connection.connect(host=db_host, user=db_user, password=db_password, database=database)
    mycursor = db.cursor()

    query = "DELETE FROM Ratings WHERE buyer_id = %s"
    values = (buyer_id,)
    mycursor.execute(query, values)

    db.commit()
    mycursor.close()
    db.close()
