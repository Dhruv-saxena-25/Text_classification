from dataclasses import dataclass


# Data ingestion artifacts
@dataclass

class DataIngestionArtifacts:
    imbalance_data_file_path: str
    raw_data_file_path: str
    
@dataclass
class DataValidationArtifacts:
    validation_status:bool
    message: str
    report_file_path: str

@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str


@dataclass 
class ModelTrainerArtifacts: 
    trained_model_path:str
    X_test_path: list
    y_test_path: list
