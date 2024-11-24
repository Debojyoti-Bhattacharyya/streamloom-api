from flask import Blueprint

from streamloom_api.views.series import (fetch_series_by_id,
                                         search_series_by_name)

# Declare the blueprints for different routes, created based on their functionalities
series_routes = Blueprint('series_routes', __name__)

@series_routes.route("/searchBySeriesName", methods=['GET'])
def search_series_details_by_name():
    return search_series_by_name()


@series_routes.route("/getSeriesById", methods=["GET"])
def get_series_by_id():
    return fetch_series_by_id()