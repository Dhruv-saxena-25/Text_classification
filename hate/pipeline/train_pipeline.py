import sys
from hate.logger import logging
from hate.exception import CustomException
from hate.components.data_ingestion import DataIngestion
from hate.components.data_validation import DataValidation
from hate.components.data_transforamation import DataTransformation

from hate.entity.config_entity import (DataIngestionConfig, 
                                       DataValidationConfig,
                                       DataTransformationConfig,)

from hate.entity.artifact_entity import (DataIngestionArtifacts,
                                         DataValidationArtifacts,
                                         DataTransformationArtifacts,)

class TrainPipeline:

    def __init__(self):
        try: 
            self.data_ingestion_config = DataIngestionConfig()
            self.data_validation_config = DataValidationConfig()
            self.data_transformation_config = DataTransformationConfig()
        except Exception as e:
            raise CustomException(e, sys) from e
    
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from GCLoud Storage bucket")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and valid from GCLoud Storage")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
        

    def start_data_validation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataValidationArtifacts:
        try:
        
            logging.info("Entered the start_data_validation method of TrainPipeline class")
            data_validation = DataValidation(data_ingestion_artifacts= data_ingestion_artifacts,
                                             data_validation_config=self.data_validation_config)

            data_validation_artifacts = data_validation.initiate_data_validation()
            
            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifacts
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def start_data_transformation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataTransformationArtifacts:
        try:
            logging.info("Entered the start_data_trnaformation method of TrainPipeline class")

            data_taransforamtion = DataTransformation(data_ingestion_artifacts= data_ingestion_artifacts,
                                                      data_transformation_config= self.data_transformation_config)
            data_taransforamtion_artifacts = data_taransforamtion.initiate_data_transformation()


            logging.info("Performed the data transformation operation")
            logging.info("Exited the start_data_trnaformation method of TrainPipeline class")

            return data_taransforamtion_artifacts
        
        except Exception as e:
            raise CustomException(e, sys) from e

        

    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifacts=data_ingestion_artifacts)
            data_taransforamtion_artifacts = self.start_data_transformation(data_ingestion_artifacts=data_ingestion_artifacts)
        except Exception as e:
            raise CustomException(e, sys) from e  