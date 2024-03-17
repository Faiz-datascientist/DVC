import os 
# import current directory 
import sys 
from src.exception import CustomException
from src.loggers import logging
import pandas as pd 
import numpy as np
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_data_sql():
    logging.info("reading sql database started: ")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established reading sql data ")
        df=pd.read_sql("select * from students",mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e,sys)
    

if __name__=="__main__":
    app_data = read_data_sql()
