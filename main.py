from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage04_model_evaluation import ModelEvaluationPipeline



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================================================================================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Prepare Base Model"
try:
    logger.info(f"************************")
    logger.info(f">>>>>>>stage: {STAGE_NAME} started<<<<<<")   
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>OK! stage: {STAGE_NAME} completed<<<<<<\n\nX===========X")
             
except Exception as e:
    logger.exception(e)
    raise e

    
STAGE_NAME= "Model Training Stage"
try:
    logger.info(f">>>>>>>stage: {STAGE_NAME} started<<<<<<")   
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>>stage: {STAGE_NAME} completed<<<<<<\n\nX===========X")
            
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>stage: {STAGE_NAME} started<<<<<<")   
    model_eval = ModelEvaluationPipeline()
    model_eval.main()
    logger.info(f">>>>>>>stage: {STAGE_NAME} completed<<<<<<\n\nX===========X")
            
except Exception as e:
    logger.exception(e)
    raise e