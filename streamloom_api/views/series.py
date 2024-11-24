import logging

from flask import current_app, jsonify, request

from streamloom_api.utils import ServiceUtils


def search_series_by_name():
    payload = request.get_json()
    default_params = current_app.config['SEARCH_SERIES_DEFAULT_PARAMS']
    params = {
        key: payload.get(
        key, default_params[key] if key != 'query' else default_params[key].replace(' ', '+'))
        for key in default_params
        }
    access_token = request.headers.get("Authorization")
    target_endpoint = current_app.config['SEARCH_TV_SERIES_ENDPOINT']
    logging.info("Process started: Searching related TV Series by name")
    logging.info(f"Search series request: {params}")
    
    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, params,
                                                  'tv series related by name'))


def fetch_series_by_id():
    payload = request.get_json()
    default_params = current_app.config['SERIES_DETAILS_BY_ID_DEFAULT_PARAMS']
    params = {
        key: payload.get(key, default_params[key])
        for key in default_params
    }
    access_token = request.headers.get("Authorization")
    target_endpoint = f"{current_app.config['SERIES_DETAILS_ID_ENDPOINT']}{params.get('series_id')}"
    logging.info("Process started: Fetching tv series details by ID")
    logging.info(f"Series details request body: {params}")
    return jsonify(ServiceUtils.call_external_api(target_endpoint, access_token, params, 'tv series details'))