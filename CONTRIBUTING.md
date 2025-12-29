# Contributing to Diabetes MLOps Project

Thank you for your interest in contributing to the Diabetes MLOps project! This document provides guidelines and information for contributors.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/diabetes-mlops.git
   cd diabetes-mlops
   ```

2. **Set up the development environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   pip install -e .[dev]
   ```

3. **Set up DVC**
   ```bash
   dvc init
   dvc pull  # Pull data and models
   ```

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests and linting**
   ```bash
   # Run tests
   pytest tests/ -v --cov=src

   # Run linting
   flake8 src/ tests/
   black src/ tests/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions small and focused on a single responsibility

## Testing

- Write unit tests for all new functionality
- Aim for at least 80% code coverage
- Use descriptive test names that explain what is being tested
- Mock external dependencies in unit tests

## Documentation

- Update the README.md if you add new features
- Add docstrings to all public functions and classes
- Update type hints as needed

## Commit Message Convention

We follow the [Conventional Commits](https://conventionalcommits.org/) specification:

- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

## Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Get approval from at least one maintainer
4. Squash commits if requested
5. Merge using "Squash and merge"

## Reporting Issues

When reporting bugs or requesting features:

- Use the issue templates provided
- Provide detailed steps to reproduce bugs
- Include relevant error messages and logs
- Specify your environment (OS, Python version, etc.)

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (MIT License).