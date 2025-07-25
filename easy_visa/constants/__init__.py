import os
from datetime import date

DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL"
PIPELINE_NAME: str = "us_visa_pipeline"
ARTIFACTS_DIR: str = "artifacts"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "EasyVisa.csv"
MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessor.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1" 



"""
Data Ingestion related constants start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""
Data Validation related constants start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "data_drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

"""
Data Transformation related constants start with DATA_TRANSFORMATION VAR NAME
"""

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

"""
Model Trainer related constants start with MODEL_TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINING_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINING_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")

"""
Model Evaluation related constants 
"""

MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.2
MODEL_BUCKET_NAME: str = "easyvisa-model2025"
MODEL_PUSHER_S3_KEY: str = "model-registry"

APP_HOST = "0.0.0.0"
APP_PORT = 8080