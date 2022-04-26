class Config:
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
class DevConfig(Config):
    DEBUG = True
class ProdConfig(Config):
    pass