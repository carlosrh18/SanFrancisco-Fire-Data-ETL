# Fire Incidents Pipeline

## Overview

This project builds a pipeline to extract, clean, and load San Francisco Fire Incident data into a local PostgreSQL database for analysis.

## Setup

1. Run Docker:
   ```bash
   docker-compose up -d
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run pipeline:
   ```bash
   python etl/extract.py
   python etl/transform.py
   python etl/load.py
   ```

4. Query database or use dbt to generate reports.

## Notes
- Deduplicates by `Incident Number`
- Aggregates by battalion and time (weekly)