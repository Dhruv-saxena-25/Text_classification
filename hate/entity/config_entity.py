from dataclasses import dataclass
from hate.constants import *
import os 

# Data Ingestion Configuration

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.ZIP_FILE_NAME = ZIP_FILE_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR,DATA_INGESTION_ARTIFACTS_DIR)
        self.DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR,DATA_INGESTION_IMBALANCE_DATA_DIR)
        self.NEW_DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR,DATA_INGESTION_RAW_DATA_DIR)
        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(self.ZIP_FILE_DIR, self.ZIP_FILE_NAME)


# Data Validation COnfiguration
@dataclass
class DataValidationConfig:
        data_validation_dir: str = os.path.join(ARTIFACTS_DIR, DATA_VALIDATION_DIR_NAME)
        report_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_REPORT_FILE_NAME)


# Data Transformation Configuration
@dataclass 
class DataTransformationConfig:
    def __init__(self):
         self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
         self.TRANSFORMED_FILE_PATH: str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_FILE_NAME)
         self.ID = ID
         self.AXIS = AXIS
         self.INPLACE = INPLACE
         self.DROP_COLUMNS = DROP_COLUMNS
         self.CLASS = CLASS
         self.LABEL = LABEL
         self.TWEET = TWEET


