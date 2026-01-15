"""
BigQuery loader module for data persistence.
Handles connection and data loading to Google BigQuery.
"""

import pandas as pd
import logging
from google.cloud import bigquery
from google.oauth2 import service_account
from typing import Optional

from config import Config

logger = logging.getLogger(__name__)


class BigQueryLoader:
    """Handles loading data to Google BigQuery."""
    
    def __init__(self):
        self.project_id = Config.GCP_PROJECT_ID
        self.dataset_id = Config.BQ_DATASET
        self.table_id = Config.BQ_TABLE
        self.credentials_path = Config.GCP_CREDENTIALS_PATH
        self.client = None
        
    def initialize_client(self) -> bool:
        """
        Initialize BigQuery client with credentials.
        
        Returns:
            True if initialization successful, False otherwise
        """
        try:
            if self.credentials_path:
                credentials = service_account.Credentials.from_service_account_file(
                    self.credentials_path
                )
                self.client = bigquery.Client(
                    credentials=credentials,
                    project=self.project_id
                )
            else:
                # Use default credentials (for GitHub Actions with Workload Identity)
                self.client = bigquery.Client(project=self.project_id)
            
            logger.info(f"BigQuery client initialized for project: {self.project_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize BigQuery client: {str(e)}")
            return False
    
    def ensure_dataset_exists(self) -> bool:
        """
        Ensure BigQuery dataset exists, create if not.
        
        Returns:
            True if dataset exists or was created, False otherwise
        """
        try:
            dataset_ref = f"{self.project_id}.{self.dataset_id}"
            
            try:
                self.client.get_dataset(dataset_ref)
                logger.info(f"Dataset {dataset_ref} already exists")
            except Exception:
                # Dataset doesn't exist, create it
                dataset = bigquery.Dataset(dataset_ref)
                dataset.location = "US"
                dataset.description = "Cryptocurrency analytics dataset for MI reporting automation"
                
                self.client.create_dataset(dataset, timeout=30)
                logger.info(f"Created dataset {dataset_ref}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error ensuring dataset exists: {str(e)}")
            return False
    
    def load_data(self, df: pd.DataFrame, write_disposition: str = "WRITE_APPEND") -> bool:
        """
        Load DataFrame to BigQuery table.
        
        Args:
            df: DataFrame to load
            write_disposition: Write mode (WRITE_APPEND, WRITE_TRUNCATE, WRITE_EMPTY)
            
        Returns:
            True if load successful, False otherwise
        """
        if df is None or df.empty:
            logger.warning("Cannot load empty DataFrame to BigQuery")
            return False
        
        try:
            table_ref = f"{self.project_id}.{self.dataset_id}.{self.table_id}"
            
            # Configure job settings
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
                schema_update_options=[
                    bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION
                ]
            )
            
            logger.info(f"Loading {len(df)} records to {table_ref}")
            
            # Load data
            job = self.client.load_table_from_dataframe(
                df, table_ref, job_config=job_config
            )
            
            # Wait for the job to complete
            job.result()
            
            # Get the table to verify load
            table = self.client.get_table(table_ref)
            
            logger.info(f"Successfully loaded {len(df)} records to BigQuery")
            logger.info(f"Table now contains {table.num_rows} total rows")
            
            return True
            
        except Exception as e:
            logger.error(f"Error loading data to BigQuery: {str(e)}")
            return False
    
    def execute_query(self, query: str) -> Optional[pd.DataFrame]:
        """
        Execute a SQL query and return results as DataFrame.
        
        Args:
            query: SQL query string
            
        Returns:
            DataFrame with query results or None if error
        """
        try:
            logger.info("Executing query on BigQuery")
            query_job = self.client.query(query)
            results = query_job.result()
            df = results.to_dataframe()
            
            logger.info(f"Query returned {len(df)} rows")
            return df
            
        except Exception as e:
            logger.error(f"Error executing query: {str(e)}")
            return None
