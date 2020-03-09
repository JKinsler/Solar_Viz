"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import (Company, Program, Production, Consumption, connect_to_db, db)

from query import (get_production_by_year, format_production_for_table, 
                   format_production_for_chartjs, get_production_years, 
                   get_production_for_year, get_consumption_from_year,
                   get_percent_solar_by_year, all_utilities_production_for_a_year, 
                   get_utilities_consumption_in_year, get_production_change)
from news import (get_google_news, create_search_url, parse_google_news_response)


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


@app.route('/solar_news')
def show_solar_news():
    """Newsfeed page."""
    return render_template("solar_news.html")


@app.route("/solar_news/news_feed")
def get_news_feed_info():
    """Show info about the companies from the year."""

    #get variables I want to send
    search_url, payload = create_search_url()
    news_results = get_google_news(search_url, payload)


    return jsonify(news_results)


@app.route("/data_viz", methods=["GET"])
def show_solar_details():
    """Show data vizualization details."""

    #get production data by year. This will be a dictionary.
    production_by_year = format_production_for_table()
    years = get_production_years()

    return (render_template("data_viz.html",\
            production_by_year = production_by_year,\
            years = years))


@app.route("/data_viz", methods=["POST"])
def get_year():
    """Get selected year from data_viz dropdown."""

    selected_year = request.form.get("year")
    
    return redirect(f"/data_viz/{selected_year}")


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
    production = '{:,.0f}'.format(production)
    
    consumption = get_consumption_from_year(year)
    if consumption != None:
        consumption = '{:,.0f}'.format(consumption)
    else:
        consumption = 0
    
    percent_production = get_percent_solar_by_year(year)
    change_factor = get_production_change(year)


    return render_template("year.html",  year = year,\
                            production = production, \
                            consumption = consumption, \
                            percent_production = percent_production, \
                            change_factor = change_factor)


@app.route("/data_viz/<int:year>/compare_companies")
def compare_companies(year):
    """Show info about the companies from the year."""

    #information for utilities bar chart
    utilities, production_values = all_utilities_production_for_a_year(year)
    utilities2, consumption_values = get_utilities_consumption_in_year(year)


    return jsonify({'labels_utilities': utilities,
                   'year_productions': production_values, 
                   'year_consumptions': consumption_values})

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

