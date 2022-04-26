from distutils.command.config import config
import imp
from app import app
from flask import render_template

@app.route('/')
def home():
    title = 'App runs'
    return render_template('index.html')
