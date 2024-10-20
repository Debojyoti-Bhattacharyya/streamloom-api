import logging

from flask import current_app, request, jsonify

from streamloom_api.utils import ServiceUtils


def discover_all_movies():
    target_endpoint = current_app.config['DISCOVER_MOVIES_ENDPOINT']
    access_token = request.headers.get("Authorization")
    logging.info("Process started: Discovering movies")
    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, None, 'discovered movies'))


def search_movies_by_name():
    data = request.get_json()
    movie_name = data.get("movieName").replace(" ", "+")
    access_token = request.headers.get("Authorization")
    target_endpoint = current_app.config['SEARCH_MOVIE_ENDPOINT']
    params = {"query": movie_name}
    logging.info("Process started: Searching related movies by name")

    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, params,
                                                  'movie related by name'))


def fetch_movie_by_id():
    movie_id = request.args.get("movieId")
    access_token = request.headers.get("Authorization")
    target_endpoint = f"{current_app.config['MOVIE_DETAILS_BY_ID_ENDPOINT']}{movie_id}"
    params = {"language": "en-US"}
    logging.info("Process started: Fetching movie details by ID")

    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, params, 'movie details'))


def fetch_movie_poster():
    movie_id = request.get_json().get("movieId")
    access_token = request.headers.get("Authorization")
    movie_images_endpoint = f"{current_app.config['MOVIE_DETAILS_BY_ID_ENDPOINT']}{movie_id}/images"
    configuration_endpoint = f"{current_app.config['CONFIGURATION_DETAILS_ENDPOINT']}"
    params = {"language": "en-US"}
    logging.info("Process started: Fetching movie posters")
    movie_images_response = ServiceUtils.call_external_api(movie_images_endpoint, access_token, None, 'movie images')
    configuration_response = ServiceUtils.call_external_api(configuration_endpoint, access_token, params, 'configuration')
    posters = [item.get('file_path') for item in movie_images_response.get('posters')]
    complete_poster_urls = [configuration_response.get('images').get('secure_base_url') + 'original' + poster
                            for poster in posters]
    movie_posters = {'posters': complete_poster_urls}
    logging.info(f"Successfully fetched movie posters: {movie_posters}")
    return jsonify(movie_posters)