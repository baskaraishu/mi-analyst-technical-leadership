-- =====================================================
-- BigQuery Schema: Cryptocurrency Price Data
-- =====================================================
-- Dataset: crypto_analytics
-- Table: crypto_prices
-- Description: Stores historical cryptocurrency market data
--              fetched from CoinGecko API for MI analysis
-- =====================================================

CREATE TABLE IF NOT EXISTS `crypto_analytics.crypto_prices` (
  -- Primary Identifiers
  crypto_id STRING NOT NULL OPTIONS(description="Unique cryptocurrency identifier (e.g., 'bitcoin')"),
  symbol STRING NOT NULL OPTIONS(description="Trading symbol in uppercase (e.g., 'BTC')"),
  name STRING NOT NULL OPTIONS(description="Full name of the cryptocurrency"),
  
  -- Price Metrics
  current_price FLOAT64 OPTIONS(description="Current price in USD"),
  high_24h FLOAT64 OPTIONS(description="Highest price in last 24 hours (USD)"),
  low_24h FLOAT64 OPTIONS(description="Lowest price in last 24 hours (USD)"),
  
  -- Price Changes
  price_change_24h FLOAT64 OPTIONS(description="Absolute price change in last 24 hours (USD)"),
  price_change_percentage_24h FLOAT64 OPTIONS(description="Percentage price change in last 24 hours"),
  price_change_percentage_7d FLOAT64 OPTIONS(description="Percentage price change in last 7 days"),
  
  -- Market Metrics
  market_cap FLOAT64 OPTIONS(description="Total market capitalization (USD)"),
  market_cap_rank INT64 OPTIONS(description="Market cap ranking (1 = highest)"),
  total_volume FLOAT64 OPTIONS(description="24-hour trading volume (USD)"),
  
  -- Supply Metrics
  circulating_supply FLOAT64 OPTIONS(description="Circulating supply of coins/tokens"),
  total_supply FLOAT64 OPTIONS(description="Total supply of coins/tokens"),
  max_supply FLOAT64 OPTIONS(description="Maximum supply cap (NULL if unlimited)"),
  
  -- Historical Extremes
  ath FLOAT64 OPTIONS(description="All-time high price (USD)"),
  ath_date TIMESTAMP OPTIONS(description="Date when all-time high was reached"),
  atl FLOAT64 OPTIONS(description="All-time low price (USD)"),
  atl_date TIMESTAMP OPTIONS(description="Date when all-time low was reached"),
  
  -- Metadata
  last_updated TIMESTAMP OPTIONS(description="Last update timestamp from API"),
  extraction_timestamp TIMESTAMP NOT NULL OPTIONS(description="ETL extraction timestamp (UTC)")
)
PARTITION BY DATE(extraction_timestamp)
CLUSTER BY crypto_id, symbol
OPTIONS(
  description="Cryptocurrency market data for MI reporting and analytics. Data is partitioned by extraction date for optimal query performance.",
  labels=[("department", "analytics"), ("data_source", "coingecko"), ("update_frequency", "daily")]
);

-- =====================================================
-- Create View: Latest Cryptocurrency Prices
-- =====================================================
-- This view provides the most recent price data for each cryptocurrency
-- Useful for dashboards and real-time reporting

CREATE OR REPLACE VIEW `crypto_analytics.v_latest_crypto_prices` AS
SELECT 
  crypto_id,
  symbol,
  name,
  current_price,
  market_cap,
  market_cap_rank,
  total_volume,
  price_change_percentage_24h,
  price_change_percentage_7d,
  circulating_supply,
  last_updated,
  extraction_timestamp
FROM (
  SELECT *,
    ROW_NUMBER() OVER (PARTITION BY crypto_id ORDER BY extraction_timestamp DESC) as rn
  FROM `crypto_analytics.crypto_prices`
)
WHERE rn = 1
ORDER BY market_cap_rank;

-- =====================================================
-- Create View: Daily Price Summary
-- =====================================================
-- Aggregated daily metrics for trend analysis

CREATE OR REPLACE VIEW `crypto_analytics.v_daily_price_summary` AS
SELECT 
  DATE(extraction_timestamp) as date,
  crypto_id,
  symbol,
  name,
  AVG(current_price) as avg_price,
  MIN(low_24h) as daily_low,
  MAX(high_24h) as daily_high,
  AVG(market_cap) as avg_market_cap,
  AVG(total_volume) as avg_volume,
  AVG(price_change_percentage_24h) as avg_24h_change_pct,
  COUNT(*) as data_points
FROM `crypto_analytics.crypto_prices`
GROUP BY date, crypto_id, symbol, name
ORDER BY date DESC, avg_market_cap DESC;

-- =====================================================
-- Indexes and Optimization
-- =====================================================
-- Note: BigQuery automatically optimizes queries using clustering
-- The table is already clustered by crypto_id and symbol for efficient filtering

-- =====================================================
-- Data Quality Checks (Example Queries)
-- =====================================================

-- Check for NULL values in critical columns
-- SELECT 
--   COUNTIF(crypto_id IS NULL) as null_crypto_id,
--   COUNTIF(current_price IS NULL) as null_current_price,
--   COUNTIF(market_cap IS NULL) as null_market_cap
-- FROM `crypto_analytics.crypto_prices`
-- WHERE DATE(extraction_timestamp) = CURRENT_DATE();

-- Check for duplicate records
-- SELECT 
--   crypto_id, 
--   extraction_timestamp, 
--   COUNT(*) as duplicate_count
-- FROM `crypto_analytics.crypto_prices`
-- GROUP BY crypto_id, extraction_timestamp
-- HAVING COUNT(*) > 1;

-- Check daily data completeness
-- SELECT 
--   DATE(extraction_timestamp) as date,
--   COUNT(DISTINCT crypto_id) as unique_cryptos,
--   COUNT(*) as total_records
-- FROM `crypto_analytics.crypto_prices`
-- GROUP BY date
-- ORDER BY date DESC
-- LIMIT 30;
