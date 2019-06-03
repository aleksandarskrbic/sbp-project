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

    order_reviews = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.order.review_score', 'count': {'$sum': 1}}}
    ]

    orders_by_status = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.order.status', 'count': {'$sum': 1}}},
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

    payment_methods_info = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.order.payment_type', 'count': {'$sum':1}}}
    ]


class Products:
    most_popular_product_categories = [
        {'$unwind': '$orders'},
        {'$group': {'_id': '$orders.product.category', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]


class Delivery:
    delivery_prices = [
        {'$unwind': '$orders'},
        {'$project': {'orders.order.payment_value': 1, 'orders.product.price': 1}},
        {'$addFields': {
            'delivery_price': {'$subtract': ['$orders.order.payment_value', '$orders.product.price']}
            }
        }
    ]

    purchase_curier_days = [
        {'$unwind': '$orders'},
        {'$project': {'orders.order.purchase_timestamp': 1, 'orders.order.delivered_carrier_date': 1}},
        {'$addFields': {
            'purchase_curier': 
            {
                '$ceil':
                    {'$divide': [
                        {'$subtract': ['$orders.order.delivered_carrier_date', '$orders.order.purchase_timestamp']}, 86400000]
                }             
            }
        }}
    ]

    curier_customer_days = [
        {'$unwind': '$orders'},
        {'$project': {'orders.order.delivered_customer_date': 1, 'orders.order.delivered_carrier_date': 1}},
        {'$addFields': {
            'curier_customer': 
            {
                '$ceil':
                    {'$divide': [
                        {'$subtract': ['$orders.order.delivered_customer_date', '$orders.order.delivered_carrier_date']}, 86400000]
                    }             
            }
        }}
    ]


#payment_value - payment_type
#orders by days
#orders by months