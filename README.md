# 🩺 Diabetes Prediction - Professional MLOps Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![MLflow](https://img.shields.io/badge/MLflow-2.8+-green.svg)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

A professional MLOps implementation for diabetes prediction using machine learning, featuring automated pipelines, model tracking, and a modern Streamlit web interface.

## 🎯 Project Overview

This project demonstrates industry-standard MLOps practices for building, deploying, and monitoring a diabetes prediction model. It uses the Pima Indians Diabetes Dataset to predict diabetes risk based on health metrics.

### ✨ Key Features

- **Modular Architecture**: Clean separation of data, model, and pipeline components
- **MLflow Integration**: Complete experiment tracking and model versioning
- **Streamlit UI**: Interactive web interface for real-time predictions
- **Automated Testing**: Comprehensive test suite with pytest
- **Containerization**: Docker and Docker Compose support
- **Professional Logging**: Structured logging throughout the application
- **Configuration Management**: YAML-based configuration system

## 🏗️ Architecture

```
diabetes-prediction-mlops/
├── src/                          # Source code
│   ├── data/                     # Data ingestion and validation
│   ├── model/                    # Model training and prediction
│   ├── pipeline/                 # ML pipelines
│   └── utils/                    # Utility functions
├── streamlit_app/                # Streamlit web application
├── config/                       # Configuration files
├── research/                     # Jupyter notebooks for exploration
├── tests/                        # Unit tests
├── models/                       # Saved models
├── logs/                         # Application logs
├── params.yaml                   # Configuration parameters
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── Dockerfile                    # Docker configuration
├── docker-compose.yml           # Multi-container setup
└── README.md
``

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Docker (optional)
- Docker Compose (optional)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd diabetes-prediction-mlops

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
python setup.py install
```

### 2. Train the Model

```bash
# Run the training pipeline
python main.py
```

This will:
- Download and validate the dataset
- Train a Random Forest model
- Log experiments and metrics with MLflow
- Save the model to `models/diabetes_model.pkl`

### 3. Launch MLflow UI (Optional)

```bash
# Start MLflow tracking server
mlflow ui
```

Visit `http://localhost:5000` to view experiments and model metrics.

### 4. Run the Streamlit App

```bash
# Method 1: Direct run
streamlit run streamlit_app/app.py

# Method 2: Using the runner script
python streamlit_app/run_app.py
```

Visit `http://localhost:8501` to access the web interface.

### 5. Run Tests

```bash
pytest tests/
```

## 🐳 Docker Deployment

### Single Container

```bash
# Build and run
docker build -t diabetes-mlops .
docker run -p 8501:8501 diabetes-mlops
```

### Multi-Container (with MLflow)

```bash
# Build and run all services
docker-compose up --build
```

This starts:
- Streamlit app on `http://localhost:8501`
- MLflow server on `http://localhost:5000`

## 📊 Usage

### Web Interface

1. Open the Streamlit app in your browser
2. Enter patient health metrics:
   - Pregnancies
   - Glucose level
   - Blood pressure
   - BMI
   - Age
3. Click "Predict Diabetes Risk"
4. View prediction results with confidence scores

### API Usage (Programmatic)

```python
from src.model.model_trainer import load_model, predict
import numpy as np

# Load model
model = load_model()

# Make prediction
input_data = np.array([[2, 130, 70, 28.5, 45]])  # Sample input
prediction, probability = predict(model, input_data)

print(f"Prediction: {'Diabetic' if prediction else 'Not Diabetic'}")
print(f"Confidence: {probability:.2%}")
```

## 🔧 Configuration

All configuration is managed through `params.yaml`:

```yaml
data:
  url: "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
  test_size: 0.2
  random_state: 42

model:
  name: "RandomForest"
  params:
    n_estimators: 100
    random_state: 42
    max_depth: 10

mlflow:
  experiment_name: "Diabetes_Prediction_Experiment"
  tracking_uri: "http://localhost:5000"
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_data_ingestion.py
```

## 📈 Model Performance

The Random Forest model achieves:
- **Accuracy**: ~85%
- **Precision**: ~82%
- **Recall**: ~78%
- **F1-Score**: ~80%
- **ROC-AUC**: ~88%

*Note: Performance may vary based on random seed and data splits.*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Pima Indians Diabetes Dataset
- Scikit-learn, Streamlit, and MLflow communities
- MLOps best practices from the industry

---

**Built with ❤️ for learning and demonstrating professional MLOps practices**

```
python train.py
```

## Run the API Locally

```
uvicorn main:app --reload
```

### Sample Input for /predict

```
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "BMI": 28.5,
  "Age": 45
}
```

## Dockerize the API

### Build the Docker Image

```
docker build -t diabetes-prediction-model .
```

### Run the Container

```
docker run -p 8000:8000 diabetes-prediction-model
```

## Deploy to Kubernetes

```
kubectl apply -f diabetes-prediction-model-deployment.yaml
```

🙌 Credits

Created by `Rami Fourati`


