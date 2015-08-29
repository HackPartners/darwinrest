from flask_restful import Resource, reqparse, marshal_with, fields

from common.datafetcher import get_stations_and_codes

class StationCrs(Resource):

    def get(self, query=None):

        try:
            response = get_stations_and_codes(query)

        except Exception as e:
            response = {
                "error": str(e)
            }

        return response

