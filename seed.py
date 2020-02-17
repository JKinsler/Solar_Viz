"""Utility file to seed soalr_viz database from CSI data"""

from sqlalchemy import func
from datetime import datetime
from model import Company, Program, Production, Consumption
from model import connect_to_db, db
from server import app

################################################################################
#functions to import data to the model

#companies #####################################
# def load_companies():
#     """Load companies information from seed file into the database.
#     non-working code."""

"""PSEUDO CODE
use the 'programs_test_csv.csv' as the seed data file
look at columns for: 
- application number
- solar contractor
- pv_manufacturer
- invert_manufacturer

ways to move forward:
1. first alternative: make a dictionary
check if the company name is in the dictionary
if the company is in the dictionary then skip
if the company is not in the dictionary then add

2. second alternative: work directly with the database
check if the company name is already in the database
if it's in the database then skip
if it's not in the database then add

"""
#     print("Company")

#programs#####################################

# def load_programs():
#     """Load programs information from seed file into the database.
#     non-working code"""

#     print("Company")

#productions######################################

def load_productions():
    """Load production information from seed file into the database.
    NON-WORKING CODE
    need to add foreign key values (application_id) to programs table before this will run"""

    print("Productions")

    # Read productions file 
    for row in open("seed_test/productions_test_csv.csv"):
        row = row.rstrip() #may not need the rstrip but leaving it anyway.
        row = row.split(",")
        #print(row)

        application_id, _, _, _, _, _, _, _, _, _, end_date_initial, produced = row
        # print(application_id)
        # print(end_date)
        # print(produced)
        
        #skip the header row
        if application_id != "Application Number":
            
            #format the received end_date_initial to correspond with datetime:
            end_date_format = "%m/%d/%Y"
            end_date = datetime.strptime(end_date_initial, end_date_format)
            print(end_date)

            production = Production(application_id=application_id,
                            energy_type = 'solar',
                            end_date=end_date,
                            produced=produced,
                            )
            print(production)

            # Add to the session to the database
            db.session.add(production)

    # Commit our work so it saves to the database
    db.session.commit()

#consumptions######################################
# def load_consumptions():
#     """Load consumption information from seed file into the database.
#     non-working code"""

#     print("Consumptions")


################################################################################
#helper functions for seeding the model

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    # db.create_all()

    # Import different types of data
    #   UNCOMMENT WHEN SEED.PY IS COMPLETE
    # load_companies()
    # load_programs()
    load_productions()
    # load_consumptions()
