# Additional SQL Queries for Analytics

This directory contains useful SQL queries for analyzing cryptocurrency data in BigQuery.

## Sample Analytical Queries

### Market Performance Analysis

```sql
-- Top 10 cryptocurrencies by market cap
SELECT 
  name,
  symbol,
  current_price,
  market_cap,
  market_cap_rank,
  price_change_percentage_24h
FROM `crypto_analytics.v_latest_crypto_prices`
ORDER BY market_cap_rank
LIMIT 10;
```

### Price Volatility Analysis

```sql
-- Calculate 7-day price volatility
SELECT 
  crypto_id,
  name,
  STDDEV(current_price) as price_volatility,
  AVG(current_price) as avg_price,
  (STDDEV(current_price) / AVG(current_price)) * 100 as volatility_coefficient
FROM `crypto_analytics.crypto_prices`
WHERE extraction_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
GROUP BY crypto_id, name
ORDER BY volatility_coefficient DESC;
```

### Volume Analysis

```sql
-- Average daily trading volume by cryptocurrency
SELECT 
  crypto_id,
  name,
  DATE(extraction_timestamp) as date,
  AVG(total_volume) as avg_daily_volume,
  MAX(total_volume) as max_daily_volume
FROM `crypto_analytics.crypto_prices`
WHERE extraction_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY crypto_id, name, date
ORDER BY date DESC, avg_daily_volume DESC;
```
