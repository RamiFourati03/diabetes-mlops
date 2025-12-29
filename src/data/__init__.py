# src/data/__init__.py
"""
Data ingestion and validation module for diabetes prediction.
"""

from .data_ingestion import ingest_data, validate_data

__all__ = ["ingest_data", "validate_data"]