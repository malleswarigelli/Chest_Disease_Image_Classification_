from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline



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

if __name__=='__main__':
    try:
        logger.info(f"************************")
        logger.info(f">>>>>>>stage: {STAGE_NAME} started<<<<<<")   
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>OK! stage: {STAGE_NAME} completed<<<<<<\n\nX===========X")
             
    except Exception as e:
        logger.exception(e)
        raise e