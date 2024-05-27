# Creating model architecture.
from hate.entity.config_entity import ModelTrainerConfig
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM,Activation,Dense,Dropout,Input,Embedding,SpatialDropout1D
from hate.constants import *
from hate.exception import CustomException
import sys

class ModelArchitecture:
    def __init__(self):
        pass

    def get_model(self):
        try:
            # Creating model architecture.
            model = Sequential()
            model.add(Embedding(MAX_WORDS,50,input_length=MAX_LEN))
            model.add(SpatialDropout1D(0.2))
            model.add(LSTM(50,dropout=0.2,recurrent_dropout=0.2))
            model.add(Dense(1,activation=ACTIVATION))
            model.summary()
            model.compile(loss= LOSS,
                          optimizer=RMSprop(),
                          metrics= METRICS)

            return model
        except Exception as e:
            raise CustomException(e, sys) from e
        
