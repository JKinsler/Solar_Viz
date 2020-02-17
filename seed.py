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

#     print("Company")

#programs#####################################

# def load_programs():
#     """Load programs information from seed file into the database.
#     non-working code"""

#     print("Company")

#productions######################################

def load_productions():
    """Load production information from seed file into the database.
    non-working code"""

    print("Productions")

    # Read productions file 
    for row in open("seed_test/productions_test_csv.csv"):
        row = row.rstrip() #may not need the rstrip but leaving it anyway.
        row = row.split(",")
        #print(row)

        application_id, _, _, _, _, _, _, _, _, _, end_date, produced = row
        # print(application_id)
        # print(end_date)
        # print(produced)

        # user = User(user_id=user_id,
        #             age=age,
        #             zipcode=zipcode)

        # We need to add to the session or it won't ever be stored
        # db.session.add(user)

    # # Once we're done, we should commit our work
    # db.session.commit()

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
    #   UPDATE TO THE CORRECT FUNCTION NAMES
    # load_users()
    # load_movies()
    # load_ratings()
    # set_val_user_id()