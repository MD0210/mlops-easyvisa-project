from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    feature_store_file_path: str
    training_file_path: str
    testing_file_path: str
    train_test_split_ratio: float
    collection_name: str