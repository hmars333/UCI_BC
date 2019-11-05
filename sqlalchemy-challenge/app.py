import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify



engine = create_engine(":sqlite\\\hawaii.sqlite)

Base= automap_base()

Base.prepare(engine, reflect= True)
Base.classes.keys()

measurement= Base.classes.measurement
station= Base.classes.station

app= Flask(__name__)

@app.route("/")
def Welcome():
    """list all available routes."""
    return(
          f"Available Routes: <br/>"
          f"/apiv1.0/names<br/>"
          f"/api/v1.0/measurement"
          f"/api/v1.0/station"
      )
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Dates and Precipitation Values."""
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-08-24", Measurement.date <= "2017-08-23").\
        all()

    
    precipitation_list = [results]

    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def stations():
    session= Session(engine)
    """List of all Stations"""
    stations= session.query(Station.name, Station.station).all()
    session.close()
    all_stations= list(np.ravel(stations))
    return jsonify(all_stations)

