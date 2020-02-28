"""Utility file to seed soalr_viz database from CSI data.

HAVE OPTION TO USE PRODUCTION OR TEST DATA FOR SEEDING.
MUST CHANGE DATABASE ROUTE IN MODEL.PY WHEN SWITCHING BETWEEN THE TWO."""


import csv
from query import check_application_id, get_company_id, get_like_company_id
from sqlalchemy import func
from datetime import datetime
from model import Company, Program, Production, Consumption
from model import connect_to_db, db
from server import app
import timeit

################################################################################
#functions to import data to the model

def clear_tables():
    """Delete data from all tables in the database. 
    Delete in dependancy reverse-order to avoid errors related to foreign key relationships."""

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Consumption.query.delete()
    Production.query.delete()
    Program.query.delete()
    Company.query.delete()

    print('ALL TABLES HAVE BEEN CLEARED OF THEIR DATA')

def inform_tables_loaded():
    """indicate that all functions ran"""

    print('ALL TABLES HAVE BEEN LOADED WITH DATA')


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


def check_date():
    date_today = datetime.now()

    return date_today

#companies #####################################


def load_companies():
    """Load companies information from seed file into the database.
    working code.
    """

    print("Company")

    # opening seed file with the csv library and csv reader. 
    with open('seed_production/WorkingDataSet_2-19-2020.csv') as csv_file:
    # below line will load 'test' seed file
    # with open('seed_test/programs_test_csv.csv') as csv_file:
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
    print(f'Company line_count: {line_count}')

#programs#####################################


def load_programs():
    """Load programs information from seed file into the database.
    working code"""

    print("Program")

    # opening seed file with the csv library and csv reader. 
    with open('seed_production/WorkingDataSet_2-19-2020.csv') as csv_file:
    # below will seed with 'test' data
    # with open('seed_test/programs_test_csv.csv') as csv_file:
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
                utility = get_company_id(utility_name)
                # print(f'utility: {utility}')

                city = row[18]
                county = row[19]
                zipcode = row[21]
                
                #get the contractor id
                contractor_name = row[44]
                c_name = Company.query.filter(Company.name == contractor_name).first()
                contractor = c_name.company_id
                
                #get the pv manuf id
                pv_manuf_name = row[49]
                pv_manuf = get_company_id(pv_manuf_name)
                
                #get the invert manuf id
                invert_manuf_name = row[76]
                invert_manuf = get_company_id(invert_manuf_name)
                
                status = row[106]

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

                line_count+=1

        # Commit our work so it saves to the database
        db.session.commit()

        print(f'Program line_count: {line_count}')


#productions######################################

def load_productions():
    """Load production information from seed file into the database.
    WORKING CODE"""

    print("Production")

    with open('seed_production/MeasuredProduction_2-19-2020.csv') as csv_file:
    # below will seed with 'test' data.
    # with open('seed_test/productions_test_csv.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        date_today = check_date()

        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                application_id = row[0]
                
                #check if the application_id is in the programs table
                id_check = check_application_id(application_id)
                if id_check == True:

                    end_date_string = row[10]
                    produced = row[11]
            
                    # convert date string to date time
                    end_date_format = "%m/%d/%Y"
                    end_date = datetime.strptime(end_date_string, end_date_format)
                    # print(end_date)
                    
                    # print functions for debugging
                    # print(application_id)
                    # print(end_date)
                    # print(produced)
                    
                    # add data from real past dates only
                    if date_today > end_date:
                        production = Production(application_id=application_id,
                                        energy_type = 'solar',
                                        end_date=end_date,
                                        produced=produced,
                                        )
                        # print(production)

                        # Add to the session to the database
                        db.session.add(production)

                    line_count+=1

        # Commit our work so it saves to the database
        db.session.commit()
        print(f'Production line_count: {line_count}')

# consumptions######################################

def load_consumptions():
    """Load consumption information from seed file into the database.
    working code"""

    print("Consumption")

    with open('seed_production/ElectricityByUtility_2-20-2020.csv') as csv_file:
    # below will seed with 'test' data.
    # with open('seed_test/consumptions_test_csv.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                utility_name = row[1]
                utility = get_like_company_id(utility_name)

                year = row[2]
                
                # consumed units must be converted from gWh to kWh
                consumed = int(float(row[10])*1000000)
                # print(f'consumed: {consumed}')
                # print(type(consumed))
                
                consumption = Consumption(utility=utility,
                                year = year,
                                consumed = consumed)
                # print(consumption)

                # Add to the session to the database
                db.session.add(consumption)

                line_count+=1

        # Commit our work so it saves to the database
        db.session.commit()

        print(f'Consumption line_count: {line_count}')


################################################################################
#helper functions for seeding the model

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Run functions
    clear_tables()
    
    #seed data for each table. User timer to see how long it takes.
    start_companies = timeit.default_timer()
    load_companies()
    stop_companies = timeit.default_timer()
    print('Time to seed companies: ', start_companies - stop_companies)

    start_programs = timeit.default_timer()
    load_programs()
    stop_programs = timeit.default_timer()
    print('Time to seed programs: ', start_programs - stop_programs)

    start_productions = timeit.default_timer()
    load_productions()
    stop_productions = timeit.default_timer()
    print('Time to seed productions: ', start_productions - stop_productions)

    start_consumptions = timeit.default_timer()
    load_consumptions()
    stop_consumptions = timeit.default_timer()
    print('Time to seed consumptions: ', start_consumptions - stop_consumptions)

    inform_tables_loaded()



"""
Timer return values are in 'seconds'

Timer data from 'seed_production' files:
ALL TABLES HAVE BEEN CLEARED OF THEIR DATA
Company
Company line_count: 174344
Time to seed companies:  -8.612042455992196
Program
Program line_count: 174344
Time to seed programs:  -1493.2976502100064
Production
Production line_count: 208612
Time to seed productions:  -666.5932022799971
Consumption
Consumption line_count: 88
Time to seed consumptions:  -0.26305283699184656
ALL TABLES HAVE BEEN LOADED WITH DATA




Timer data from 'seed_test' files:
ALL TABLES HAVE BEEN CLEARED OF THEIR DATA
Company
Company line_count: 7
Time to seed companies:  -0.01644753699656576
Program
Program line_count: 7
Time to seed companies:  -0.04395975999068469
Production
Production line_count: 27
Time to seed companies:  -0.10117992598679848
Consumption
Consumption line_count: 24
Time to seed companies:  -0.07823562799603678
ALL TABLES HAVE BEEN LOADED WITH DATA

"""