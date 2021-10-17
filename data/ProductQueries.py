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

def addProduct(data):
    mycursor = db.cursor()
    print(data)
    query = "INSERT INTO Products (product_id, owner_id, name, description, price, state, image, category_id) " \
            "VALUES (%s, %s, %s, %s, %f, %i, %s, %i)"
    values = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    mycursor.execute(query, values)
    db.commit()

def deleteProduct(product_id):
    mycursor = db.cursor()
    query = "DELETE FROM Products WHERE product_id = %s"
    mycursor.execute(query)
    db.commit()
