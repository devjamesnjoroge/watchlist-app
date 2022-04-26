from app import app
from flask import render_template
from .request import get_movies

@app.route('/')
def home():
    popular_movies = get_movies('popular')
    return render_template('index.html', popular_movies = popular_movies)