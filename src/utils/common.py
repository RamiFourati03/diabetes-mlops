# src/utils/common.py
"""
Common utility functions for the diabetes prediction MLOps project.
"""

import yaml
import logging
import os
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations


@ensure_annotations
def get_project_root() -> Path:
    """Get the project root directory

    Returns:
        Path: Project root directory path
    """
    return Path(__file__).parent.parent.parent


@ensure_annotations
def load_config() -> ConfigBox:
    """Load configuration from params.yaml

    Returns:
        ConfigBox: Configuration object
    """
    config_path = get_project_root() / "params.yaml"
    return read_yaml(config_path)


@ensure_annotations
def setup_logging():
    """Setup logging configuration"""
    config = load_config()
    logging.basicConfig(
        level=getattr(logging, config["logging"]["level"]),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config["logging"]["file"]),
            logging.StreamHandler()
        ]
    )


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns ConfigBox object

    Args:
        path_to_yaml (Path): Path to yaml file

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): List of path of directories
        verbose (bool, optional): Whether to print created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"Created directory: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB

    Args:
        path (Path): Path to file

    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"