# Vector Store creation pipeline
from src.common.logger import get_logger
from src.common.config import ConfigurationManager
from src.components.data_transformation import DataTransformationComponent
from src.components.vector_store import VectorStoreComponent

logger = get_logger(__name__)


class VectorStorePipeline:
    def __init__(self, config_manager: ConfigurationManager):
        self.config_manager = config_manager

    def run(self):
        data_transformation_config = (
            self.config_manager.get_data_transformation_config()
        )
        DataTransformationComponent(config=data_transformation_config)()

        data_retrieval_config = self.config_manager.get_data_retrieval_config()
        vector_store_component = VectorStoreComponent(config=data_retrieval_config)
        vector_store_component.create_vector_store()


if __name__ == "__main__":
    config_manager = ConfigurationManager("./config/config.yaml")
    vector_store_pipeline = VectorStorePipeline(config_manager=config_manager)
    vector_store_pipeline.run()
