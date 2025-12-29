# Makefile - Automation commands for the MLOps project

.PHONY: help install data train test clean lint format

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt
	python setup.py install

data: ## Download and prepare data
	python -m dvc repro data_ingestion

train: ## Train the model
	python main.py

test: ## Run tests
	pytest tests/ -v --cov=src

lint: ## Run linting
	flake8 src/ tests/ --max-line-length=100

format: ## Format code
	black src/ tests/
	isort src/ tests/

clean: ## Clean up generated files
	rm -rf models/*.pkl
	rm -rf logs/*.log
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +

mlflow: ## Start MLflow UI
	mlflow ui --host 0.0.0.0 --port 5000

streamlit: ## Run Streamlit app
	streamlit run streamlit_app/app.py --server.port 8501 --server.address 0.0.0.0

docker-build: ## Build Docker image
	docker build -t diabetes-mlops .

docker-run: ## Run Docker container
	docker run -p 8501:8501 diabetes-mlops

all: install data train test ## Run full pipeline