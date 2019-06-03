import json
import pymongo
from bson.code import Code
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from queries import Orders, Payments, Products, Delivery


app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['sbp']
collection = db['orders']


@app.route('/order/state', methods=['GET'])
def orders_by_state():
    result = list(collection.aggregate(Orders.orders_by_state))
    return jsonify(result)


@app.route('/order/city', methods=['GET'])
def orders_by_city():
    result = list(collection.aggregate(Orders.orders_by_city))
    return jsonify(result)


@app.route('/order/min-max', methods=['GET'])
def min_max_order():
    min_order = list(collection.aggregate(Orders.order_min))
    max_order = list(collection.aggregate(Orders.order_max))
    print(min_order)
    print(max_order)

    result = {
        'min': min_order[0]['min'],
        'max': max_order[0]['max']
    }
    return jsonify(result)


@app.route('/order/status', methods=['GET'])
def orders_by_status():
    result = list(collection.aggregate(Orders.orders_by_status))
    return jsonify(result)


@app.route('/order/reviews', methods=['GET'])
def order_reviews():
    result = list(collection.aggregate(Orders.order_reviews))
    return jsonify(result)


@app.route('/order/months-count', methods=['GET'])
def orders_by_months():
    result = list(collection.aggregate(Orders.order_counts_by_month))
    return jsonify(result)
    

@app.route('/order/months-avg', methods=['GET'])
def orders_avg_by_months():
    result = list(collection.aggregate(Orders.order_avg_spent_by_month))
    return jsonify(result)


@app.route('/payment/state', methods=['GET'])
def payments_by_state():
    result = list(collection.aggregate(Payments.payments_by_state))
    return jsonify(result)


@app.route('/payment/city', methods=['GET'])
def payments_by_city():
    result = list(collection.aggregate(Payments.payments_by_city))
    return jsonify(result)


@app.route('/payment/methods', methods=['GET'])
def payment_methods_info():
    result = list(collection.aggregate(Payments.most_popular_payment_method))
    return jsonify(result)


@app.route('/payment/methods-avg', methods=['GET'])
def avg_spent_by_payment_method():
    result = list(collection.aggregate(Payments.avg_spent_by_payment_method))
    return jsonify(result)


@app.route('/product/categories', methods=['GET'])
def most_popular_product_categories():
    result = list(collection.aggregate(Products.most_popular_product_categories))
    return jsonify(result)


@app.route('/delivery/purchase-customer', methods=['GET'])
def purchase_to_customer_avg_days():
    result = list(collection.aggregate(Delivery.purchase_to_customer_avg_days))
    return jsonify(result)


@app.route('/delivery/purchase-deliverer', methods=['GET'])
def purchase_to_deliverer_avg_days():
    result = list(collection.aggregate(Delivery.purchase_to_deliverer_avg_days))
    return jsonify(result)


@app.route('/delivery/deliverer-customer', methods=['GET'])
def deliverer_to_customer_avg_days():
    result = list(collection.aggregate(Delivery.deliverer_to_customer_avg_days))
    return jsonify(result)



"""
@app.route('/')
def index():
    return render_template('index.html')
"""

if __name__ == '__main__':
    app.run()
