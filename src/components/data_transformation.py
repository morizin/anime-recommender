from src.common.config_entity import DataTransformationConfig
from src.common.utils import create_directory
import pandas as pd
import os


class DataTransformationComponent:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform(self):
        data = pd.read_csv(os.path.join(self.config.indir, "data.csv"))
        create_directory(self.config.outdir)
        required_columns = {"Name", "Genres", "sypnopsis"}

        missing_columns = required_columns - set(data.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        transformed_csv = data[["Name", "Genres", "sypnopsis"]]
        transformed_csv["combined_info"] = transformed_csv.apply(
            lambda row: self.config.format.format(
                title=row["Name"], genres=row["Genres"], sypnopsis=row["sypnopsis"]
            ),
            axis=1,
        )
        transformed_csv.insert(0, "id", range(1, len(transformed_csv) + 1))
        transformed_csv[["id", "combined_info"]].to_csv(
            os.path.join(self.config.outdir, "data.csv"), index=False
        )

    def __call__(self):
        self.transform()


if __name__ == "__main__":
    from ..common.config import ConfigurationManager

    config_manager = ConfigurationManager("./config/config.yaml")
    data_transformation_config = config_manager.get_data_transformation_config()
    DataTransformationComponent(config=data_transformation_config)()
