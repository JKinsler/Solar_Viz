"""Models and database functions for Solar Viz project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class Program(db.Model):
    """Information per solar project applications.

    Reference: CSI's working data set: 
    https://www.californiasolarstatistics.ca.gov/data_downloads/
    """

    __tablename__ = "programs"

    application_id = db.Column(db.String(25), primary_key=True, nullable=False)
    admin = db.Column(db.Column(db.Integer,
                         db.ForeignKey('companies.company_id')))
    city = db.Column(db.String(64), nullable=False)
    county = db.Column(db.String(64), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    contractor = db.Column(db.Column(db.Integer,
                         db.ForeignKey('companies.company_id'))) 
    pv_manuf = db.Column(db.Column(db.Integer,
                         db.ForeignKey('companies.company_id'))) 
    invert_manuf = db.Column(db.Column(db.Integer,
                         db.ForeignKey('companies.company_id'))) 
    status = db.Column(db.String(64), nullable=True)

    #ADD RELATIONSHIP DESCRIPTORS HERE

    #ADD REPR HERE


class Company(db.Model):
    """Information about companies.
    """

    __tablename__ = "companies"

    company_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    company_type = db.Column(db.String(64), nullable=False)
    
    #ADD RELATIONSHIP DESCRIPTORS HERE

    #ADD REPR here


class Production(db.Model):
    """Information about solar energy production per appliction number.

    - amount unit values will be in kWh.
    """

    __tablename__ = "productions"

    production_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    application_id = db.Column(db.Column(db.Integer,
                         db.ForeignKey('programs.application_id')))
    energy_type = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    produced = db.Column(db.Integer, nullable=False) 

    #ADD RELATIONSHIP DESCRIPTORS HERE
    #ADD REPR here


class Consumption(db.Model):
    """Information about solar energy production per appliction number.

    - amount unit values will be in kWh. 
    #WHEN SEEDING, NEED TO CONVERT FROM KWH
    """

    __tablename__ = "consumptions"

    consumption_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    utility = db.Column(db.Column(db.Integer,
                         db.ForeignKey('companies.company_id')))
    year = db.Column(db.String(10), nullable=False)
    consumed = db.Column(db.Integer, nullable=False) 

    #ADD RELATIONSHIP DESCRIPTORS HERE
    #ADD REPR here