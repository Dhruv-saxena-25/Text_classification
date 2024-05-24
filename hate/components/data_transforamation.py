import os, sys, re, string
import nltk
import pandas as pd
from nltk.corpus import stopwords
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from hate.logger import logging
from hate.exception import CustomException
from hate.entity.config_entity import DataTransformationConfig
from hate.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts


class DataTransformation:
    def __init__(self, data_transformation_config : DataTransformationConfig, data_ingestion_artifacts : DataIngestionArtifacts):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts

    
    def imbalance_data_cleaning(self):
        try:
            logging.info(" Entered into the imbalance_data_cleaning function")
            imbalance_data = pd.read_csv(self.data_ingestion_artifacts.imbalance_data_file_path)
            imbalance_data.drop(self.data_transformation_config.ID, axis= self.data_transformation_config.AXIS, 
                                inplace= self.data_transformation_config.INPLACE)
            logging.info(f"Exited into the imbalance_data_cleaning function and returned imbalance data {imbalance_data}")
            return imbalance_data
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def raw_data_cleaning(self):
        try:
            logging.info(" Entered into the raw_data_cleaning function")
            ## read the cvs data file from the data_ingestion_artifacts 
            raw_data = pd.read_csv(self.data_ingestion_artifacts.raw_data_file_path)
            ## Dropping the unnecessary columns
            raw_data.drop(self.data_transformation_config.DROP_COLUMNS, axis= self.data_transformation_config.AXIS,
                          inplace= self.data_transformation_config.INPLACE)
            
            # Let's copy the valus of the class 1 into class 0. 
            raw_data[raw_data[self.data_transformation_config.CLASS] == 0][self.data_transformation_config.CLASS] =1  # raw_data[raw_data['class'] == 0]['class']=1              

            # replace the value of 0 to 1
            raw_data[self.data_transformation_config.CLASS].replace({0: 1}, inplace= self.data_transformation_config.INPLACE) # raw_data["class"].replace({0:1},inplace=True)


            # Let's replace the value of 2 to 0.
            raw_data[self.data_transformation_config.CLASS].replace({2 :0}, inplace= self.data_transformation_config.INPLACE) # raw_data["class"].replace({2:0}, inplace = True)

            # Let's change the name of the 'class' to label
            
            raw_data.rename(columns= {self.data_transformation_config.CLASS : self.data_transformation_config.LABEL}, inplace= self.data_transformation_config.INPLACE) # raw_data.rename(columns={'class':'label'},inplace =True)            

            logging.info(f"Exited into the raw_data_cleaning function and returned raw data {raw_data}")
            return raw_data
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def concat_dataframe(self):
        try:
            logging.info(f"Entered into the concat_dataframe function")
            # Let's concatinate both the data into a single data frame.

            frame = [self.raw_data_cleaning(), self.imbalance_data_cleaning()]  # frame = [imb_data, raw_data]

            df= pd.concat(frame)
            print(df.head(2))
            
            logging.info(f"returned the concatinated dataframe {df}")
            return df    
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def concat_data_cleaning(self, words):
        try:

            logging.info("Entered into the concat_data_cleaning function")
            # Let's apply stemming and stopwords on the data
            stemmer = nltk.SnowballStemmer('english')
            stopword = set(stopwords.words('english'))
            words = str(words).lower()
            words = re.sub('\[.*?\]', '', words)
            words = re.sub('https?://\S+|www\.\S+', '', words)
            words = re.sub('[%s]' % re.escape(string.punctuation), '', words)
            words = re.sub('\n', '', words)
            words = re.sub('\w*\d\w*', '', words)
            words = re.sub('<.*?>+', '', words)
            words = [word for word in words.split(' ') if words not in stopword]
            words = " ".join(words)
            words = [stemmer.stem(words) for word in words.split(' ')]
            words=" ".join(words)
            
            logging.info("Exited the concat_data_cleaning function")
            return words

        except Exception as e:
            raise CustomException(e, sys) from e
        
    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        try:
            logging.info("Entered the initiate_data_transformation method of Data transformation class")
            self.imbalance_data_cleaning()
            self.raw_data_cleaning()
            df = self.concat_dataframe()
            # let's apply the data_cleaning on the data.
            df[self.data_transformation_config.TWEET]= df[self.data_transformation_config.TWEET].apply(self.concat_data_cleaning)  # df['tweet']=df['tweet'].apply(data_cleaning)
            
            # Create Directory in the Artifats Folder 
            os.makedirs(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR, exist_ok=True)

            # Save the cleaned data into new csv file `final.csv`
            df.to_csv(self.data_transformation_config.TRANSFORMED_FILE_PATH, index= False, header= True)

            data_transformation_artifacts = DataTransformationArtifacts(
                transformed_data_path= self.data_transformation_config.TRANSFORMED_FILE_PATH
            )

            logging.info("returning the DataTransformationArtifacts")
            return data_transformation_artifacts  
        except Exception as e:
            raise CustomException(e, sys) from e
        
        