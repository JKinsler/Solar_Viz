"""Practice using the google news API to get latest articles"""

import requests, json
import datetime
from datetime import timedelta
import os


def get_oldest_article_date():
    """Return the date of the oldest allowed article"""

    # date = datetime.datetime.strptime(date, "%m/%d/%Y")
    today_date = datetime.date.today()
    last_week = today_date-timedelta(days=2)
    search_date = last_week.isoformat()

    return search_date


def create_search_url():
    """Retrun a url to search in Google News that includes the desired news 
    search parameters.

    Output: url as a string

    Examples:
    >>>create_search_url()
    'http://newsapi.org/v2/everything?'
           'q=Apple&'
           'from=2020-03-02&'
           'sortBy=popularity&'
           'apiKey=XXXXXX'
    """

    search_url = 'http://newsapi.org/v2/everything?'

    # A date and optional time for the oldest article allowed. This should be in ISO 8601 format.
    oldest_article = get_oldest_article_date()
    
    payload = {
        "q":"solar+energy+utility",
        "from":oldest_article,
        "sortBy":"relevancy",
        "pageSize":100,
        "apiKey": os.environ['GOOGLE_NEWS_KEY']
    }


    return search_url, payload


def get_google_news(search_url, payload):
    """Return request from Google News endpoint

    Output: dictionary of google news results. 

    Examples:
        {
    "status": "ok",
    "totalResults": 38,
    -"articles": [
        -{
        -"source": {
            "id": null,
            "name": "Nytimes.com"
            },
        "author": "Nick Corasaniti, Alexander Burns",
        "title": "Amy Klobuchar Drops Out of Presidential Race and Plans to Endorse Biden - The New York Times",
        "description": "Ms. Klobuchar made her decision hours before Super Tuesday. She shocked the primary field with a third-place finish in New Hampshire, but ultimately could not compete with better-funded rivals.",
        "url": "https://www.nytimes.com/2020/03/02/us/politics/amy-klobuchar-drops-out.html",
        "urlToImage": "https://static01.nyt.com/images/2020/03/02/us/politics/02klobuchar-out1/02klobuchar-out1-facebookJumbo.jpg",
        "publishedAt": "2020-03-02T18:31:00Z",
        "content": "The senator from Minnesota shocked her rivals with a surprising third-place finish in New Hampshire, placing ahead of better-known candidates like Senator Elizabeth Warren of Massachusetts and Mr. Biden.\r\nBut aside from New Hampshire, Ms. Klobuchar struggled … [+1222 chars]"
        },
        -{
        -"source": {
            "id": null,
            "name": "Tmz.com"
            },
        "author": "TMZ Staff",
        "title": "'Inside the Actors Studio' Host James Lipton Dead at 93 from Bladder Cancer - TMZ",
        "description": "The great James Lipton has passed away.",
        "url": "https://www.tmz.com/2020/03/02/inside-the-actors-studio-james-lipton-dead-dies-age-93/",
        "urlToImage": "https://imagez.tmz.com/image/a5/16by9/2020/03/02/a57ab23bb3b0405e8086e85a6597c5dd_xl.jpg",
        "publishedAt": "2020-03-02T17:58:00Z",
        "content": "\"Inside the Actors Studio\" host and veteran TV writer James Lipton has died ... TMZ has learned.\r\nLipton passed away peacefully Monday morning at his New York City home. His wife, Kedakai Turner, tells TMZ James had been battling bladder cancer. She adds, \"Th… [+2678 chars]"
        },
        """

    # get the results from the URL endpoint
    r = requests.get(search_url, params=payload)
    # print (f' r.url {r.url}')

    # print the response. <Response [200]> means good!
    # print (r.json)
    # will print:
    # <bound method Response.json of <Response [200]>>

    # print(f' type(r): {type(r)}')

    #save the response as a dictionary
    news_results = r.json()
    # print(f' type(news_results): {type(news_results)}')

    return news_results


def parse_google_news_response(news_results, i=0):
    """Return parsed results of the google news request.
    Translate to javascript to use."""

    # get the value of the key 'status' from the response dictionary
    results_status = news_results['status']
    print(f'results_status: {results_status}')

    # get the value of the key 'totalResults' from the response dictionary
    num_results = news_results['totalResults']
    print(f'num_results: {num_results}')

    #save the response from the dictionary
    title = news_results['articles'][i]['title']
    source = news_results['articles'][i]['source']['name']
    published_time = news_results['articles'][i]['publishedAt']
    description = news_results['articles'][i]['description']
    article_url = news_results['articles'][i]['url']
    image_url = news_results['articles'][i]['urlToImage']
    return (title, source, published_time, description, article_url, image_url)


# HELPFUL CODE FOR PYTHON DEBUGGING BELOW
# search_url, payload = create_search_url()
# current_news = get_google_news(search_url, payload)
# for i in range(5):
#     title, source, published_time, description, article_url, image_url = parse_google_news_response(current_news, i)
#     print(f'Article {i+1}: {title}\n{source}\n{published_time}\n{description}\n{article_url}\n\n')
