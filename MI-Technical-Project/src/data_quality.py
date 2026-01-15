"""
Data Quality module for validation and quality checks.
Ensures data integrity before loading to BigQuery.
"""

import pandas as pd
import logging
from typing import Dict, List, Tuple

from config import Config

logger = logging.getLogger(__name__)


class DataQualityChecker:
    """Performs data quality checks on cryptocurrency data."""
    
    def __init__(self):
        self.min_records = Config.MIN_RECORDS_THRESHOLD
        self.max_null_pct = Config.MAX_NULL_PERCENTAGE
        self.quality_report = {}
        
    def check_empty_response(self, df: pd.DataFrame) -> bool:
        """
        Check if DataFrame is empty.
        
        Args:
            df: DataFrame to check
            
        Returns:
            True if validation passes, False otherwise
        """
        if df is None or df.empty:
            logger.error("Data Quality FAILED: Empty DataFrame received")
            self.quality_report['empty_check'] = 'FAILED'
            return False
        
        logger.info(f"Data Quality PASSED: Empty check - {len(df)} records found")
        self.quality_report['empty_check'] = 'PASSED'
        self.quality_report['record_count'] = len(df)
        return True
    
    def check_minimum_records(self, df: pd.DataFrame) -> bool:
        """
        Check if DataFrame meets minimum record threshold.
        
        Args:
            df: DataFrame to check
            
        Returns:
            True if validation passes, False otherwise
        """
        record_count = len(df)
        
        if record_count < self.min_records:
            logger.error(f"Data Quality FAILED: Only {record_count} records, minimum required: {self.min_records}")
            self.quality_report['min_records_check'] = 'FAILED'
            return False
        
        logger.info(f"Data Quality PASSED: Minimum records check - {record_count} records")
        self.quality_report['min_records_check'] = 'PASSED'
        return True
    
    def check_null_values(self, df: pd.DataFrame, critical_columns: List[str]) -> bool:
        """
        Check null values in critical columns.
        
        Args:
            df: DataFrame to check
            critical_columns: List of column names that cannot have nulls
            
        Returns:
            True if validation passes, False otherwise
        """
        null_report = {}
        has_failures = False
        
        for col in critical_columns:
            if col in df.columns:
                null_count = df[col].isnull().sum()
                null_pct = (null_count / len(df)) * 100
                null_report[col] = {
                    'null_count': null_count,
                    'null_percentage': round(null_pct, 2)
                }
                
                if null_pct > self.max_null_pct:
                    logger.error(f"Data Quality FAILED: Column '{col}' has {null_pct:.2f}% null values (threshold: {self.max_null_pct}%)")
                    has_failures = True
        
        self.quality_report['null_values'] = null_report
        
        if has_failures:
            self.quality_report['null_check'] = 'FAILED'
            return False
        
        logger.info("Data Quality PASSED: Null values check")
        self.quality_report['null_check'] = 'PASSED'
        return True
    
    def check_data_types(self, df: pd.DataFrame) -> bool:
        """
        Validate data types for key columns.
        
        Args:
            df: DataFrame to check
            
        Returns:
            True if validation passes, False otherwise
        """
        type_checks = {
            'current_price': ['float64', 'float32', 'int64'],
            'market_cap': ['float64', 'float32', 'int64'],
            'total_volume': ['float64', 'float32', 'int64'],
        }
        
        has_failures = False
        
        for col, valid_types in type_checks.items():
            if col in df.columns:
                if df[col].dtype.name not in valid_types:
                    logger.error(f"Data Quality FAILED: Column '{col}' has invalid type '{df[col].dtype}'")
                    has_failures = True
        
        if has_failures:
            self.quality_report['datatype_check'] = 'FAILED'
            return False
        
        logger.info("Data Quality PASSED: Data types check")
        self.quality_report['datatype_check'] = 'PASSED'
        return True
    
    def check_value_ranges(self, df: pd.DataFrame) -> bool:
        """
        Check if values are within expected ranges.
        
        Args:
            df: DataFrame to check
            
        Returns:
            True if validation passes, False otherwise
        """
        has_failures = False
        
        # Price should be positive
        if 'current_price' in df.columns:
            negative_prices = df[df['current_price'] < 0]
            if len(negative_prices) > 0:
                logger.error(f"Data Quality FAILED: Found {len(negative_prices)} records with negative prices")
                has_failures = True
        
        # Market cap should be positive
        if 'market_cap' in df.columns:
            negative_mcap = df[df['market_cap'] < 0]
            if len(negative_mcap) > 0:
                logger.error(f"Data Quality FAILED: Found {len(negative_mcap)} records with negative market cap")
                has_failures = True
        
        if has_failures:
            self.quality_report['range_check'] = 'FAILED'
            return False
        
        logger.info("Data Quality PASSED: Value ranges check")
        self.quality_report['range_check'] = 'PASSED'
        return True
    
    def run_all_checks(self, df: pd.DataFrame) -> Tuple[bool, Dict]:
        """
        Run all data quality checks.
        
        Args:
            df: DataFrame to validate
            
        Returns:
            Tuple of (validation_passed, quality_report)
        """
        logger.info("=" * 60)
        logger.info("STARTING DATA QUALITY CHECKS")
        logger.info("=" * 60)
        
        critical_columns = ['crypto_id', 'symbol', 'name', 'current_price']
        
        checks = [
            self.check_empty_response(df),
            self.check_minimum_records(df) if df is not None and not df.empty else False,
            self.check_null_values(df, critical_columns) if df is not None and not df.empty else False,
            self.check_data_types(df) if df is not None and not df.empty else False,
            self.check_value_ranges(df) if df is not None and not df.empty else False,
        ]
        
        all_passed = all(checks)
        
        logger.info("=" * 60)
        if all_passed:
            logger.info("DATA QUALITY: ALL CHECKS PASSED ✓")
        else:
            logger.error("DATA QUALITY: SOME CHECKS FAILED ✗")
        logger.info("=" * 60)
        
        self.quality_report['overall_status'] = 'PASSED' if all_passed else 'FAILED'
        
        return all_passed, self.quality_report
