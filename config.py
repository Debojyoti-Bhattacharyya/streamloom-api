import logging
import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    DEBUG = False
    TMDB_API_KEY = os.getenv('TMDB_API_KEY')

    # External APIs for Movies
    DISCOVER_MOVIES_ENDPOINT = "https://api.themoviedb.org/3/discover/movie"
    SEARCH_MOVIE_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
    MOVIE_DETAILS_BY_ID_ENDPOINT = "https://api.themoviedb.org/3/movie/"
    CONFIGURATION_DETAILS_ENDPOINT = "https://api.themoviedb.org/3/configuration"

    # External APIs for TV Series
    DISCOVER_TV_SERIES_ENDPOINT = "https://api.themoviedb.org/3/discover/tv"
    SEARCH_TV_SERIES_ENDPOINT = "https://api.themoviedb.org/3/search/tv"
    SERIES_DETAILS_ID_ENDPOINT = "https://api.themoviedb.org/3/tv/"

    # Logging configurations. This used the the CustomFormatter formatter class defined below
    logging_config = {
        'version': 1,
        'formatters': {'MyCustomFormatter': {
            '()': 'config.CustomFormatter'
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'MyCustomFormatter'
        }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    }

    # Default request parameters for different endpoints
    SEARCH_SERIES_DEFAULT_PARAMS = {
        'query' : 'Something Random',
        'first_air_date_year': None,
        'include_adult': False,
        'language': 'en-US',
        'page': 1,
        'year': None
    }
    
    SERIES_DETAILS_BY_ID_DEFAULT_PARAMS = {
        'series_id' : 12345,
        'append_to_response' : None,
        'language' : 'en-US'
    }

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
