from app.database import db



def getProductByIds(user_id, product_id):
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    result = myresult[0]
    return {'product_id': result[0], 'owner_id': result[1], 'name': result[2],
            'description': result[3], 'price': result[4], 'state': result[5],
            'image': result[6], 'category_id': result[7]}



