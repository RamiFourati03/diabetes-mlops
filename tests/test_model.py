# tests/test_model.py
import pytest
import numpy as np
from src.model.model_trainer import predict
from src.data.data_ingestion import ingest_data
import joblib

def test_model_prediction():
    """Test model prediction functionality"""
    # Load model
    try:
        model = joblib.load("models/diabetes_model.pkl")
    except FileNotFoundError:
        pytest.skip("Model not found - run training pipeline first")

    # Test data
    test_input = np.array([[2, 130, 70, 28.5, 45]])

    prediction, probability = predict(model, test_input)

    # Check prediction is 0 or 1
    assert prediction in [0, 1], "Prediction should be 0 or 1"

    # Check probability is between 0 and 1
    assert 0 <= probability <= 1, "Probability should be between 0 and 1"