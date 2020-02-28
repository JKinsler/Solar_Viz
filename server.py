"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import (Company, Program, Production, Consumption, connect_to_db, db)

from query import (get_production_by_year, format_production_for_table, 
                   format_production_for_chartjs, get_production_years, 
                   get_production_for_year, get_consumption_from_year,
                   get_percent_solar_by_year, all_utilities_production_for_a_year)



app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


#MY CODE HERE ##########################

@app.route('/')
def index():
    """Homepage."""
    return render_template("homepage.html")


@app.route("/data_viz")
def show_solar_details():
    """Show data vizualization details."""

    #get production data by year. This will be a dictionary.
    production_by_year = format_production_for_table()
    years = get_production_years()

    return (render_template("data_viz.html",\
            production_by_year = production_by_year,\
            years = years))


@app.route("/data_viz/all_production")
def show_all_production():
    """Return all production data by year."""

    
    #get production data by year. 
    # 'datasets' should be a list of dictionaries
    # 'labels' should be a list
    yearly_labels, production_datasets = format_production_for_chartjs()

    return jsonify({'labels_by_year': yearly_labels, 'yearly_datasets': production_datasets})


@app.route("/data_viz/<int:year>")
def show_year(year):
    """Show info about the year."""


    #information for table
    production = get_production_for_year(year)
    consumption = get_consumption_from_year(year)
    percent = get_percent_solar_by_year(year)


    return render_template("year.html",  year = year,\
                            production = production, \
                            consumption = consumption, \
                            percent = percent)


@app.route("/data_viz/<int:year>/compare_companies")
def compare_companies(year):
    """Show info about the companies from the year."""

    #information for utilities bar chart
    utilities, production_values = all_utilities_production_for_a_year(year)


    return jsonify({'labels_utilities': utilities}, {'yearly_datasets': production_values})

# in future update routes to GET and POST methods and pass d
# may need to update data type to be better for chart.js

#DUNDER NAME #########################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')

