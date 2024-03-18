# create dataclass for DataIngestionConfig (inputs from config.yaml)

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # frozen=True means you can't add any additional parameters
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    trained_model_path: Path
    final_trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
    
 
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    metrics_path: Path
    path_of_trained_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_batch_size: int    
    params_image_size: list  