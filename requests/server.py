from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json
import product_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = product_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = product_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)


# run command :

#if installed then run direct 
# python3 server.py
# http://127.0.0.1:5000/getProducts

#in not installed, install first
# pip3 install mysql-connector-python
# pip3 install flask
# python3 server.py
# http://127.0.0.1:5000/getProducts
# http://127.0.0.1:5000/getUOM
# and so on...

# reference link: 
# https://www.youtube.com/watch?v=f9PR1qcwOyg&list=PLeo1K3hjS3uu1hh_qzBt6e379cofVD9Sb&index=3
# initial 6 minutes only :  https://www.youtube.com/watch?v=RsK70V-R2N0&list=PLeo1K3hjS3uu1hh_qzBt6e379cofVD9Sb&index=4


