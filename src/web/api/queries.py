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