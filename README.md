# OLIST DATA ANALYSYS
Project for Database Systems Course
### How to run

1. Set up python3 environment like virtual environment or miniconda [preferred]
 or just install python3 with pip
 Windows: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation
 Linux: https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/
 
2. Clone repository and then move to sbp-project/src

3. Install requred python packages
```bash
pip install -r requirements.txt
```

4. Download data from https://www.kaggle.com/olistbr/brazilian-ecommerce#olist_order_payments_dataset.csv
and extract it into sbt-projet/data folder. Of course you need MongoDB running locally on
you machine.

5. Run ETL job to move data from files to MongoDB
```bash
pyton /etl/app.py
```

6. To start webapp with dashboard run:
```bash
pyton /web/app.py
```
  and go to http://127.0.0.1:5000/
