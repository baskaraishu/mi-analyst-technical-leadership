# Testing Configuration

This directory contains unit tests and test fixtures for the MI Reporting Automation Engine.

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_data_quality.py
```

## Test Structure

- `test_data_fetcher.py` - Tests for API data fetching
- `test_data_quality.py` - Tests for data quality validation
- `test_bigquery_loader.py` - Tests for BigQuery integration (to be added)
- `test_config.py` - Tests for configuration management (to be added)

## Writing Tests

Follow these guidelines when writing tests:

1. Use descriptive test names that explain what is being tested
2. Follow the Arrange-Act-Assert pattern
3. Mock external dependencies (API calls, database connections)
4. Test both success and failure scenarios
5. Aim for high code coverage (>80%)

## Test Fixtures

Create reusable test fixtures in `conftest.py` for common test data.
