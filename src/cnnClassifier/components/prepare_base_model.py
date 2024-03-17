import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from cnnClassifier import logger



# write PrepareBaseModel Component
class PrepareBaseModel: 
    """
    This class gets VGG16 base model from keras, update bottom layers
    """
    
    def __init__(self, prepare_base_model_config:PrepareBaseModelConfig):
        """
        :param prepare_base_model_config: configuration for PrepareBaseModel    
        """
        self.prepare_base_model_config = prepare_base_model_config
        
    def get_base_model(self):
        """
        Method Name : get_base_model
        Description : fetch VGG16 base model from keras.applications
        Output      : 
        On Failure  :   Write an exception log and then raise an exception
        """
        logger.info("Entering get_base_model method of PrepareBaseModel")
        try:
            self.base_model= tf.keras.applications.vgg16.VGG16(
                include_top= self.prepare_base_model_config.params_include_top, 
                weights= self.prepare_base_model_config.params_weights,              
                input_shape= self.prepare_base_model_config.params_image_size         
                     
            )
            self.save_model(path= self.prepare_base_model_config.base_model_path, model=self.base_model)
            
            logger.info("Saved Vgg16 base model")
            logger.info("Then, exiting get_base_model method of PrepareBaseModel")
            
        except Exception as e:
            raise e
        
    @staticmethod
    def _prepare_full_model(base_model, classes, freeze_all, freeze_till, learning_rate):
        """
        Method Name : _prepare_full_model
        Description : update the base model (change architexture by adding custom dense layer)
        Output      : 
        On Failure  :  Write an exception log and then raise an exception
        
        """
        logger.info("Entering _prepare_full_model method of PrepareBaseModel")
        
        try: 
            logger.info("Freezing the layers")
            if freeze_all:
                for layer in base_model.layers:
                    base_model.trainable= False
            elif (freeze_all is not None) and (freeze_till > 0):
                for layer in base_model.layers[:-freeze_till]:
                    base_model.trainable= False
                
            logger.info("Flattening the layers")
            flatten_in = tf.keras.layers.Flatten()(base_model.output)  
            
            logger.info("Custom dense layer added!")
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(flatten_in) 
            
            logger.info("Preparing custom architexture of the model!")
            full_model = tf.keras.models.Model(
                inputs= base_model.input,
                outputs= prediction
            ) 
            
            logger.info("Compiling the model!")
            full_model.compile(
                optimizer= tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss= tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"]
            )
        
            full_model.summary()
            logger.info("Returning full architexture of the model")
            logger.info("Then, exiting _prepare_full_model method of PrepareBaseModel")
            return full_model
        
        except Exception as e:
            raise e
        
    def get_updated_base_model(self):
        """
        Method Name : get_updated_base_model
        Description : get updated vgg16 model
        Output      : 
        On Failure  :  Write an exception log and then raise an exception
        
        """
        logger.info("Entering get_updated_base_model method of PrepareBaseModel")
        
        try: 
            self.full_model= self._prepare_full_model(
                base_model= self.base_model, 
                classes= self.prepare_base_model_config.params_classes, 
                freeze_all= True, 
                freeze_till= None, 
                learning_rate= self.prepare_base_model_config.params_learning_rate
            ) 
            self.save_model(path= self.prepare_base_model_config.updated_base_model_path, model=self.full_model)
            
            logger.info("Saved updated Vgg16 model")
            logger.info("Then, exiting get_updated_base_model method of PrepareBaseModel")
            
        except Exception as e:
            raise e
        
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)