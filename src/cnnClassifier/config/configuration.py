from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig,
                                                ModelTrainerConfig)
from cnnClassifier import logger
import os

# write configuration manager
class ConfigurationManager:
    """
    ConfigurationManager class captures & returns configuration for components implementation
        
    """
    def __init__(self,
        # params: config.yaml, params.yaml file paths          
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        # read config, params yaml file
        self.config = read_yaml(config_filepath) # returns ConfigBox to access data easily
        self.params = read_yaml(params_filepath)
        
        # create artifact directory
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config (self) -> DataIngestionConfig:
        """
        Method: get_data_ingestion_config
        Params:
        Returns: configuration for Data Ingestion component i.e DataIngestionConfig 
        """
        logger.info("Entering get_data_ingestion_config method of ConfigurationManager")
        data_ingestion_config = self.config.data_ingestion # data_ingestion key from config.yaml
        create_directories([
            Path(data_ingestion_config.root_dir)
            ]) # creates artifacts/data_ingestion directory
        
        # returning from entity: DataIngestionConfig dataclass
        data_ingestion_config= DataIngestionConfig(
            root_dir = Path(data_ingestion_config.root_dir),
            source_URL= data_ingestion_config.source_URL,
            local_data_file= Path(data_ingestion_config.local_data_file),          
            unzip_dir= Path(data_ingestion_config.unzip_dir)
        )
        logger.info("Then, exiting get_data_ingestion_config method of ConfigurationManager")
        return data_ingestion_config
        
    def get_prepare_base_model_config (self) -> PrepareBaseModelConfig:
        """
        Method: get_prepare_base_model_config
        Params:
        Returns: configurations from config.yaml, params.yaml for prepare_base_model component i.e PrepareBaseModelConfig 
        """
        logger.info("Entering get_prepare_base_model_config method of ConfigurationManager")
        prepare_base_model_config = self.config.prepare_base_model # prepare_base_model key from config.yaml
        params_config = self.params
        create_directories([
            Path(prepare_base_model_config.root_dir)
            ]) # creates artifacts/prepare_base_model
        
        # returning from entity: PrepareBaseModelConfig dataclass
        prepare_base_model_config= PrepareBaseModelConfig(
            root_dir = Path(prepare_base_model_config.root_dir),
            base_model_path= Path(prepare_base_model_config.base_model_path),
            updated_base_model_path= Path(prepare_base_model_config.updated_base_model_path),
            params_image_size= params_config.IMAGE_SIZE, 
            params_learning_rate= params_config.LEARNING_RATE, 
            params_include_top= params_config.INCLUDE_TOP,
            params_weights= params_config.WEIGHTS,
            params_classes= params_config.CLASSES   
          
        )
        logger.info("Then, exiting prepare_base_model method of ConfigurationManager")
        return prepare_base_model_config
    
    def get_model_trainer_config (self) -> ModelTrainerConfig:
        """
        Method: get_model_trainer_config
        Params:
        Returns: configuration for Model Trainer component i.e ModelTrainerConfig 
        """
        logger.info("Entering get_model_trainer_config method of ConfigurationManager")
        model_trainer_config = self.config.model_training # model_training key from config.yaml
        prepare_base_model_config = self.config.prepare_base_model # prepare_base_model key from config.yaml
        params_config = self.params # params.yaml              
        training_data= os.path.join(self.config.data_ingestion.unzip_dir, "Chest-CT-Scan_data") # training data from data ingestion artifact
        
        create_directories([
            Path(model_trainer_config.root_dir)
                 ]) # creates artifacts/model_training directory
        
        # returning from entity: ModelTrainerConfig dataclass
        model_trainer_config= ModelTrainerConfig(
            root_dir = Path(model_trainer_config.root_dir),
            trained_model_path= Path(model_trainer_config.trained_model_path),
            updated_base_model_path= Path(prepare_base_model_config.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs= params_config.EPOCHS,
            params_batch_size= params_config.BATCH_SIZE,
            params_is_augmentation= params_config.AUGMENTATION,
            params_image_size= params_config.IMAGE_SIZE
            
        )
        logger.info("Then, exiting get_model_trainer_config method of ConfigurationManager")
        return model_trainer_config