import os 

from datetime import datetime

import os

from datetime import datetime



# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR =   os.path.join("artifacts", TIMESTAMP)
ZIP_FILE_NAME = 'dataset.zip'
LABEL = 'label'
TWEET = 'tweet'
BUCKET_NAME = 'hates-speech-project'
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"

# Data Validation Constant
DATA_VALIDATION_DIR_NAME: str = "DataValidationArtifacts"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"
