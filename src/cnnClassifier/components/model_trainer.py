
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import ModelTrainerConfig

import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf


class ModelTraining:
    """
     This class trains the data with updated Vgg16 model
    """
    def __init__(self, model_training_config:ModelTrainerConfig):
        self.model_training_config= model_training_config 
        
    
    def get_base_model(self):
        """
        Method Name : get_base_model
        Description : loads updated VGG16 model from artifacts/prepare_base_model/base_model_updated.h5
        Output      : 
        On Failure  :   Write an exception log and then raise an exception
        """
        logger.info("Getting base model")
        try:
            self.model= tf.keras.models.load_model(self.model_training_config.updated_base_model_path) # artifacts/prepare_base_model/base_model_updated.h5
            
        except Exception as e:
            raise e
        
    def train_valid_generator(self):
        """
        Method Name : train_valid_generator
        Description : performs train test split of the data
        Output      : 
        On Failure  :   Write an exception log and then raise an exception
        
        """
        logger.info("Data split: Training and validation: started!")
        data_generator_kwargs= dict(rescale= 1./255,
                                   validation_split= 0.20)
        
        dataflow_kwargs= dict(target_size= self.model_training_config.params_image_size[:-1],
                              batch_size= self.model_training_config.params_batch_size,
                              interpolation= "bilinear")
        
        valid_data_generator= tf.keras.preprocessing.image.ImageDataGenerator(**data_generator_kwargs)
        self.valid_generator= valid_data_generator.flow_from_directory(directory= self.model_training_config.training_data,
                                                                       subset= "validation",
                                                                       shuffle= False,
                                                                       **dataflow_kwargs)
        
        if self.model_training_config.params_is_augmentation:
            train_data_generator= tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=40,
                                                                                  horizontal_flip=True,
                                                                                  width_shift_range=0.2,
                                                                                  height_shift_range=0.2,
                                                                                  shear_range=0.2,
                                                                                  zoom_range=0.2,
                                                                                  **data_generator_kwargs)
        else:
            train_data_generator= valid_data_generator
            
        self.train_generator= train_data_generator.flow_from_directory(directory= self.model_training_config.training_data,
                                                                       subset= "training",
                                                                       shuffle= True,
                                                                       **dataflow_kwargs)
        logger.info("Data split: Training and validation: completed!")
        
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
    
    def train(self):
        self.steps_per_epoch= self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps= self.valid_generator.samples // self.valid_generator.batch_size
        
        logger.info("Model is fit")
        self.model.fit(self.train_generator,
                       epochs=self.model_training_config.params_epochs,
                       steps_per_epoch=self.steps_per_epoch,
                       validation_steps=self.validation_steps,
                       validation_data=self.valid_generator
                       )
        
        logger.info("Trained model is saved")
        self.save_model(path=self.model_training_config.trained_model_path,
                        model= self.model)