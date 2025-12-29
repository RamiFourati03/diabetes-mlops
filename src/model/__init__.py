# src/model/__init__.py
"""
Machine learning model training and prediction module.
"""

from .model_trainer import train_model, save_model, load_model, predict

__all__ = ["train_model", "save_model", "load_model", "predict"]