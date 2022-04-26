from app import app
import urllib.request,json
from .models import movie

#getting api key
api_key = app.config['MOVIE_API_KEY']
#getting the base_url
base_url = app.config['MOVIE_API_BASE_URL']

#Get Movie class template
Movie = movie.Movie

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category, api_key)
