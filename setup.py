# setup.py
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="diabetes-prediction-mlops",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Professional MLOps project for diabetes prediction with Streamlit UI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/diabetes-prediction-mlops",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "scikit-learn>=1.3.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "joblib>=1.3.0",
        "mlflow>=2.8.0",
        "pyyaml>=6.0",
        "streamlit>=1.28.0",
        "python-box>=7.0",
        "ensure>=1.0.0",
    ],
)