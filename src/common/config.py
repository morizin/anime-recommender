from src.common.constants import TRANSFORMED_DATA_DIR
import yaml
from src.common.config_entity import (
    DataTransformationConfig,
    DataRetrievalConfig,
    RecommenderConfig,
)
import os


class ConfigurationManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_path, "r") as file:
            config = yaml.safe_load(file)
        return config

    def get_data_transformation_config(self):
        return DataTransformationConfig(
            indir=self.config["data"]["indir"],
            format=self.config["data"]["transforms"]["format"],
            outdir=TRANSFORMED_DATA_DIR,
        )

    def get_data_retrieval_config(
        self,
    ):
        return DataRetrievalConfig(
            persist_dir=self.config["data"]["persist_dir"],
            csv_file_path=os.path.join(TRANSFORMED_DATA_DIR, "data.csv"),
            model=self.config["data"]["embed_model"],
        )

    def get_recommender_config(self):
        return RecommenderConfig(
            llm=self.config["recommender"]["llm"],
            temperature=self.config["recommender"]["temperature"],
        )

    def __repr__(self):
        lines = [f"ConfigurationManager(config_path='{self.config_path}')"]

        def format_config(config, indent=0):
            for key, value in config.items():
                if isinstance(value, dict):
                    lines.append(" " * indent + f"{key}:")
                    format_config(value, indent + 2)
                else:
                    lines.append(" " * indent + f"{key}: {value}")

        format_config(self.config)
        return "\n".join(lines)


if __name__ == "__main__":
    config_manager = ConfigurationManager("./config/config.yaml")
