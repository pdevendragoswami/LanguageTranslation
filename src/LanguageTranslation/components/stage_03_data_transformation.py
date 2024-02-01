from LanguageTranslation.entity.config_entity import DataTransformationConfig
from LanguageTranslation.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from LanguageTranslation.logging import logger
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)



    def preprocess_function(self,examples):
        inputs = [ex["en"] for ex in examples["translation"]]
        targets = [ex["hi"] for ex in examples["translation"]]
        model_inputs = self.tokenizer(inputs, max_length=128, truncation=True)

        # Setup the tokenizer for targets
        with self.tokenizer.as_target_tokenizer():
            labels = self.tokenizer(targets, max_length=128, truncation=True)

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs


    def convert(self):
        dataset_iitb_english_hindi = load_from_disk(self.config.data_path)
        dataset_iitb_english_hindi_pt = dataset_iitb_english_hindi.map(self.preprocess_function, batched = True)
        dataset_iitb_english_hindi_pt.save_to_disk(os.path.join(self.config.root_dir,"iitb-english-hindi_dataset"))



'''
config = ConfigurationManager()
data_transformation_config = config.get_data_transformation_config()
data_transformation = DataTransformation(config=data_transformation_config)
data_transformation.convert() 
'''   
                                                                                      
 