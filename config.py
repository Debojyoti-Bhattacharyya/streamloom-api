import os
import logging

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    DEBUG = False
    TMDB_API_KEY = os.getenv('TMDB_API_KEY')

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

    # External APIs for Movies
    DISCOVER_MOVIES_ENDPOINT = "https://api.themoviedb.org/3/discover/movie"
    SEARCH_MOVIE_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
    MOVIE_DETAILS_BY_ID_ENDPOINT = "https://api.themoviedb.org/3/movie/"


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
