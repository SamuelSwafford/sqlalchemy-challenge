# Import the dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt
import numpy as np


# Flask Setup
app = Flask(__name__)

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
base = automap_base()

# Reflect the tables
base.prepare(engine, reflect=True)

# Save references to each table
measurement = base.classes.measurement
station = base.classes.station

# Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_ago).all()
    session.close()
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(station.station).all()
    session.close()
    station_list = [station[0] for station in stations]
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    most_active_station = session.query(measurement.station).group_by(measurement.station).order_by(func.count(measurement.station).desc()).first()
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temperature_data = session.query(measurement.tobs).filter(measurement.date >= year_ago, measurement.station == most_active_station[0]).all()
    session.close()
    temperature_list = [temp[0] for temp in temperature_data]
    return jsonify(temperature_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    session = Session(engine)
    if not end:
        results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).all()
    else:
        results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start, measurement.date <= end).all()
    session.close()
    temp_stats = list(np.ravel(results))
    return jsonify(temp_stats)

if __name__ == '__main__':
    app.run(debug=True)
