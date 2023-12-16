from appfolder import app,mysql
from flask import render_template

@app.route('/')
def homepage():
    return render_template('index.html')


# route for product
@app.route('/product')
def product():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product")
    product_data = cursor.fetchall()
    print(product_data)
    cursor.close()
    return render_template ('product.html', products = product_data)
    

# route for orders
@app.route('/order')
def order():
    return render_template('order.html')


    




