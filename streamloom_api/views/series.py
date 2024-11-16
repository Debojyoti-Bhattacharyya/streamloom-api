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