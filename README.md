# sqlalchemy-challenge

## Overview
This project conducts a climate analysis and data exploration of a climate database for Honolulu, Hawaii. The analysis is done using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. Additionally, a Flask API is developed to present the results.

## Contents
- `climate_starter.ipynb`: Jupyter notebook containing the climate analysis and data exploration.
- `app.py`: Flask application providing a series of API endpoints related to the climate analysis.
- `Resources/`: Directory containing the `hawaii.sqlite` database and CSV data files.

## Climate Analysis and Exploration
The analysis includes:
- Precipitation Analysis: Analysis of the last 12 months of precipitation data.
- Station Analysis: Analysis of weather station data, including temperature observations.

## Flask API
The Flask API includes the following routes:
- `/`: Home page listing all available routes.
- `/api/v1.0/precipitation`: JSON representation of the last year's precipitation data.
- `/api/v1.0/stations`: JSON list of weather stations.
- `/api/v1.0/tobs`: JSON list of Temperature Observations (TOBS) for the previous year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: JSON list of the minimum, average, and maximum temperatures for a given date range.

## How to Run
1. To run the Jupyter notebook, navigate to the `SurfsUp` folder and open `climate_starter.ipynb`.
2. To start the Flask API, run `python app.py` from within the `SurfsUp` folder.

## Dependencies
- Python
- Flask
- SQLAlchemy
- Pandas
- Matplotlib

## Data Sources
- `hawaii.sqlite`: SQLite database containing climate data for Honolulu, Hawaii.
- `hawaii_stations.csv`: CSV file containing weather station data.
- `hawaii_measurements.csv`: CSV file containing climate measurements.

## Author
Samuel Swafford
