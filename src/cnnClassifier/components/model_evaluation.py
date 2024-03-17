from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse

from cnnClassifier.constants import *
from cnnClassifier.utils.common import save_json
from cnnClassifier import logger
import tensorflow as tf

from cnnClassifier.utils.common import save_json
from cnnClassifier.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    """
     This class tracks model evaluation metrics
    """
    def __init__(self, evaluation_config:ModelEvaluationConfig):
        self.evaluation_config= evaluation_config 
        
    
    def _valid_generator(self):
        """
        Method Name : _valid_generator
        Description : performs split of training data, slice 30% data for validation 
        Output      : 
        On Failure  :   Write an exception log and then raise an exception
        
        """
        logger.info("Data split for validation data started!")
        data_generator_kwargs= dict(rescale= 1./255,
                                   validation_split= 0.30)
        
        dataflow_kwargs= dict(target_size= self.evaluation_config.params_image_size[:-1],
                              batch_size= self.evaluation_config.params_batch_size,
                              interpolation= "bilinear")
        
        valid_data_generator= tf.keras.preprocessing.image.ImageDataGenerator(**data_generator_kwargs)
        self.valid_generator= valid_data_generator.flow_from_directory(directory= self.evaluation_config.training_data,
                                                                       subset= "validation",
                                                                       shuffle= False,
                                                                       **dataflow_kwargs)
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
        
    def evaluation(self):
        """
        Method Name : evaluation
        Description : performs model evaluation
        Output      : 
        On Failure  :   Write an exception log and then raise an exception
        
        """
        logger.info("Model evaluation started!")
        logger.info("Loading the Trained model")
        self.model= self.load_model(self.evaluation_config.path_of_trained_model)
        logger.info("Generating validation data")
        self._valid_generator()
        logger.info("Evaluating the model, saving loss and accuracy scores")
        self.metric= self.model.evaluate(self.valid_generator)
        self.save_metrics()
        
    def save_metrics(self):
        """
        Method Name : save_score
        Description : saves loss and accuracy scores
        Output      : 
        On Failure  : Write an exception log and then raise an exception
        """
        metrics= {"loss": self.metric[0], "accuracy": self.metric[1]}
        save_json(path= Path("scores.json"), data= metrics)        
        
        
    def log_into_mlflow(self):
        """
        Method Name : log_into_mlflow
        Description : log experiments in mlflow
        Output      : 
        On Failure  : Write an exception log and then raise an exception
        """
        logger.info("Logging Experiments stated in mlflow")
        mlflow.set_registry_uri(self.evaluation_config.mlflow_uri)
        tracking_url_type_store= urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            logger.info("Logging parameters metrics")
            mlflow.log_params(self.evaluation_config.all_params)
            mlflow.log_metrics(
                {"loss":self.metric[0],
                 "accuracy":self.metric[1]}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(self.model, "model", registered_model_name="Vgg16Model")
            else:
                mlflow.sklearn.log_model(self.model, "model")
            
        
        
        