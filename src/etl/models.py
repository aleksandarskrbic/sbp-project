import pandas as pd


def get_customer_info(row: pd.core.series.Series) -> dict:
    return {
        'zip': row['customer_zip_code_prefix'],
        'city': row['customer_city'],
        'state': row['customer_state']
    }

def get_seller_info(row: pd.core.series.Series) -> dict:
    return {
        'zip': row['seller_zip_code_prefix'],
        'city': row['seller_city'],
        'state': row['seller_state']
    }

def get_product_info(row: pd.core.series.Series) -> dict:
    return {
        'price': row['price'],
        'category': row['product_category_name_english']
    }

def get_order_info(row: pd.core.series.Series) -> dict:
    return {
        'status': row['order_status'],
        'purchase_timestamp': row['order_purchase_timestamp'],
        'delivered_carrier_date': row['order_delivered_carrier_date'],
        'delivered_customer_date': row['order_delivered_customer_date'],
        'payment_type': row['payment_type'],
        'payment_value': row['payment_value'],
        'review_score': row['review_score'],
    }
