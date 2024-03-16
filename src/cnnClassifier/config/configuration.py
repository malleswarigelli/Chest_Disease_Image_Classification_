from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import logger

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
        create_directories([data_ingestion_config.root_dir]) # creates artifacts/data_ingestion directory
        
        # returning from entity: DataIngestionConfig dataclass
        data_ingestion_config= DataIngestionConfig(
            root_dir = data_ingestion_config.root_dir,
            source_URL= data_ingestion_config.source_URL,
            local_data_file= data_ingestion_config.local_data_file,          
            unzip_dir= data_ingestion_config.unzip_dir
        )
        logger.info("Then, exiting get_data_ingestion_config method of ConfigurationManager")
        return data_ingestion_config
        