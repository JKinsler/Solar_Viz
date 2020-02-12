"""Models and database functions for Solar Viz project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class Company(db.Model):
    """Information about companies.
    """

    __tablename__ = "companies"

    company_id = db.Column(db.Integer, autoincrement=True, primary_key=True, 
                    nullable=False)
    name = db.Column(db.String(64), nullable=False)
    company_type = db.Column(db.String(64), nullable=False)
    
    """table relationships """
    consumption = db.relationship('Consumption', backref='consumptions')
    # additional relationship to Company in Program class
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<Company company_id={self.company_id}
                   name={self.name}
                   company_type={self.company_type}>"""


class Program(db.Model):
    """Information per solar project applications.

    Reference: CSI's working data set: 
    https://www.californiasolarstatistics.ca.gov/data_downloads/
    """

    __tablename__ = "programs"

    application_id = db.Column(db.String(25), primary_key=True, nullable=False)
    admin = db.Column(db.Integer,
                         db.ForeignKey('companies.company_id'))
    city = db.Column(db.String(64), nullable=False)
    county = db.Column(db.String(64), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    contractor = db.Column(db.Integer, 
                        db.ForeignKey('companies.company_id')) #should I add nullable = True?
    pv_manuf = db.Column(db.Integer,
                         db.ForeignKey('companies.company_id')) #should I add nullable = True?
    invert_manuf = db.Column(db.Integer,
                         db.ForeignKey('companies.company_id')) #should I add nullable = True?
    status = db.Column(db.String(64), nullable=True)

    """table relationships"""
    company = db.relationship('Company', backref='companies')
    production = db.relationship('Production', backref='productions')

    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<Program application_id={self.application_id}
                   admin={self.admin}
                   city={self.city}
                   county={self.county}
                   zipcode={self.zipcode}
                   contractor={self.contractor}
                   pv_manuf={self.pv_manuf}
                   invert_manuf={self.invert_manuf}
                   status={self.status}>"""


class Production(db.Model):
    """Information about solar energy production per appliction number.

    - 'produced' unit values will be in kWh.
    """

    __tablename__ = "productions"

    production_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    application_id = db.Column(db.Integer,
                         db.ForeignKey('programs.application_id'))
    energy_type = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    produced = db.Column(db.Integer, nullable=False) 

    """table relationships"""
    # additional relationship to Production in Program class


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<Production application_id={self.application_id}
                   energy_type={self.energy_type}
                   start_date={self.start_date}
                   end_date={self.end_date}
                   produced={self.produced}>"""


class Consumption(db.Model):
    """Information about total energy consumption accounted for per utility.

    'consumed' unit values will be in kWh. 
    
    #WHEN SEEDING, NEED TO CONVERT FROM gWh
    """

    __tablename__ = "consumptions"

    consumption_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    utility = db.Column(db.Integer,
                         db.ForeignKey('companies.company_id'))
    year = db.Column(db.String(10), nullable=False)
    consumed = db.Column(db.Integer, nullable=False) 

    """add table relationships here"""

    #relatinship to Consumption in Company class
    
    #ADD REPR here


    ##############################################################################
# Helper functions
"""Took helper functions from ratings lab. Need to understand this code 
better."""

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
