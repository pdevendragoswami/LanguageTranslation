from LanguageTranslation.config.configuration import ConfigurationManager
from LanguageTranslation.components.stage_05_model_evaluation import ModelEvaluation
from LanguageTranslation.logging import logger


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()


'''
model_evaluation = ModelEvaluationTrainingPipeline()
model_evaluation.main()
'''