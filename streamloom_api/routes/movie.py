from flask import Blueprint
from streamloom_api.views.movie import (
    discover_all_movies,
    search_movies_by_name,
    fetch_movie_by_id
)

# Declare the blueprints for different routes, created based on their functionalities
movie_routes = Blueprint('movie_routes', __name__)


@movie_routes.route("/getMovieList", methods=['GET'])
def get_all_movies():
    return discover_all_movies()


@movie_routes.route("/searchByMovieName", methods=['GET'])
def search_movie_details_by_name():
    return search_movies_by_name()


@movie_routes.route("/getMovieById", methods=['GET'])
def get_movie_by_id():
    return fetch_movie_by_id()
