
from pathlib import Path
from cnnClassifier.constants import *
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import logger
import gdown
import os
import zipfile


# write DataIngestion Component
class DataIngestion:
    """
    
    """
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
    
    def download_file(self) ->str:
        """
        Method: download_url
        purpose: fetch data from the url
        Returns: str: _description_
        """
        logger.info("Entering download_file method of DataIngestion component")
        
        try:
            dataset_url = self.data_ingestion_config.source_URL
            zip_download_dir = self.data_ingestion_config.local_data_file #artifacts/data_ingestion/data.zip
            # create directory to store zip file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into {zip_download_dir}")
            
            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir) # gdown.download('from_where', 'to_where')
            
            logger.info(f"Downloaded data from {dataset_url} into {zip_download_dir}")
            logger.info("Then, exiting download_file method of DataIngestion component")
        except Exception as e:
            raise e
            
    def extract_zip_data(self) -> None:
        """
        Method: extract_zip_data
        purpose: Extract zip file into the data directory
        zip_file_path:str
        Returns: None
        
        """
        logger.info("Entering extract_zip_data method of DataIngestion component")
        
        try:
            # path for unzip_dir 
            unzip_path = self.data_ingestion_config.unzip_dir  # artifacts/data_ingestion
            os.makedirs(unzip_path, exist_ok=True) 
            
            logger.info(f"Extracting zip file into {unzip_path}")
            
            zip_file = self.data_ingestion_config.local_data_file
            # unzip from artifacts/data_ingestion/data.zip
            with zipfile.ZipFile(zip_file, "r") as zip_ref:
                # extract into artifacts/data_ingestion
                zip_ref.extractall(unzip_path)
                
            logger.info(f"Extracted zip data from {zip_file} into {unzip_path}") 
            logger.info("Then, exiting extract_zip_data method of DataIngestion component")   
            
        except Exception as e:
            raise e