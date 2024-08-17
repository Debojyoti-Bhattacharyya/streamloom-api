import logging

from flask import current_app, request, jsonify

from streamloom_api.utils import ServiceUtils


def discover_all_movies():
    target_endpoint = current_app.config['DISCOVER_MOVIES_ENDPOINT']
    access_token = request.headers.get("Authorization")
    logging.info("Process started: Discovering movies")
    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, None))


def search_movies_by_name():
    data = request.get_json()
    movie_name = data.get("movieName").replace(" ", "+")
    access_token = request.headers.get("Authorization")
    target_endpoint = current_app.config['SEARCH_MOVIE_ENDPOINT']
    params = {"query": movie_name}
    logging.info("Process started: Searching related movies by name")

    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, params))


def fetch_movie_by_id():
    movie_id = request.args.get("movieId")
    access_token = request.headers.get("Authorization")
    target_endpoint = f"{current_app.config['MOVIE_DETAILS_BY_ID_ENDPOINT']}{movie_id}"
    params = {"language": "en-US"}
    logging.info("Process started: Fetching movie details by ID")

    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, params))
