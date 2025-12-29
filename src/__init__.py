# src/__init__.py
"""
Diabetes Prediction MLOps Package

A comprehensive MLOps solution for diabetes prediction using machine learning.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .data import ingest_data, validate_data
from .model import train_model, save_model, load_model, predict
from .pipeline import run_training_pipeline
from .utils import load_config, setup_logging
from .exceptions import (
    DiabetesMLOpsException,
    DataIngestionError,
    DataValidationError,
    ModelTrainingError,
    ModelPredictionError,
    ConfigurationError,
)
from .constants import (
    PROJECT_ROOT,
    DATA_DIR,
    MODELS_DIR,
    LOGS_DIR,
    REQUIRED_COLUMNS,
    DEFAULT_MODEL_PARAMS,
    DEFAULT_DATA_PARAMS,
)

__all__ = [
    "ingest_data",
    "validate_data",
    "train_model",
    "save_model",
    "load_model",
    "predict",
    "run_training_pipeline",
    "load_config",
    "setup_logging",
    "DiabetesMLOpsException",
    "DataIngestionError",
    "DataValidationError",
    "ModelTrainingError",
    "ModelPredictionError",
    "ConfigurationError",
    "PROJECT_ROOT",
    "DATA_DIR",
    "MODELS_DIR",
    "LOGS_DIR",
    "REQUIRED_COLUMNS",
    "DEFAULT_MODEL_PARAMS",
    "DEFAULT_DATA_PARAMS",
]