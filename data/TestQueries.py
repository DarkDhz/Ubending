from app.database import host, user, password, database
import mysql.connector as connection


def removeRatings(buyer_id):
    db = connection.connect(host=host, user=user, password=password, database=database)
    mycursor = db.cursor()

    query = "DELETE FROM Ratings WHERE buyer_id = %s"
    values = (buyer_id,)
    mycursor.execute(query, values)

    db.commit()
    mycursor.close()
    db.close()
