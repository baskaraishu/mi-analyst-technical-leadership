"""
Unit tests for the data quality module.
"""

import pytest
import pandas as pd
from src.data_quality import DataQualityChecker


class TestDataQualityChecker:
    """Test cases for DataQualityChecker class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.checker = DataQualityChecker()
    
    def test_check_empty_response_with_data(self):
        """Test empty check with valid data."""
        df = pd.DataFrame({'col1': [1, 2, 3]})
        result = self.checker.check_empty_response(df)
        assert result is True
    
    def test_check_empty_response_with_empty_df(self):
        """Test empty check with empty DataFrame."""
        df = pd.DataFrame()
        result = self.checker.check_empty_response(df)
        assert result is False
    
    def test_check_empty_response_with_none(self):
        """Test empty check with None."""
        result = self.checker.check_empty_response(None)
        assert result is False
    
    def test_check_minimum_records_pass(self):
        """Test minimum records check passes."""
        df = pd.DataFrame({'col1': [1, 2, 3]})
        result = self.checker.check_minimum_records(df)
        assert result is True
    
    def test_check_null_values_no_nulls(self):
        """Test null check with no null values."""
        df = pd.DataFrame({
            'crypto_id': ['bitcoin', 'ethereum'],
            'symbol': ['BTC', 'ETH'],
            'current_price': [50000, 3000]
        })
        result = self.checker.check_null_values(df, ['crypto_id', 'symbol', 'current_price'])
        assert result is True
    
    def test_check_data_types(self):
        """Test data type validation."""
        df = pd.DataFrame({
            'current_price': [50000.0, 3000.0],
            'market_cap': [1000000000.0, 500000000.0],
            'total_volume': [50000000.0, 20000000.0]
        })
        result = self.checker.check_data_types(df)
        assert result is True
    
    def test_check_value_ranges_positive_prices(self):
        """Test value range check with positive prices."""
        df = pd.DataFrame({
            'current_price': [50000.0, 3000.0],
            'market_cap': [1000000000.0, 500000000.0]
        })
        result = self.checker.check_value_ranges(df)
        assert result is True
    
    def test_check_value_ranges_negative_prices(self):
        """Test value range check with negative prices."""
        df = pd.DataFrame({
            'current_price': [-50000.0, 3000.0],
            'market_cap': [1000000000.0, 500000000.0]
        })
        result = self.checker.check_value_ranges(df)
        assert result is False
