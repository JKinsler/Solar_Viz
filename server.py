"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import (Company, Program, Production, Consumption, connect_to_db, db)

from query import (get_production_by_year, format_production_for_table, 
                   format_production_for_chartjs)



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

    #get production data by year. 
    # 'datasets' should be a list of dictionaries
    # 'labels' should be a list
    yearly_labels_json, production_datasets_json = format_production_for_chartjs()

    return (render_template("data_viz.html",\
            production_by_year = production_by_year,\
            yearly_labels_json = yearly_labels_json, \
            production_datasets_json = production_datasets_json))


# in future update routes to GET and POST methods and pass data in to javascript
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

