# src/data/data_ingestion.py
"""
Data ingestion and validation module for diabetes prediction.
"""

import pandas as pd
import logging
from pathlib import Path
from ..utils.common import load_config
from ..constants import RAW_DATA_FILE, REQUIRED_COLUMNS
from ..exceptions import DataIngestionError, DataValidationError


def download_dataset():
    """
    Download the dataset if it doesn't exist locally

    Returns:
        pd.DataFrame: The downloaded or cached dataset

    Raises:
        DataIngestionError: If data download fails
    """
    logger = logging.getLogger(__name__)
    config = load_config()
    url = config["data"]["url"]

    try:
        if not RAW_DATA_FILE.exists():
            logger.info(f"Downloading dataset from {url}")
            df = pd.read_csv(url)
            RAW_DATA_FILE.parent.mkdir(exist_ok=True)
            df.to_csv(RAW_DATA_FILE, index=False)
            logger.info(f"Dataset saved to {RAW_DATA_FILE}")
            return df
        else:
            logger.info(f"Dataset already exists at {RAW_DATA_FILE}")
            return pd.read_csv(RAW_DATA_FILE)
    except Exception as e:
        logger.error(f"Failed to download or load dataset: {e}")
        raise DataIngestionError(f"Data ingestion failed: {e}")

def ingest_data():
    """
    Ingest data from local file or download if needed

    Returns:
        pd.DataFrame: The ingested dataset
    """
    logger = logging.getLogger(__name__)

    df = download_dataset()
    logger.info(f"Data ingested successfully. Shape: {df.shape}")
    logger.info(f"Columns: {df.columns.tolist()}")
    return df

def validate_data(df):
    """
    Basic data validation

    Args:
        df (pd.DataFrame): Data to validate

    Returns:
        bool: True if validation passes

    Raises:
        DataValidationError: If validation fails
    """
    logger = logging.getLogger(__name__)

    if not all(col in df.columns for col in REQUIRED_COLUMNS):
        missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        logger.error(f"Missing required columns: {missing_cols}")
        raise DataValidationError(f"Missing required columns: {missing_cols}")

    if df.isnull().sum().sum() > 0:
        logger.warning("Data contains missing values")
        # Fill missing values with median for numerical columns
        for col in df.select_dtypes(include=['number']).columns:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].median(), inplace=True)
        logger.info("Missing values filled with median")

    logger.info("Data validation completed")
    return True