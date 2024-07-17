# Dashboard Automobile Sales with Dash-Plotly

## Summary

This project is a dashboard for automobile sales analysis built using Dash and Plotly. It provides interactive visualizations and insights into automobile sales data.

## Features

- Interactive charts and graphs
- Sales trend analysis
- Brand and model comparisons
- Geographic sales distribution

## Development Setup

### Requirements

For development, you'll need __Python 3.9__. To install the development dependencies, run:

<!-- TODO -->
```bash
pip install -r requirements-dev.txt
```

### Running the App Locally

To run the app in development mode:

<!-- TODO -->
```bash
python app.py
```

## Deployment Preparation

The repository has been prepared for deployment with the following modifications:

- Refactored Structure:
  - Data preprocessing and app initialization logic moved into modules
  <!-- TODO -->
  - App initialization separated into app_init.py
- Modified Requirements:
  - requirements.txt compatibility for linux distros for production builds
  - Uses LF (Line Feed) line endings
  - Added *gunicorn* for running the production-grade server
- Production Entry Point:
  - *wsgi.py* as the single entry point for production

To run the app in production using Gunicorn:

```bash
gunicorn wsgi:server
```

## Data Storage

- Using Parquet file format for efficient data storage
- Implemented PyArrow backend for improved performance
