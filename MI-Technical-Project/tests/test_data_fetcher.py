"""
Unit tests for the data fetcher module.
"""

import pytest
import pandas as pd
from unittest.mock import Mock, patch
from src.data_fetcher import CryptoDataFetcher


class TestCryptoDataFetcher:
    """Test cases for CryptoDataFetcher class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.fetcher = CryptoDataFetcher()
    
    def test_initialization(self):
        """Test fetcher initialization."""
        assert self.fetcher.base_url is not None
        assert isinstance(self.fetcher.api_key, str)
    
    @patch('src.data_fetcher.requests.get')
    def test_fetch_market_data_success(self, mock_get):
        """Test successful data fetch."""
        # Mock API response
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                'id': 'bitcoin',
                'symbol': 'btc',
                'name': 'Bitcoin',
                'current_price': 50000,
                'market_cap': 1000000000,
            }
        ]
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Execute
        result = self.fetcher.fetch_market_data(['bitcoin'])
        
        # Assert
        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0
    
    @patch('src.data_fetcher.requests.get')
    def test_fetch_market_data_empty_response(self, mock_get):
        """Test handling of empty API response."""
        mock_response = Mock()
        mock_response.json.return_value = []
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        result = self.fetcher.fetch_market_data(['bitcoin'])
        
        assert result is None
    
    def test_transform_data(self):
        """Test data transformation."""
        # Create sample DataFrame
        raw_data = pd.DataFrame({
            'id': ['bitcoin'],
            'symbol': ['btc'],
            'name': ['Bitcoin'],
            'current_price': [50000],
            'market_cap': [1000000000],
        })
        
        # Execute (this will need adjustment based on actual transform logic)
        # result = self.fetcher.transform_data(raw_data)
        
        # Assert
        # assert isinstance(result, pd.DataFrame)
