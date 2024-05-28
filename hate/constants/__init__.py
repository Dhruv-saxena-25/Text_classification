import os 

from datetime import datetime

import os

from datetime import datetime



# Common Constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR =   os.path.join("artifacts", TIMESTAMP)
ZIP_FILE_NAME = 'dataset.zip'
LABEL = 'label'
TWEET = 'tweet'
BUCKET_NAME = 'hates-speech-project'
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# Data Ingestion Constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"

# Data Validation Constants
DATA_VALIDATION_ARTIFACTS_DIR: str = "DataValidationArtifacts"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# Data Transformation Constants
DATA_TRANSFORMATION_ARTIFACTS_DIR = 'DataTransformationArtifacts'
TRANSFORMED_FILE_NAME = "final.csv"
DATA_DIR = "data"
ID = 'id'
AXIS = 1
INPLACE = True
DROP_COLUMNS = ['count','hate_speech','offensive_language','neither']
CLASS = 'class'


# Model Training Constants

MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainerArtifacts"
TRAINED_MODEL_DIR = 'trained_model'
TRANINED_MODEL_NAME = 'model.h5'
X_TEST_FILE_NAME = 'x_test.csv'
Y_TEST_FILE_NAME = 'y_test.csv'

X_TRAIN_FILE_NAME = 'x_train.csv'

TEST_SIZE = 0.3

RANDOM_STATE = 2024
EPOCH = 7
BATCH_SIZE = 128
VALIDATION_SPLIT = 0.2

# Model Architecture Constants

MAX_WORDS = 5000
MAX_LEN = 300
LOSS = 'binary_crossentropy' 
METRICS = ['accuracy'] 
ACTIVATION = 'sigmoid'

# Model  Evaluation Constants

MODEL_EVALUATION_ARTIFACTS_DIR = "ModelEvaluationArtifacts"
BEST_MODEL_DIR = 'Best_Model'
MODEL_EVALUATION_FILE_NAME = 'loss.csv'
MODEL_NAME = 'model.h5'

# Flask Constants 
APP_HOST = "0.0.0.0"
APP_PORT = 8080

