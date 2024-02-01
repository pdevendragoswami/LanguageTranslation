from LanguageTranslation.components.stage_01_data_ingestion import DataIngestion
from LanguageTranslation.config.configuration import ConfigurationManager

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
    



'''
data_ingestion = DataIngestionTrainingPipeline()
data_ingestion.main()
'''
