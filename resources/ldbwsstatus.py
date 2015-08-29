from flask_restful import Resource, reqparse

import json

from common.datafetcher import get_ldbws_status

class LdbwsStatus(Resource):

    def get(self, crs=None):

        ldbwsStatus = get_ldbws_status()

        response = {
            "OpenLDBWS": ldbwsStatus
        }

        return response