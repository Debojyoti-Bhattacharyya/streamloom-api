from logging.config import dictConfig

from flask import Flask

from config import Config
from streamloom_api.routes.movie import movie_routes
from streamloom_api.routes.series import series_routes

dictConfig(Config.logging_config)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(movie_routes, url_prefix="/api/v1/movie")
    app.register_blueprint(series_routes, url_prefix="/api/v1/series")
    return app
