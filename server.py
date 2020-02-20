"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import (Company, Program, Production, Consumption, connect_to_db, db)

from query import (get_production_by_year)



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
    production_by_year = get_production_by_year()

    return render_template("data_viz.html")


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

