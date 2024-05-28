from hate.logger import logging
from hate.exception import CustomException
import sys
from hate.configuration.gcloud_syncer import GCloudSync
from hate.pipeline.train_pipeline import TrainPipeline


obj = TrainPipeline()
obj.run_pipeline()

# obj = GCloudSync()

# obj.sync_folder_from_gcloud("hates-speech-project", "dataset.zip", "download/dataset")