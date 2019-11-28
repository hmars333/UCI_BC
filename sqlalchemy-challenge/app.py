import datetime as dt 
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#set-up hawaii Database
engine= create_engine("sqlite:///hawaii.sqlite")

#refelct classes and relationships from schema 
Base= automap_base()

#reflect Tables
Base.prepare(engine, reflect= True)

#see tables in DB
Base.classes.keys()

#Save tables as variables
Measurement= Base.classes.measurement
Station= Base.classes.station

#create session to DB
session= Session(engine)

#FLASK#
app= Flask(__name__)

#################################Routes for Page#############################

@app.route("/")
def welcome():
    """All Available Routes."""
    return(
          f"Available Routes: <br/>"
          f"/api/v1.0/precipitation <br/>"
          f"/api/v1.0/stations <br/>"
          f"/api/v1.0/observations<br/>"
          f"/api/v1.0/start<br/>"
          f"/api/v1.0/startend"
)

 ######################################################################################   
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Dates and Precipitation Values."""
#1 year ago from date
    last_year= dt.date(2017, 8, 23) - dt.timedelta(days= 365)

    precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year).all()
    precipitation_list= {date: prcp for date, prcp in precip}
#close session         
    session.close()
#return results
    return jsonify(precipitation_list)


########################################################################################

@app.route("/api/v1.0/stations")
def stations():
    """List of all Stations."""
    stations= session.query(Station.station).all()
#turn array into a list
    all_stations= list(np.ravel(stations))
#close session         
    session.close()
#return results
    return jsonify(all_stations)

########################################################################################

@app.route("/api/v1.0/observations")
def observations():
    last_year= dt.date(2017, 8, 23) - dt.timedelta(days= 365)
# main station obseravtions from previous year
    obs=  session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= last_year).all()
#turn array into list
    temps= list(np.ravel(obs))
#close session         
    session.close()    
    #return results
    return jsonify(temps)
    
########################################################################################
@app.route("/api/v1.0/start")
def start(start=None, end=None):
    """TMIN | TAVG | TMAX"""
    select= [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
#Stats for dates greater than start date
      stats= session.query(select).filter(Measurement.date >= start).all()
#turn array into list
      temps= list(np.ravel(stats))
#close session         
      session.close()
#return results
    return jsonify(temps)

########################################################################################
@app.route("/api/v1.0/startend")
def startend(start=None, end=None):
    """TMIN | TAVG | TMAX"""
#stats with a start/ end date
    end_stats= session.query(select).filter(Measurement.date >=start).filter(Measurement.date <= end).all()
#turn array into list
    temps= list(np.ravel(end_stats))
#close session         
    session.close()
#return results
    return jsonify(temps)


if __name__ == '__main__':
    app.run()

