# tests/test_data_ingestion.py
import pytest
import pandas as pd
from src.data.data_ingestion import ingest_data, validate_data

def test_ingest_data():
    """Test data ingestion"""
    df = ingest_data()

    # Check if dataframe is not empty
    assert not df.empty, "DataFrame should not be empty"

    # Check required columns exist
    required_columns = ["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age", "Outcome"]
    for col in required_columns:
        assert col in df.columns, f"Column {col} should exist"

def test_validate_data():
    """Test data validation"""
    df = ingest_data()
    is_valid = validate_data(df)

    assert is_valid, "Data validation should pass"