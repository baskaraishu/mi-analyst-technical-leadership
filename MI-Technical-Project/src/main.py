"""
Main ETL pipeline for Cryptocurrency MI Reporting Automation.
Orchestrates data extraction, quality checks, and loading to BigQuery.
"""

import logging
import sys
import json
from datetime import datetime

from config import Config
from data_fetcher import CryptoDataFetcher
from data_quality import DataQualityChecker
from bigquery_loader import BigQueryLoader

# Configure logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('etl_pipeline.log')
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Main ETL pipeline execution."""
    
    logger.info("=" * 80)
    logger.info("CRYPTOCURRENCY MI REPORTING AUTOMATION - ETL PIPELINE")
    logger.info(f"Execution started at: {datetime.utcnow().isoformat()}")
    logger.info("=" * 80)
    
    pipeline_success = False
    
    try:
        # Validate configuration
        logger.info("Step 1: Validating configuration...")
        Config.validate()
        logger.info("✓ Configuration validated successfully")
        
        # Initialize components
        logger.info("\nStep 2: Initializing components...")
        fetcher = CryptoDataFetcher()
        quality_checker = DataQualityChecker()
        bq_loader = BigQueryLoader()
        logger.info("✓ Components initialized")
        
        # Fetch data from API
        logger.info(f"\nStep 3: Fetching cryptocurrency data...")
        logger.info(f"Tracking: {', '.join(Config.CRYPTO_IDS)}")
        raw_data = fetcher.fetch_market_data(Config.CRYPTO_IDS)
        
        if raw_data is None or raw_data.empty:
            logger.error("✗ Data fetch failed or returned empty results")
            sys.exit(1)
        
        logger.info(f"✓ Fetched {len(raw_data)} records from API")
        
        # Transform data
        logger.info("\nStep 4: Transforming data...")
        transformed_data = fetcher.transform_data(raw_data)
        logger.info(f"✓ Data transformed - Shape: {transformed_data.shape}")
        
        # Run data quality checks
        logger.info("\nStep 5: Running data quality checks...")
        quality_passed, quality_report = quality_checker.run_all_checks(transformed_data)
        
        # Log quality report
        logger.info("\nData Quality Report:")
        logger.info(json.dumps(quality_report, indent=2))
        
        if not quality_passed:
            logger.error("✗ Data quality checks failed - aborting pipeline")
            sys.exit(1)
        
        logger.info("✓ All data quality checks passed")
        
        # Initialize BigQuery client
        logger.info("\nStep 6: Initializing BigQuery connection...")
        if not bq_loader.initialize_client():
            logger.error("✗ Failed to initialize BigQuery client")
            sys.exit(1)
        
        logger.info("✓ BigQuery client initialized")
        
        # Ensure dataset exists
        logger.info("\nStep 7: Ensuring BigQuery dataset exists...")
        if not bq_loader.ensure_dataset_exists():
            logger.error("✗ Failed to ensure dataset exists")
            sys.exit(1)
        
        logger.info("✓ Dataset verified/created")
        
        # Load data to BigQuery
        logger.info("\nStep 8: Loading data to BigQuery...")
        if not bq_loader.load_data(transformed_data, write_disposition="WRITE_APPEND"):
            logger.error("✗ Failed to load data to BigQuery")
            sys.exit(1)
        
        logger.info("✓ Data successfully loaded to BigQuery")
        
        pipeline_success = True
        
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error in pipeline: {str(e)}", exc_info=True)
        sys.exit(1)
    finally:
        logger.info("\n" + "=" * 80)
        if pipeline_success:
            logger.info("ETL PIPELINE COMPLETED SUCCESSFULLY ✓")
        else:
            logger.info("ETL PIPELINE FAILED ✗")
        logger.info(f"Execution ended at: {datetime.utcnow().isoformat()}")
        logger.info("=" * 80)


if __name__ == "__main__":
    main()
