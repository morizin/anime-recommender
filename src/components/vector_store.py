from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from src.common.config_entity import DataRetrievalConfig


class VectorStoreComponent:
    def __init__(self, config: DataRetrievalConfig):
        self.config = config

    def create_vector_store(self):
        loader = CSVLoader(file_path=self.config.csv_file_path, encoding="utf-8")
        documents = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        split_documents = splitter.split_documents(documents)

        db = Chroma.from_documents(
            split_documents,
            HuggingFaceEmbeddings(model_name=self.config.model),
            persist_directory=self.config.persist_dir,
        )
        return db

    def load_vector_store(self):
        db = Chroma(
            persist_directory=self.config.persist_dir,
            embedding_function=HuggingFaceEmbeddings(model_name=self.config.model),
        )
        retriever = db.as_retriever()
        return retriever
