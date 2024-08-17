from flask import Flask
from streamloom_api.routes.movie import movie_routes
from config import Config
from logging.config import dictConfig

dictConfig(Config.logging_config)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(movie_routes, url_prefix="/api/v1/movie")
    return app
