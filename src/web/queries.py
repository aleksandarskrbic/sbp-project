from datetime import datetime

class Orders:
    orders_by_state = [
        {'$group': {'_id': '$customer.state', 'count': {'$sum':1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]

    orders_by_city = [
        {'$group': {'_id': '$customer.city', 'count': {'$sum':1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]

    order_max = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$_id', 'max': {'$max': '$orders.order.payment_value'}}},
        {'$sort': {'max': -1}},
        {'$limit': 1}
    ]

    order_min = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$_id', 'min': {'$min': '$orders.order.payment_value'}}},
        {'$sort': {'max': 1}},
        {'$limit': 1}
    ]

    orders_by_status = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.order.status', 'count': {'$sum': 1}}},
    ]

    order_reviews = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.order.review_score', 'count': {'$sum': 1}}},
        {'$sort': {'_id': 1}}
    ]

    order_counts_by_month = [
        {'$unwind': '$orders'},
        {'$group': {'_id': {'$month': '$orders.order.purchase_timestamp'}, 'count': {'$sum':1}}},
        {'$sort': {'_id': 1}}
    ]

    order_avg_spent_by_month = [
        {'$unwind': '$orders'},
        {'$group': {'_id': {'$month': '$orders.order.purchase_timestamp'}, 'avg': {'$avg': '$orders.order.payment_value'}}},
        {'$sort': {'_id': 1}}
    ]


class Payments:
    payments_by_state = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$customer.state', 'avg': {'$avg': '$orders.order.payment_value'}}},
        {'$sort': {'avg': -1}},
        {'$limit': 10}
    ]

    payments_by_city = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$customer.city', 'avg': {'$avg': '$orders.order.payment_value'}}},
        {'$sort': {'avg': -1}},
        {'$limit': 10}
    ]

    most_popular_payment_method = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.order.payment_type', 'count': {'$sum':1}}},
        {'$sort': {'count': -1}},
        {'$limit': 4}
    ]

    avg_spent_by_payment_method = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.order.payment_type', 'avg': {'$avg': '$orders.order.payment_value'}}},
        {'$sort': {'avg': -1}},
        {'$limit': 4}
    ]


class Products:
    most_popular_product_categories = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.product.category', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 5}
    ]


class Delivery:
    purchase_to_customer_avg_days = [
        {'$unwind': '$orders'},
        {'$match': {
            '$and': [
                {'orders.order.delivered_customer_date': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}},
                {'orders.order.delivered_carrier_date': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}},
                {'orders.order.purchase_timestamp': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}}
            ]
        }
        },
        {'$addFields': {
            'curier_customer': 
            {
                '$ceil':
                    {'$divide': [
                        {'$subtract': ['$orders.order.delivered_customer_date', '$orders.order.purchase_timestamp']}, 86400000]
                    }             
            }
        }},
        {'$group': {'_id': {'$month' : '$orders.order.purchase_timestamp'}, 'avg': {'$avg': '$curier_customer'}}},
        {'$sort': {'avg': -1}}
    ]

    purchase_to_deliverer_avg_days = [
        {'$unwind': '$orders'},
        {'$match': {
            '$and': [
                {'orders.order.delivered_customer_date': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}},
                {'orders.order.delivered_carrier_date': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}},
                {'orders.order.purchase_timestamp': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}}
            ]
        }
        },
        {'$addFields': {
            'curier_customer': 
            {
                '$ceil':
                    {'$divide': [
                        {'$subtract': ['$orders.order.delivered_carrier_date', '$orders.order.purchase_timestamp']}, 86400000]
                    }             
            }
        }},
        {'$group': {'_id': {'$month' : '$orders.order.purchase_timestamp'}, 'avg': {'$avg': '$curier_customer'}}},
        {'$sort': {'avg': -1}}
    ]

    deliverer_to_customer_avg_days = [
        {'$unwind': '$orders'},
        {'$match': {
            '$and': [
                {'orders.order.delivered_customer_date': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}},
                {'orders.order.delivered_carrier_date': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}},
                {'orders.order.purchase_timestamp': {'$gt': datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')}}
            ]
        }
        },
        {'$addFields': {
            'curier_customer': 
            {
                '$ceil':
                    {'$divide': [
                        {'$subtract': ['$orders.order.delivered_customer_date', '$orders.order.delivered_carrier_date']}, 86400000]
                    }             
            }
        }},
        {'$group': {'_id': {'$month' : '$orders.order.purchase_timestamp'}, 'avg': {'$avg': '$curier_customer'}}},
        {'$sort': {'avg': -1}}
    ]
