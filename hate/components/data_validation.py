import os, sys, json
import pandas as pd
from pandas import DataFrame
from hate.exception import CustomException
from hate.logger import logging
from hate.entity.config_entity import DataValidationConfig
from hate.entity.artifact_entity import DataIngestionArtifacts, DataValidationArtifacts
from hate.constants import SCHEMA_FILE_PATH
from hate.utils.main_utils import  read_yaml_file, write_yaml_file

class DataValidation:
    def __init__(self, data_ingestion_artifacts: DataIngestionArtifacts, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.data_validation_config = data_validation_config
            self._schema_config =read_yaml_file(file_path=SCHEMA_FILE_PATH)

        except Exception as e:
            raise CustomException(e, sys) from e
        
    def validate_number_of_columns_imb(self, dataframe: DataFrame) -> bool:
   
        try:
            status = len(dataframe.columns) == len(self._schema_config["imbalance_data"])
            logging.info(f"Is required column present in imbalance_data: [{status}]")
            return status
        except Exception as e:
            raise CustomException(e, sys)
        
    def validate_number_of_columns_raw(self, dataframe: DataFrame) -> bool:
   
        try: 
            status1 = len(dataframe.columns) == len(self._schema_config["raw_data"])
            logging.info(f"Is required column present in raw_data: [{status1}]")
            return status1
        except Exception as e:
            raise CustomException(e, sys)
     

    def is_column_exist_imb(self, df: DataFrame) -> bool:
    
        try:
            dataframe_columns = df.columns
            missing_columns = []
            for column in self._schema_config["imbalance_data"]:
                if column not in dataframe_columns:
                    missing_columns.append(column)

            if len(missing_columns)>0:
                logging.info(f"Missing column in Imbalance dataset: {missing_columns}")

            return False if len(missing_columns)>0  else True
        except Exception as e:
            raise CustomException(e, sys) from e
    
    def is_column_exist_raw(self, df: DataFrame) -> bool:
    
        try:
            dataframe_columns = df.columns
            missing_columns1 = []
            for column in self._schema_config["raw_data"]:
                if column not in dataframe_columns:
                    missing_columns1.append(column)

            if len(missing_columns1)>0:
                logging.info(f"Missing column in raw dataset: {missing_columns1}")
            

            
            return False if len(missing_columns1)>0  else True
        except Exception as e:
            raise CustomException(e, sys) from e
    
        
    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e, sys)
        
    
    def initiate_data_validation(self) -> DataValidationArtifacts:
       
        # os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)

        try:
            validation_error_msg = ""
            logging.info("Starting data validation")
            imb_df = DataValidation.read_data(file_path=self.data_ingestion_artifacts.imbalance_data_file_path)
            raw_df =  DataValidation.read_data(file_path=self.data_ingestion_artifacts.raw_data_file_path)

            status = self.validate_number_of_columns_imb(dataframe=imb_df)
            logging.info(f"All required columns present in IMBALANCE dataframe: {status}")
            if not status:
                validation_error_msg += f"Columns are missing in IMBALANCE dataframe."
            
            status1 = self.validate_number_of_columns_raw(dataframe=raw_df)

            logging.info(f"All required columns present in RAW dataframe: {status1}")
            if not status1:
                validation_error_msg += f"Columns are missing in RAW dataframe."

            status = self.is_column_exist_imb(df=imb_df)

            if not status:
                validation_error_msg += f"Columns are missing in IMBALANCE dataframe."
            status1 = self.is_column_exist_raw(df=raw_df)

            if not status1:
                validation_error_msg += f"columns are missing in RAW dataframe."

            validation_status = len(validation_error_msg) == 0


            data_validation_artifacts = DataValidationArtifacts(
                validation_status=validation_status,
                message=validation_error_msg,
                report_file_path=self.data_validation_config.report_file_path
            )
            print(data_validation_artifacts)
            content = f"Validation Status: {bool(validation_status)}" 
            
            write_yaml_file(file_path= self.data_validation_config.report_file_path, 
                            content = content)

            logging.info(f"Data validation artifact: {data_validation_artifacts}")
            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e
        