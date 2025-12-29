# src/exceptions.py
"""
Custom exceptions for the diabetes prediction MLOps project.
"""


class DiabetesMLOpsException(Exception):
    """Base exception for the diabetes MLOps project"""
    pass


class DataIngestionError(DiabetesMLOpsException):
    """Exception raised for data ingestion errors"""
    pass


class DataValidationError(DiabetesMLOpsException):
    """Exception raised for data validation errors"""
    pass


class ModelTrainingError(DiabetesMLOpsException):
    """Exception raised for model training errors"""
    pass


class ModelPredictionError(DiabetesMLOpsException):
    """Exception raised for model prediction errors"""
    pass


class ConfigurationError(DiabetesMLOpsException):
    """Exception raised for configuration errors"""
    pass