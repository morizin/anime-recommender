from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    indir: str
    format: str
    outdir: str


@dataclass
class DataRetrievalConfig:
    persist_dir: str
    csv_file_path: str
    model: str


@dataclass
class RecommenderConfig:
    llm: str
    temperature: float
