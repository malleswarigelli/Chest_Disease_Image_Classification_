from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion

STAGE_NAME= "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        
        logger.info("Loading of Data Ingestion configuration started")
        config = ConfigurationManager() # create object for ConfigurationManager class
        data_ingestion_config = config.get_data_ingestion_config() # obj.method() returns DataIngestionConfig
        logger.info("All configuration directories, files needed for Data Ingestion component are ready")
        
        logger.info("Data Ingestion steps started")
        data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config) # create object for DataIngestion class
        data_ingestion.download_file() # obj.method()
        data_ingestion.extract_zip_data()
        logger.info("OK! Data Ingestion component completed")
        
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>>>stage {STAGE_NAME} started<<<<<<")   
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>stage {STAGE_NAME} started<<<<<<\n\nX===========X")
             
    except Exception as e:
        logger.exception(e)
        raise e