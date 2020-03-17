# SolarViz

SolarViz is a full stack web application that informs users about solar energy production and news.

SolarViz has a custom web interface that displays data from the California Solar Initiative, which is an energy tracking and incentive program run by the state. The site contains dynamically generated graphs that users can review to understand broad trends in solar energy production. Users can select filters on the broader data set to see specific information from years and companies. 

SolarViz also displays current news related to solar energy and utilities. Users can see article descriptions and click them to go to the original news source. 

This project was made at Hackbright Academy in San Francisco over four weeks in February and March 2020.

### Contents
* [Technologies](#techstack)
* [Installation](#installation)
* [Features](#features)
* [Features for Version 2.0](#futurefeatures)
* [About The Developer](#aboutme)

## <a name="techstack"></a>Technologies

Tech Stack: Python, PostreSQL, SqlAlchemy, Flask, Python .csv library, HTML, JavaScript, asynchronous JavaScript (Ajax ), bootstrap, css, Chart.js, unittest <br>
APIs: Google News

## <a name="installation"></a>Installation

### Prerequisites

The following must be installed to run SolarViz:

- Python3
- PostgreSQL
- Flask
- Jinja

- API key for GoogleNews

### Run SolarViz on your local computer

Clone or fork repository:
```
$ git clone https://github.com/JKinsler/Solar_Viz.git
```
Create and activate a virtual environment inside your travelmaps directory:
```
$ virtualenv env --always-copy
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Get a Google News API key:
![api](https://newsapi.org/s/google-news-api)
<br>
Create a file called **secrets.sh** add your Google News API key there. An example of secrets.sh looks like this: <br> 
export GOOGLE_NEWS_KEY="XXXXXXXXXXXX"
<br>
Source the API key:
```
$ source secrets.sh
```
Create database 'solar_viz':
```
$ createdb solar_viz
```
Run **seed.py** interactively in the terminal. This will and create the database tables and populate them:
```
$ python3 -i seed.py
```
Run the app from the command line:
```
$ python3 server.py
```
<br><br>
