
from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import ModelTraining

STAGE_NAME= "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logger.info("ModelTrainer component started")
            logger.info("Loading of ModelTrainer component configuration started")
            config = ConfigurationManager() # create object for ConfigurationManager class
            model_training_config= config.get_model_trainer_config() # obj.method() returns ModelTrainerConfig
            logger.info("All configuration directories, files needed for ModelTrainer component are ready")
            
            logger.info("ModelTrainer steps started")
            model_trainer = ModelTraining(model_training_config=model_training_config) # create object for ModelTraining class
            model_trainer.get_base_model() # obj.method()    
            model_trainer.train_valid_generator()
            model_trainer.train()
            logger.info("OK! ModelTrainer component completed")
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>>>stage: {STAGE_NAME} started<<<<<<")   
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>stage: {STAGE_NAME} completed<<<<<<\n\nX===========X")
             
    except Exception as e:
        logger.exception(e)
        raise e