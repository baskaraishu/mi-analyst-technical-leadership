"""
Data fetcher module for cryptocurrency price data.
Handles API requests to CoinGecko and data transformation.
"""

import requests
import pandas as pd
from datetime import datetime
import logging
from typing import Dict, List, Optional

from config import Config

logger = logging.getLogger(__name__)


class CryptoDataFetcher:
    """Fetches cryptocurrency data from CoinGecko API."""
    
    def __init__(self):
        self.base_url = Config.COINGECKO_API_URL
        self.api_key = Config.COINGECKO_API_KEY
        
    def fetch_market_data(self, crypto_ids: List[str]) -> Optional[pd.DataFrame]:
        """
        Fetch market data for specified cryptocurrencies.
        
        Args:
            crypto_ids: List of cryptocurrency IDs (e.g., ['bitcoin', 'ethereum'])
            
        Returns:
            DataFrame with cryptocurrency market data or None if request fails
        """
        endpoint = f"{self.base_url}/coins/markets"
        
        params = {
            "vs_currency": "usd",
            "ids": ",".join(crypto_ids),
            "order": "market_cap_desc",
            "per_page": 250,
            "page": 1,
            "sparkline": False,
            "price_change_percentage": "24h,7d"
        }
        
        # Add API key header if available
        headers = {}
        if self.api_key:
            headers["x-cg-demo-api-key"] = self.api_key
        
        try:
            logger.info(f"Fetching data for cryptocurrencies: {', '.join(crypto_ids)}")
            response = requests.get(endpoint, params=params, headers=headers, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if not data:
                logger.warning("API returned empty response")
                return None
            
            # Transform to DataFrame
            df = pd.DataFrame(data)
            
            # Add extraction timestamp
            df['extraction_timestamp'] = datetime.utcnow()
            
            logger.info(f"Successfully fetched {len(df)} records")
            return df
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from CoinGecko: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error during data fetch: {str(e)}")
            return None
    
    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform raw API data to match BigQuery schema.
        
        Args:
            df: Raw DataFrame from API
            
        Returns:
            Transformed DataFrame
        """
        if df is None or df.empty:
            return pd.DataFrame()
        
        # Select and rename columns to match schema
        transformed_df = pd.DataFrame({
            'crypto_id': df['id'],
            'symbol': df['symbol'].str.upper(),
            'name': df['name'],
            'current_price': df['current_price'],
            'market_cap': df['market_cap'],
            'market_cap_rank': df['market_cap_rank'],
            'total_volume': df['total_volume'],
            'high_24h': df['high_24h'],
            'low_24h': df['low_24h'],
            'price_change_24h': df['price_change_24h'],
            'price_change_percentage_24h': df['price_change_percentage_24h'],
            'price_change_percentage_7d': df.get('price_change_percentage_7d_in_currency'),
            'circulating_supply': df['circulating_supply'],
            'total_supply': df['total_supply'],
            'max_supply': df['max_supply'],
            'ath': df['ath'],
            'ath_date': pd.to_datetime(df['ath_date']),
            'atl': df['atl'],
            'atl_date': pd.to_datetime(df['atl_date']),
            'last_updated': pd.to_datetime(df['last_updated']),
            'extraction_timestamp': df['extraction_timestamp']
        })
        
        logger.info(f"Transformed {len(transformed_df)} records")
        return transformed_df
