# src/constants.py
"""
Constants and configuration values for the diabetes prediction MLOps project.
"""

from pathlib import Path

# Project structure
PROJECT_ROOT = Path(__file__).parent.parent

# Data paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_FILE = DATA_DIR / "diabetes.csv"

# Model paths
MODELS_DIR = PROJECT_ROOT / "models"
MODEL_FILE = MODELS_DIR / "diabetes_model.pkl"

# Logs
LOGS_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOGS_DIR / "app.log"

# Configuration
CONFIG_FILE = PROJECT_ROOT / "params.yaml"

# MLflow
MLFLOW_DIR = PROJECT_ROOT / "mlruns"

# Required columns for diabetes dataset
REQUIRED_COLUMNS = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "BMI",
    "Age",
    "Outcome"
]

# Model parameters defaults
DEFAULT_MODEL_PARAMS = {
    "n_estimators": 100,
    "random_state": 42,
    "max_depth": 10
}

# Data parameters defaults
DEFAULT_DATA_PARAMS = {
    "test_size": 0.2,
    "random_state": 42
}