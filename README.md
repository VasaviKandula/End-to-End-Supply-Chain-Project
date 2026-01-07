# End-to-End Supply Chain Data Warehouse

## Project Overview
Built a robust ELT pipeline and Data Warehouse to analyze global sales data, reducing reporting latency from days to seconds. This project simulates a real-world enterprise environment using Python for ingestion, SQL Server for warehousing, and Power BI for executive analytics.

## Architecture
* **Source:** Flat Files (Global Superstore Dataset ~50k rows).
* **Ingestion (Python):** Custom script using Pandas/SQLAlchemy to load raw data into a Staging Layer. Handles schema drift and file validation.
* **Warehousing (SQL Server):** Designed a Star Schema (Gold Layer) with 1 Fact Table and 3 Dimension Tables.
* **Transformation (T-SQL):** Stored Procedures (`LoadDimensions`, `LoadFactSales`) handle data cleaning, deduplication (TRIM), and Surrogate Key management.
* **Visualization (Power BI):** Interactive dashboard featuring Year-over-Year analysis, geospatial mapping, and dynamic KPI tracking.

## Technical Highlights
* **Automated Schema Management:** Python script automatically detects new columns in source files (`if_exists='replace'`).
* **Data Quality Checks:** SQL logic handles NULL handling and string sanitization (TRIM) to ensure 100% referential integrity between Fact and Dimension tables.
* **Performance:** Optimized Star Schema allows for instant filtering of millions of data points without latency.
