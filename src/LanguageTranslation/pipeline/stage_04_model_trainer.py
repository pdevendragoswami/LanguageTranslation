from LanguageTranslation.config.configuration import ConfigurationManager
from LanguageTranslation.components.stage_04_model_trainer import ModelTrainer
from LanguageTranslation.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()




'''
model_trainer = ModelTrainerTrainingPipeline()
model_trainer.main()
'''
