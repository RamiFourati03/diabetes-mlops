# src/pipeline/__init__.py
"""
ML pipeline orchestration module.
"""

from .training_pipeline import run_training_pipeline

__all__ = ["run_training_pipeline"]