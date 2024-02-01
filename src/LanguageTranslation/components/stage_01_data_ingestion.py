import os
import urllib.request as request
import zipfile
from datasets import load_dataset
from pathlib import Path
from LanguageTranslation.utils.utils import get_size
from LanguageTranslation.logging import logger
from LanguageTranslation.entity.config_entity import DataIngestionConfig
from LanguageTranslation.config.configuration import ConfigurationManager



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            dataset = load_dataset("cfilt/iitb-english-hindi")
            dataset.save_to_disk(self.config.local_data_file)
            logger.info(f" download! with following info:")
            
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  
  

        
    '''
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    '''



'''
config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()
data_ingestion = DataIngestion(config=data_ingestion_config)
data_ingestion.download_file()
'''