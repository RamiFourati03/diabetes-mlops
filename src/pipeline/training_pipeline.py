# src/pipeline/training_pipeline.py
"""
ML pipeline orchestration module.
"""

from ..data.data_ingestion import ingest_data, validate_data
from ..model.model_trainer import train_model, save_model
import logging
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from ..utils.common import load_config, setup_logging, get_project_root

def run_training_pipeline():
    """
    Main training pipeline
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting training pipeline...")

    try:
        # Load configuration
        config = load_config()

        # Ingest data
        df = ingest_data()

        # Validate data
        if not validate_data(df):
            raise ValueError("Data validation failed")

        # Prepare features and target
        feature_columns = ["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]
        X = df[feature_columns]
        y = df["Outcome"]

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=config["data"]["test_size"],
            random_state=config["data"]["random_state"]
        )

        logger.info(f"Training data shape: {X_train.shape}")
        logger.info(f"Test data shape: {X_test.shape}")

        # Train model
        model = train_model(X_train, y_train, X_test, y_test)

        # Save model
        save_model(model)

        # Save metrics
        from src.model.model_trainer import save_metrics
        # Recalculate metrics for saving
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        metrics = {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred)),
            "recall": float(recall_score(y_test, y_pred)),
            "f1_score": float(f1_score(y_test, y_pred)),
            "roc_auc": float(roc_auc_score(y_test, y_pred_proba))
        }
        save_metrics(metrics)

        logger.info("Training pipeline completed successfully!")

    except Exception as e:
        logger.error(f"Training pipeline failed: {e}")
        raise

if __name__ == "__main__":
    # Setup logging
    from src.data.data_ingestion import setup_logging
    setup_logging()
    run_training_pipeline()