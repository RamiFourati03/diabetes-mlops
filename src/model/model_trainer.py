# src/model/model_trainer.py
"""
Machine learning model training and prediction module.
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib
import mlflow
import mlflow.sklearn
import logging
from pathlib import Path
import numpy as np
from ..utils.common import load_config
from ..constants import MODEL_FILE, DEFAULT_MODEL_PARAMS
from ..exceptions import ModelTrainingError, ModelPredictionError

def train_model(X_train, y_train, X_test, y_test):
    """
    Train the model and log metrics with MLflow
    Args:
        X_train, y_train: Training data
        X_test, y_test: Test data
    Returns:
        trained model
    """
    logger = logging.getLogger(__name__)
    config = load_config()

    # Set MLflow experiment
    mlflow.set_experiment(config["mlflow"]["experiment_name"])

    with mlflow.start_run():
        # Get model parameters
        model_params = config["model"]["params"]

        # Train model
        logger.info("Training Random Forest model...")
        model = RandomForestClassifier(**model_params)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]

        # Calculate metrics
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred),
            "roc_auc": roc_auc_score(y_test, y_pred_proba)
        }

        # Log parameters and metrics
        mlflow.log_params(model_params)
        mlflow.log_metrics(metrics)

        # Log model
        mlflow.sklearn.log_model(model, "model")

        logger.info(f"Model trained successfully. Metrics: {metrics}")

        return model

def save_model(model, filepath=None):
    """
    Save the trained model

    Args:
        model: Trained model
        filepath: Path to save the model (relative to project root)

    Raises:
        ModelTrainingError: If model saving fails
    """
    logger = logging.getLogger(__name__)

    if filepath is None:
        filepath = MODEL_FILE
    else:
        project_root = Path(__file__).parent.parent.parent
        filepath = project_root / filepath

    try:
        # Create models directory if it doesn't exist
        filepath.parent.mkdir(exist_ok=True)
        joblib.dump(model, filepath)
        logger.info(f"Model saved to {filepath}")
    except Exception as e:
        logger.error(f"Failed to save model: {e}")
        raise ModelTrainingError(f"Model saving failed: {e}")

    joblib.dump(model, filepath)
    logger.info(f"Model saved to {filepath}")

    # Log model artifact in MLflow
    mlflow.log_artifact(filepath, "model")

def save_metrics(metrics, filepath="metrics.json"):
    """
    Save model metrics to JSON file
    Args:
        metrics: Dictionary of metrics
        filepath: Path to save metrics
    """
    import json
    with open(filepath, 'w') as f:
        json.dump(metrics, f, indent=4)

    # Log metrics in MLflow
    mlflow.log_metrics(metrics)
    mlflow.log_artifact(filepath, "metrics")

def load_model(filepath=None):
    """
    Load a saved model

    Args:
        filepath: Path to the saved model (relative to project root)

    Returns:
        Loaded model

    Raises:
        ModelPredictionError: If model loading fails
    """
    if filepath is None:
        filepath = MODEL_FILE
    else:
        project_root = Path(__file__).parent.parent.parent
        filepath = project_root / filepath

    try:
        model = joblib.load(filepath)
        logging.getLogger(__name__).info(f"Model loaded from {filepath}")
        return model
    except Exception as e:
        logging.getLogger(__name__).error(f"Failed to load model: {e}")
        raise ModelPredictionError(f"Model loading failed: {e}")


def predict(model, input_data):
    """
    Make predictions with the model

    Args:
        model: Trained model
        input_data: Input features as numpy array

    Returns:
        tuple: (prediction (0 or 1), probability)
    """
    try:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        return int(prediction), float(probability)
    except Exception as e:
        logging.getLogger(__name__).error(f"Failed to make prediction: {e}")
        raise ModelPredictionError(f"Prediction failed: {e}")