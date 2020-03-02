import query
import doctest
import unittest
# from unittest import TestCase
from server import app
from model import connect_to_db, db
import server
from flask_sqlalchemy import SQLAlchemy


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# class TestQuery(unittest.TestCase):
#     """Unit tests for query.py"""

#     def test_convert_date_to_iso(self):
#         """test convert_date_to_iso(self) function."""

#         self.assertEqual(convert_date_to_iso(2016), '2016-01-01T00:00:00')


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the sql alchemy database
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        connect_to_db(app)
        # below code is contents of connect_to_db functions
        # # Connect to test database
        # # connect to the test database
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///solar_viz_test'
        
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # db.app = app
        # db.init_app(app)

        # Create tables and add sample data
        # db.create_all()
        # example_data()

        print('called SetUp')


    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        # db.drop_all()

        print('called tearDown')


    def test_print_hello(self):
        """Can we find an employee in the sample data?"""

        print('Hello World')


    def test_get_production_by_year(self):

        actual = query.get_production_by_year()
        expected = [(2007.0, Decimal('151240')), (2011.0, Decimal('22302')), \
            (2014.0, Decimal('301')), (2015.0, Decimal('6490')), \
            (2016.0, Decimal('103458')), (2018.0, Decimal('62918')), \
            (2019.0, Decimal('18356'))]

        self.assertEqual(actual, expected)
        
        


    # def test_emps_by_state(self):
    #     """Find employees in a state."""

    #     result = self.client.get("/emps-by-state?state=California")

    #     self.assertIn(b"Nadine", result.data)



if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()