from app import app
from flask import render_template
from .request import get_movies

@app.route('/')
def home():
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    return render_template(
        'index.html',
        popular_movies = popular_movies,
        upcoming_movies = upcoming_movies,
        now_showing_movies = now_showing_movies
        )