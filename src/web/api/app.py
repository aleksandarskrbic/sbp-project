import json
import pymongo
from bson.code import Code
from flask import Flask, request, jsonify, render_template
from queries import Orders, Payments


app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['sbp']
collection = db['orders']


@app.route('/orders-state', methods=['GET'])
def orders_by_state():
    customers_by_state = list(collection.aggregate(Orders.orders_by_state))
    return jsonify(customers_by_state)


@app.route('/orders-city', methods=['GET'])
def orders_by_city():
    customers_by_city = list(collection.aggregate(Orders.orders_by_city))
    return jsonify(customers_by_city)


@app.route('/payments-state', methods=['GET'])
def payments_by_state():
    payments_by_city = list(collection.aggregate(Payments.payments_by_state))
    return jsonify(payments_by_city)


@app.route('/payments-city', methods=['GET'])
def payments_by_city():
    payments_by_city = list(collection.aggregate(Payments.payments_by_city))
    return jsonify(payments_by_city)


@app.route('/payments-methods', methods=['GET'])
def payment_methods_info():
    payments_by_city = list(collection.aggregate(Payments.payment_methods_info))
    return jsonify(payments_by_city)


if __name__ == '__main__':
    app.run()
