import argparse
from src.components.vector_store import VectorStoreComponent
from src.components.recommender import AnimeRecommender
from src.common.config import ConfigurationManager
from src.common.logger import get_logger
from src.common.custom_exception import CustomException

logger = get_logger(__name__)


class RecommendationPipeline:
    def __init__(self, config_path: str = "./config/config.yaml"):
        self.config_manager = ConfigurationManager(config_path)
        self.retrieval_config = self.config_manager.get_data_retrieval_config()
        self.vector_store = VectorStoreComponent(
            self.retrieval_config
        ).load_vector_store()
        self.recommender_config = self.config_manager.get_recommender_config()
        self.recommender = AnimeRecommender(
            retriever=self.vector_store,
            model_name=self.recommender_config.llm,
            temperature=self.recommender_config.temperature,
        )

    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received query: {query}")
            response = self.recommender.recommend(query)
            logger.info("Generated recommendations successfully.")
            return response
        except Exception as e:
            logger.error(f"Error during recommendation: {e}")
            raise CustomException(f"Failed to generate recommendations: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Anime Recommender System")
    parser.add_argument(
        "--config_path",
        type=str,
        default="./config/config.yaml",
        help="Path to the configuration file",
    )
    args = parser.parse_args()
    pipeline = RecommendationPipeline(config_path=args.config_path)
    query = input(
        "Enter your anime preferences (e.g., light-hearted anime with school settings): "
    )
    if query:
        response = pipeline.recommend(query)
        print("Recommendations:")
        print(response)
