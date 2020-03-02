import query
import doctest
import unittest
# from unittest import TestCase
from server import app
from model import connect_to_db, db
import server
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract, func
from decimal import Decimal # required to handle Decimal by AssertEqual

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"



class DatabaseTests(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the sql alchemy database
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        connect_to_db(app, 'postgresql:///solar_viz_test')


    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        print('called tearDown')


    # def test_print_hello(self):
    #     """Can we find an employee in the sample data?"""

    #     print('Hello World')


    def test_get_production_by_year(self):
        """Test get-production_by_year function from query.py"""

        actual = query.get_production_by_year()
        expected = [(2007.0, Decimal('151240')), (2011.0, Decimal('22302')), \
            (2014.0, Decimal('301')), (2015.0, Decimal('6490')), \
            (2016.0, Decimal('103458')), (2018.0, Decimal('62918')), \
            (2019.0, Decimal('18356'))]

        self.assertEqual(actual, expected)
        

    def test_convert_date_to_iso(self):
        """test convert_date_to_iso(self) function."""

        self.assertEqual(query.convert_date_to_iso(2016), '2016-01-01T00:00:00')


    def test_format_production_for_table(self):
        """Test format_production_for_table from query.py"""

        actual = type(query.format_production_for_table())
        expected = type({2007: 151240, 2011: 22302, 2014: 301, 2015: 6490, 2016: 103458, 2018: 62918, 2019: 18356})

        self.assertEqual(actual, expected)



if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()