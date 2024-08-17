import json
import logging
from typing import Optional

import requests
from flask import jsonify


class ServiceUtils:
    def __init__(self):
        pass

    @staticmethod
    def call_external_api(endpoint: str,
                          access_token: str,
                          params: Optional[dict]):
        headers = {
            "accept": "application/json",
            "Authorization": access_token
        }
        try:
            response = requests.get(endpoint, params=params, headers=headers)
            logging.info("Successfully retrieved information!!")
            return json.loads(response.text)
        except Exception as e:
            logging.error(f"Failed to retrieve information: {e}")
            return {"message": "Failed to retrieve information"}
