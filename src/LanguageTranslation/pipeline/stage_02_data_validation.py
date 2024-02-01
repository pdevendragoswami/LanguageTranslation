from LanguageTranslation.config.configuration import ConfigurationManager
from LanguageTranslation.components.stage_02_data_validation import DataValidation
from LanguageTranslation.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()


'''
data_validation = DataValidationTrainingPipeline()
data_validation.main()
'''
