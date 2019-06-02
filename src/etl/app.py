from etl import ETL


if __name__ == '__main__':
    etl = ETL(url='mongodb://localhost:27017/', db_name='sbp')
    etl.run()