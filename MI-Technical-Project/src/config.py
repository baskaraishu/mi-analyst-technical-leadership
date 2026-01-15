"""
Configuration module for the MI Reporting Automation Engine.
Handles environment variables and application settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for application settings."""
    
    # API Configuration
    COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
    COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", "")  # Optional for free tier
    
    # BigQuery Configuration
    GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
    BQ_DATASET = os.getenv("BQ_DATASET", "crypto_analytics")
    BQ_TABLE = os.getenv("BQ_TABLE", "crypto_prices")
    GCP_CREDENTIALS_PATH = os.getenv("GCP_CREDENTIALS_PATH")
    
    # Data Quality Thresholds
    MIN_RECORDS_THRESHOLD = int(os.getenv("MIN_RECORDS_THRESHOLD", "1"))
    MAX_NULL_PERCENTAGE = float(os.getenv("MAX_NULL_PERCENTAGE", "10.0"))
    
    # Cryptocurrencies to track
    CRYPTO_IDS = os.getenv("CRYPTO_IDS", "bitcoin,ethereum,cardano,solana,polkadot").split(",")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls):
        """Validate required configuration parameters."""
        missing_vars = []
        
        if not cls.GCP_PROJECT_ID:
            missing_vars.append("GCP_PROJECT_ID")
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
