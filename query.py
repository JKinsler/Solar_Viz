"""Write queries to call from server.py"""

from model import Company, Program, Production, Consumption, connect_to_db, db
from datetime import datetime


################################################################################
#queries to test the databas setup

"""individual database tests"""
def get_production():
    """Return all the objects from the 'productions' table.
    working code"""

    return Production.query.all()


def get_company():
    """Return all the objects from the 'companies' table.
    working code"""

    return Company.query.all()


def get_program():
    """Return all the objects from the 'programs' table.
    working code"""

    return Program.query.all()


def get_consumption():
    """Return all the objects from the 'consumptions' table.
    working code"""

    return Consumption.query.all()



"""field filter queries"""
def get_production_values():
    """Return the solar production value for all companies in all date ranges.
    working code"""

    produced_list = get_production()

    total_production = 0
    # print(f'total_production is: {total_production}')

    for instance in produced_list:
        # print(f'{instance.application_id}, {instance.produced}')
        total_production += instance.produced
        print(f'total_production is: {total_production} kWh, for 3 CSI utilities over all dates')

    return total_production


def get_yearly_production_values():
    """Return the solar production values by year
    Output will be a dictionary with year: production as key value pairs.
    
    Non WORKING CODE

    This is the equivalent psql query:

    SELECT date_part('year', end_date) AS year, SUM(produced) as yearly_production
    FROM productions
    GROUP BY year
    ORDER BY year;

     year | yearly_production
    ------+-------------------
     2007 |            151240
     2011 |             22302
     2014 |               301
     2015 |              6490
     2016 |            103458
     2018 |             62918
     2019 |             18356
    (7 rows)
    

    resource: https://www.postgresqltutorial.com/postgresql-date_part/
    """

    production_by_year = db.session.query(\
                                        extract('year', Production.end_date),\
                                        func.sum(Production.produced)\
                                        .label('total'))\
                                        .group_by(extract('year', Production.end_date)).all()
    
    return production_by_year

def get_consumption_values():
    """Return the energy consumption value for all companies in all date ranges.
    working code"""

    consumed_list = get_consumption()

    total_consumption = 0
    # print(f'total_consumption is: {total_consumption}')

    for instance in consumed_list:
        print(f'{instance.consumption_id}, {instance.consumed}')
        total_consumption += instance.consumed
    
    print(f'total_consumption is: {total_consumption} kWh, for 3 CSI utilities over all dates')

    return total_consumption


def get_percent_solar():
    """returns the percentage energy of solar in production in comparison with total consumption.
    non working code."""

    total_production = get_production_values()
    total_consumption = get_consumption_values()

    percent_solar = total_production / total_consumption

    return percent_solar
    

def get_company(search_company_name):
    """Return the object of a company which is given as an argument.
    working code"""

    return Company.query.filter(Company.name == search_company_name).one()


def get_company_id(search_company_name):
    """Return the id of a company which is given as an argument.
    used in seed.py
    working code"""

    c_name = Company.query.filter(Company.name == search_company_name).first()
    return c_name.company_id


def get_like_company_id(search_company_name):
    """Return the id of a company whose name matches the first 20 characters of 
    the company which is used an an imput parameter.
    used in seed.py
    working code"""

    first_twenty = search_company_name[0:19]+'%'
    # print(f'first_fifteen: {first_twenty}')
    # print(type(first_twenty))

    c_name = Company.query.filter(Company.name.like(first_twenty)).first()
    # print(c_name)
    return c_name.company_id


def check_company_name(company_name):
    """Check whether a comany name is in the company table.
    working code."""

    #look for the value of the application ID in the program table
    name_check = Company.query.filter(Company.company_name == company_name).first()
    if name_check != None:
        return True
    else:
        return False


def check_application_id(application_id):
    """Check whether an application ID is in the programs table.
    Used in seed.py.
    Working code."""

    #look for the value of the application ID in the program table
    id_check = Program.query.filter(Program.application_id == application_id).first()
    if id_check != None:
        return True
    else:
        return False


"""joined load database tests"""
def get_company_application(search_company_name):
    """Return the application id for the company which is input as a parameter.
    working code"""

    applications = Program.query.filter(Company.name == search_company_name)\
                                .options(db.joinedload('utility_company'))\
                                .all()

    return applications

###############################################################################
#helper functions

if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)
