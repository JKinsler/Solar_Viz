"""Write queries to call from server.py"""

from model import Company, Program, Production, Consumption, connect_to_db, db
from datetime import datetime
from datetime import timedelta
from sqlalchemy import extract, func
import json



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


def get_production_by_year():
    """Return the solar production values by year
    
    Output will be a list of years and production values in kWh

    used in server.py

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
    
    Tests from solar_viz_test database
    Examples: 
        >>> get_production_by_year()
        [(2007.0, Decimal('151240')), (2011.0, Decimal('22302')), (2014.0, Decimal('301')), (2015.0, Decimal('6490')), (2016.0, Decimal('103458')), (2018.0, Decimal('62918')), (2019.0, Decimal('18356'))]
    """

    production_by_year = db.session.query(\
                                        extract('year', Production.end_date),\
                                        func.sum(Production.produced)\
                                        .label('total'))\
                                        .group_by(extract('year', Production.end_date))\
                                        .order_by(extract('year', Production.end_date))\
                                        .all()
    



    # format the output of the query into a dictionary
    # CAUTION - may need to change int to big int after seeding production database
    
    return production_by_year


def get_production_years():
    """Return all years of solar energy production from the database.
    Used in server.py"""

    production_by_year = get_production_by_year()

    years = []
    for year in production_by_year:
        years.append(str(int(year[0])))

    return years


def format_production_for_table():
    """Returns a dictionary with key value pairs as 'year':'production'.
    
    Output: dictionary
        - key types are 'int'
        - value types are 'int', kWh
   
    Used in server.py

    (tests from 'solar_viz_test' database)
    Examples:
        >>> format_production_for_table()
        {2007: 151240, 2011: 22302, 2014: 301, 2015: 6490, 2016: 103458, 2018: 62918, 2019: 18356}
    """

    production_by_year = get_production_by_year()

    production_by_year_dict = {}
    for year in production_by_year:
        production_by_year_dict[int(year[0])] = int(year[1])

    return production_by_year_dict


def convert_date_to_iso(date_year):
    """Convert a 4-digit year iso standard date, which is required
    for chartjs
    This function takes the argument date_year as a string parameter.

    (test from 'solar_viz_test' database)
    Example:
        >>> convert_date_to_iso('2016')
        '2016-01-01T00:00:00'
        >>>
    """

    date_year = str(date_year)
    year_format = "%Y"
    date_year_datetime = datetime.strptime(date_year, year_format)
    
    return date_year_datetime.isoformat()


def format_production_for_chartjs():
    """Re-format get_production_by_year output so it's compatible with chartjs
    and javascript.

    Example (from solar_viz_test database):

    format_production_for_chartjs()
    (['2007-01-01T00:00:00', '2011-01-01T00:00:00', '2014-01-01T00:00:00', '2015-01-01T00:00:00', '2016-01-01T00:00:00', '2018-01-01T00:00:00', '2019-01-01T00:00:00'], 
    [{'x': '2007-01-01T00:00:00', 'y': 151.24}, {'x': '2011-01-01T00:00:00', 'y': 22.302}, 
    {'x': '2014-01-01T00:00:00', 'y': 0.301}, {'x': '2015-01-01T00:00:00', 'y': 6.49}, 
    {'x': '2016-01-01T00:00:00', 'y': 103.458}, {'x': '2018-01-01T00:00:00', 'y': 62.918}, 
    {'x': '2019-01-01T00:00:00', 'y': 18.356}])
    
    used by server.py    
    """

    production_by_year = get_production_by_year()

    production_datasets = []
    yearly_labels = []
    for year in production_by_year:
        # year_date = 
        # year_end_date = 
        yearly_labels.append(convert_date_to_iso(str(int(year[0]))))
        
        yearly_dataset = {}
        yearly_dataset["x"] = convert_date_to_iso(str(int(year[0])))
        yearly_dataset["y"] = float(year[1]/1000)
        production_datasets.append(yearly_dataset)

    # yearly_labels_json = json.dumps(yearly_labels)
    # production_datasets_json = json.dumps(production_datasets)

    return yearly_labels, production_datasets


