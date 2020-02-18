"""Utility file to seed soalr_viz database from CSI data"""

import csv
from sqlalchemy import func
from datetime import datetime
from model import Company, Program, Production, Consumption
from model import connect_to_db, db
from server import app

################################################################################
#functions to import data to the model

#companies #####################################
def get_utility_name(utility):

    """convert company abbreviations into company names"""
    
    if utility == 'CSE':
        name = 'San Diego Gas and Electric'
   
    elif utility =='PG&E':
        name = 'Pacific Gas and Electric'
    
    elif utility == 'SCE':
        name = 'Southern California Edison'
    
    else:
        name = utility

    return name


def load_companies():
    """Load companies information from seed file into the database.
    non-complete code.
    """

    print("Company")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Company.query.delete()


    # opening seed file with the csv library and csv reader. 
    with open('seed_test/programs_test_csv.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        utility_list = []
        contractor_list = []
        pv_manuf_list = []
        invert_manuf_list = []

        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                utility_abreviation = row[1]
                contractor_company = row[44]
                pv_manuf_company = row[49]
                invert_manuf_company = row[76]

                # print functions for debugging:
                # print(f' LINE COUNT: {line_count}')
                # print(f'{utility_abreviation}')
                # print(f'{contractor_company}')
                # print(f'{pv_manuf_company}')
                # print(f'{invert_manuf}')

                #append companies to the appropriate lists:
                if utility_abreviation not in utility_list:
                    utility_list.append(utility_abreviation)

                if contractor_company not in contractor_list:
                    contractor_list.append(contractor_company)

                if pv_manuf_company not in pv_manuf_list:
                    pv_manuf_list.append(pv_manuf_company)

                if invert_manuf_company not in invert_manuf_list:
                    invert_manuf_list.append(invert_manuf_company)

                # increase the line count by 1
                line_count += 1

        # print funtions for debugging:
        # print(f'utility list: {utility_list}')
        # print(f'contractor_list: {contractor_list}')
        # print(f'pv_manuf_list: {pv_manuf_list}')
        # print(f'invert_manuf_list:{invert_manuf_list}')

        # print(f'Processed {line_count} lines.')

        for utility in utility_list:
            # convert company abbreviations into company names
            
            name = get_utility_name(utility)

            # create instances of the company class to add to the database 
            company = Company(name=name,
                                company_type = 'Utility and Energy Producer')
            # print(company)

            # Add to the session to the database - NEED TO ADD
            db.session.add(company)

        for contractor in contractor_list:
            # create instances of the company class to add to the database 
            company = Company(name=contractor,
                                company_type = 'Solar Contractor')
            # print(company)

            # Add to the session to the database - NEED TO ADD
            db.session.add(company)

        for pv_manuf in pv_manuf_list:
            # create instances of the company class to add to the database 
            company = Company(name=pv_manuf, 
                                company_type = 'photovoltaic manufacture')

            # Add to the session to the database - NEED TO ADD
            db.session.add(company)

        for invert_manuf in invert_manuf_list:
            # create instances of the company class to add to the database 
            company = Company(name=invert_manuf,
                                company_type = 'inverter manufacturer')
            # print(company)

            # Add to the session to the database - NEED TO ADD
            db.session.add(company)

    # Commit our work so it saves to the database
    db.session.commit()


#programs#####################################

def load_programs():
#     """Load programs information from seed file into the database.
#     non-working code"""

    print("Program")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Program.query.delete()


    # opening seed file with the csv library and csv reader. 
    with open('seed_test/programs_test_csv.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #get field values from the csv file
                application_id = row[0]
                
                #get the utility id
                utility_abreviation = row[1]
                #convert utility code to company name
                utility_name = get_utility_name(utility_abreviation)
                c_name = Company.query.filter(Company.name == utility_name).one()
                utility = c_name.company_id
                print(f'utility: {utility}')

                city = row[18]
                county = row[19]
                zipcode = row[21]
                
                #get the contractor id
                contractor_name = row[44]
                c_name = Company.query.filter(Company.name == contractor_name).one()
                contractor = c_name.company_id
                
                #get the pv manuf id
                pv_manuf_name = row[49]
                c_name = Company.query.filter(Company.name == pv_manuf_name).one()
                pv_manuf = c_name.company_id
                
                #get the invert manuf id
                invert_manuf_name = row[76]
                c_name = Company.query.filter(Company.name == invert_manuf_name).one()
                invert_manuf = c_name.company_id
                
                status = row[106]

                # print functions for debugging:
                # print(f' LINE COUNT: {line_count}')
                # print(f'{utility_abreviation}')
                # print(f'{contractor_company}')
                # print(f'{pv_manuf_company}')
                # print(f'{invert_manuf}')

                #add field values to an instance of Program
                program = Program(application_id=application_id, 
                                utility = utility, 
                                city = city, 
                                county = county, 
                                zipcode = zipcode,
                                contractor = contractor, 
                                pv_manuf = pv_manuf, 
                                invert_manuf = invert_manuf, 
                                status = status)

                # add the instance of program to the database
                db.session.add(program)

        # Commit our work so it saves to the database
        db.session.commit()


#productions######################################

# def load_productions():
#     """Load production information from seed file into the database.
#     NON-WORKING CODE
#     need to add foreign key values (application_id) to programs table before this will run"""

#     print("Productions")

#     # Read productions file 
#     for row in open("seed_test/productions_test_csv.csv"):
#         row = row.rstrip() #may not need the rstrip but leaving it anyway.
#         row = row.split(",")
#         #print(row)

#         application_id, _, _, _, _, _, _, _, _, _, end_date_initial, produced = row
#         # print(application_id)
#         # print(end_date)
#         # print(produced)
        
#         #skip the header row
#         if application_id != "Application Number":
            
#             #format the received end_date_initial to correspond with datetime:
#             end_date_format = "%m/%d/%Y"
#             end_date = datetime.strptime(end_date_initial, end_date_format)
#             print(end_date)

#             production = Production(application_id=application_id,
#                             energy_type = 'solar',
#                             end_date=end_date,
#                             produced=produced,
#                             )
#             print(production)

#             # Add to the session to the database
#             db.session.add(production)

#     # Commit our work so it saves to the database
#     db.session.commit()

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
    db.create_all()

    # Import different types of data
    #   UNCOMMENT WHEN SEED.PY IS COMPLETE
    load_companies()
    # load_programs()
    # load_productions()
    # load_consumptions()
