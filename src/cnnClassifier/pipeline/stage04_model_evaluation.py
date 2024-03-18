from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import ModelEvaluation

STAGE_NAME= "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logger.info("Loading of ModelEvaluation component configuration started")
            config = ConfigurationManager() # create object for ConfigurationManager class
            evaluation_config= config.get_model_evaluation_config() # obj.method() returns ModelEvaluationConfig
            logger.info("All configuration directories, files needed for ModelEvaluation component are ready")
            
            logger.info("ModelEvaluation steps started")
            model_evaluation = ModelEvaluation(evaluation_config=evaluation_config) # create object for ModelTraining class
            model_evaluation.evaluation() # obj.method() 
            model_evaluation.save_metrics()   
            model_evaluation.log_into_mlflow()

            logger.info("OK! ModelEvaluation component completed")
        except Exception as e:
            raise e
        
            
if __name__=='__main__':
    try:
        logger.info(f">>>>>>>stage: {STAGE_NAME} started<<<<<<")   
        model_eval = ModelEvaluationPipeline()
        model_eval.main()
        logger.info(f">>>>>>>stage: {STAGE_NAME} completed<<<<<<\n\nX===========X")
             
    except Exception as e:
        logger.exception(e)
        raise e