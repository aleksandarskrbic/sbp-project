import logging
import pymongo
import pandas as pd
import models


logging.basicConfig(level=logging.INFO)


class ETL():
    def __init__(self, url, db_name) -> None:
        self._init_database(url, db_name)

    def run(self) -> None:
        self._extract()
        self._transform()
        self._load()
    
    def _init_database(self, url, db_name) -> pymongo.database.Database:
        logging.info('Connecting to MongoDB, url: {}, database name: {}'.format(url, db_name))
        self._client = pymongo.MongoClient(url)
        self._db = self._client[db_name]

    def _extract(self) -> None:
        logging.info('Loading csv files to DataFrames...')
        self._customers: pd.DataFrame() = pd.read_csv('../../data/olist_customers_dataset.csv')
        self._orders: pd.DataFrame() = pd.read_csv('../../data/olist_orders_dataset.csv')
        self._order_payments: pd.DataFrame() = pd.read_csv('../../data/olist_order_payments_dataset.csv')
        self._order_reviews: pd.DataFrame() = pd.read_csv('../../data/olist_order_reviews_dataset.csv')
        self._order_items: pd.DataFrame() = pd.read_csv('../../data/olist_order_items_dataset.csv')
        self._products: pd.DataFrame = pd.read_csv('../../data/olist_products_dataset.csv')
        self._product_category_translation: pd.DataFrame = pd.read_csv('../../data/product_category_name_translation.csv')
        self._sellers: pd.DataFrame = pd.read_csv('../../data/olist_sellers_dataset.csv')

    def _transform(self) -> None:
        self._clean_dataframes()
        self._join_tables()
        self._make_collection()

    def _clean_dataframes(self) -> None:
        logging.info('Cleaning DataFrames...')
        self._orders.drop(columns=['order_estimated_delivery_date', 'order_approved_at'], inplace=True)
        self._order_payments.drop(columns=['payment_sequential', 'payment_installments'], inplace=True)
        self._order_reviews = self._order_reviews[['order_id', 'review_score']]
        self._order_items.drop(columns=['shipping_limit_date', 'freight_value'], inplace=True)
        products_cleaned = self._products[['product_id', 'product_category_name']]
        self._products = products_cleaned.merge(self._product_category_translation, how='left', on='product_category_name').drop(columns=['product_category_name'])
 
    def _join_tables(self) -> None:
        logging.info('Merging DataFrames...')
        customer_order: pd.DataFrame = self._customers.merge(self._orders, how='left', on='customer_id')
        customer_order_payment: pd.DataFrame = customer_order.merge(self._order_payments, how='left', on='order_id')
        customer_order_payment_reviews = customer_order_payment.merge(self._order_reviews, how='left', on='order_id')
        customer_order_payment_reviews_items = customer_order_payment_reviews.merge(self._order_items, how='left', on='order_id')
        customer_order_payment_reviews_items_products = customer_order_payment_reviews_items.merge(self._products, how='left', on='product_id')
        self._final_table = customer_order_payment_reviews_items_products.merge(self._sellers, how='left', on='seller_id')

    def _make_collection(self) -> None:
        logging.info('Transforming final DataFrame into Collection...')
        collection = {}
        for _, row in self._final_table.iterrows():
            customer_unique_id = row['customer_unique_id']
            if customer_unique_id not in collection:
                collection[customer_unique_id] = {
                     'customer': models.get_customer_info(row),
                     'orders': [
                         {
                            'order': models.get_order_info(row),
                            'product': models.get_product_info(row),
                            'seller': models.get_seller_info(row)
                         }
                     ]
                }
            else:
                collection[customer_unique_id]['orders'].append(
                    {
                        'order': models.get_order_info(row),
                        'product': models.get_product_info(row),
                        'seller': models.get_seller_info(row)
                    }
                )

        self._collection = [record for record in collection.values()]

    def _load(self) -> None:
        logging.info('Writing to database...')
        self._db['orders'].insert_many(self._collection)