def get_production_for_year(year):
    """Return the amount of energy produced from a particular year.
    Input 'year' is taken as a string or int
    Output will be production, as an int
    
    WORKING CODE

    used in server.py

    Example 1: (from 'solar_viz_test' database):
    >>> print(get_production_for_year('2016'))
    103458

    Example 2:
    >>> print(get_production_for_year(2016))
    103458

    Example 3:
    >>> print(get_production_for_year(1990))
    None

    """
    year_int = int(year)
    production_by_year_dict = format_production_for_table()
    
    if year_int in production_by_year_dict:
        production = float(production_by_year_dict[year_int])/1000
        return production
    else:
        return None


def get_production_change(year):
    """Return the factor of change in production since the previous year

    Input: Year can be entered as an int or string
    Output: change factor will be a float with one decimal place
    """
    
    year = int(year)
    previous_year = year - 1
    year_production = get_production_for_year(year)
    print(year_production)
    previous_year_production = get_production_for_year(previous_year)
    print(previous_year_production)
    
    if previous_year_production:
        change_factor = round((year_production/previous_year_production), 1)
        print(change_factor)
        change_factor = str(change_factor) + " X"
    
        return change_factor

    else:
        return 'cannot be calculated'


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


def get_consumption_by_year():
    """Return the energy consumption value for the year which is given as an input.

    Output: list of tuples that contain (year, consumed)
    'year' is returned as str
    'consumed' is returned as Decimal

    working code

    used by query.py

    Example (from 'solar_viz_test' database):
    print(get_consumption_by_year())
    [('2003', Decimal('82187501000')), ('2004', Decimal('165991784420')), 
    ('2005', Decimal('168176982210')), ('2006', Decimal('173128734110')), 
    ('2007', Decimal('195208993470')), ('2008', Decimal('197699316250')), 
    ('2009', Decimal('106050234170')), ('2010', Decimal('102752303400')), 
    ('2011', Decimal('103375578300')), ('2012', Decimal('20107762330')), 
    ('2013', Decimal('19908245100')), ('2014', Decimal('20166788140')), 
    ('2015', Decimal('19767120550'))]

    """

    all_consumption = db.session.query(Consumption.year.label('year'), 
                                        func.sum(Consumption.consumed).label('total'))\
                                        .group_by(Consumption.year)\
                                        .order_by(Consumption.year)\
                                        .all()
    return all_consumption


def get_consumption_for_utility_in_year(search_company_name, search_year):
    """Return the energy consumption value for a utility company, in year 
    which is given as an input.

    Input: 
        - utilities, as a list
        - year, as an int or string
    Output: 
        - utility name
        - consumption as a float, in kWh
    
    Example (from 'solar_viz_test' database):
    >>> get_consumption_for_utility_in_year('Pacific Gas and Electric', 2007)
    [(86078891490, '2007', 'Pacific Gas and Electric')]
    
    used by server.py
    """
    search_year = str(search_year) 

    company_consumption = db.session.query(Consumption.consumed, Consumption.year, Company.name)\
                                    .join(Company, Consumption.utility == Company.company_id)\
                                    .filter(Company.name == search_company_name)\
                                    .filter(Consumption.year == search_year)\
                                    .all()
    return company_consumption


def get_utilities_consumption_in_year(search_year):
    """Return a list of consumption values that corresponds with a list of
    utilties for a year.

    Input: Year | as int or str
    Output: Utility names, as a list
    Output: Consumption values, in gWh

    Example (from 'solar_viz_test' database):
    
    >>> get_utilities_consumption_in_year(2007)
    (['San Diego Gas and Electric', 'Southern California Edison', 'Pacific Gas and Electric'], [20324710.98, 88805391.0, 86078891.49])

    Used by server.py"""
    
    search_year = str(search_year)
    utilities = get_utility_names()
    consumption_values = []

    for utility in utilities:
        utility_consumption = get_consumption_for_utility_in_year(utility, search_year)
        if utility_consumption != []:
            utilities_consumption_gWh = float(utility_consumption[0][0])/1000
            consumption_values.append(utilities_consumption_gWh)

        else: 
            consumption_values.append(0) 

    return utilities, consumption_values

