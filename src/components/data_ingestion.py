
#Mysql to train test split data 
import os 
# import current directory 
import sys 
from src.exception import CustomException
from src.loggers import logging
import pandas as pd 
import numpy as np
from src.utils import read_data_sql
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def Initiate_DataIngestion(self):

        try:
        #we are reading the data here
            df=read_data_sql()

            logging.info("reading the mysql data")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=51)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("data importing completed!!")

            return(
                self.ingestion_config.test_data_path,
                self.ingestion_config.train_data_path
            )
            

        except Exception as e:
            raise CustomException(e,sys)
        

