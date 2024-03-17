from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel

STAGE_NAME= "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        
        logger.info("Loading of PrepareBaseModel component configuration started")
        config = ConfigurationManager() # create object for ConfigurationManager class
        prepare_base_model_config = config.get_prepare_base_model_config() # obj.method() returns PrepareBaseModelConfig
        logger.info("All configuration directories, files needed for PrepareBaseModel component are ready")
        
        logger.info("PrepareBaseModel steps started")
        prepare_base_model = PrepareBaseModel(prepare_base_model_config = prepare_base_model_config) # create object for PrepareBaseModel class
        prepare_base_model.get_base_model() # obj.method()    
        prepare_base_model.get_updated_base_model()
        
# write this for dvc execution    
if __name__=='__main__':
    try:
        logger.info(f">>>>>>>stage: {STAGE_NAME} started<<<<<<")   
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>OK! stage: {STAGE_NAME} completed<<<<<<\n\nX===========X")
             
    except Exception as e:
        logger.exception(e)
        raise e