def get_consumption_from_year(input_year):
    """Return the energy consumption value from a particular year, which is 
    given as an inpu. The return value is a total of all companies.

    Returns consumption, as an float in gWh.

    Example (from 'solar_viz_test' database):

    >>> get_consumption_from_year(2008)
    197699316.25
    
    CODE NOT WORKING

    """

    search_year = str(input_year) 
    all_consumption = get_consumption_by_year()

    for pair in all_consumption:
        if pair[0] == search_year:
            production = float(pair[1])/1000
            return production
        # else: 
        #     return 0
            

def get_percent_solar_by_year(year):
    """return the percentage energy of solar in production in comparison with total consumption.
    ."""

    production = get_production_for_year(year)
    consumption = get_consumption_from_year(year)

    if consumption:
        percent_solar = round(float(production / consumption), 2)
        return percent_solar
    
    else:
        return 0


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
    working code

    Example (from 'solar_viz_test' database): 
    >>> print(get_company_application('Pacific Gas and Electric'))
    [<Program application_id=SD-CSI-00001
                       utility=1
                       city=San Diego
                       county=San Diego
                       zipcode=92121
                       contractor=4
                       pv_manuf=11
                       invert_manuf=18
                       status=Installed>, <Program application_id=SCE-CSI-06676
                       utility=2
                       city=Manhattan Beach
                       county=Los Angeles
                       zipcode=90266
                       contractor=5
                       pv_manuf=12
                       invert_manuf=19
                       status=Installed>, 
                       ... AND MORE RETURNED BUT TRUNCATED

        """

    applications = Program.query.filter(Company.name == search_company_name)\
                                .options(db.joinedload('utility_company'))\
                                .all()

    return applications


def get_production_from_utility_by_years(search_company_name):
    """Return the production from a utility company for all years

    Used in server.py.

    Example (from 'solar_viz_test' database): 
    
    >>> get_production_from_company_by_years('Pacific Gas and Electric')
    [(2015.0, Decimal('5666'), 'Pacific Gas and Electric'), (2016.0, Decimal('103458'), 
    'Pacific Gas and Electric')]


    To help with debugging: get_production_from_company_by_years('Pacific Gas and Electric')"""
    
    company_production_by_year = db.session.query\
                (extract('year', Production.end_date).label('year'),\
                func.sum(Production.produced).label('total'),\
                Company.name)\
                .join(Program, Production.application_id == Program.application_id)\
                .join(Company, Program.utility == Company.company_id)\
                .filter(Company.name == search_company_name)\
                .group_by(extract('year', Production.end_date))\
                .group_by(Company.name)\
                .order_by(extract('year', Production.end_date))\
                .all()

    return company_production_by_year


def get_utility_names():
    """Return a list of all the utilities in the companies table.
    
    Example (from 'solar_viz_test' database): 

    >>> get_utility_names()
    ['San Diego Gas and Electric', 'Southern California Edison', 'Pacific Gas and Electric']

    """
    
    utilities = Company.query.filter(Company.company_type == 'Utility and Energy Producer').all()

    utilities_list = []
    for utility in utilities:
        if utility.name != 'GRID Alternatives':
            utilities_list.append(utility.name)
    
    return utilities_list


def utility_production_for_a_year(utility, search_year):
    """Get the production for a utility, for a particular year.
    
    Input:
        utiity: company name, as a string, which must match the companies database
        search_year: year, as an int or str
    Output: production, as a float, gWh
    
    Example (from 'solar_viz_test' database): 

    >>> utility_production_for_a_year('Pacific Gas and Electric', 2016)
    103
    
    Used by server.py
    """

    search_year = float(search_year)
    years = get_production_from_utility_by_years(utility)

    for year in years:
        if search_year == year[0]:
            return float(year[1]/1000)

def all_utilities_production_for_a_year(year):
    """Returns a list of production values that correspond with the utilities in a year.

    Input: year value as str or int
    Output: 
        - list of utillities
        - list of production values, as floats, in gWh

    Example (from 'solar_viz_test' database):
    >>> all_utilities_production_for_a_year(2016)
    (['San Diego Gas and Electric', 'Southern California Edison', 'Pacific Gas and Electric'], 
    [None, None, 103.458])

    Used in server.py
    """
    
    year = int(year)
    utilities = get_utility_names()
    production_values = []
    for utility in utilities:
        production_value = utility_production_for_a_year(utility, year)
        production_values.append(production_value)

    return utilities, production_values


  

###############################################################################
#helper functions

if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)
