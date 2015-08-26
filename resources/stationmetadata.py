from flask_restful import Resource

from darwinrest.common.datafetcher import get_stations_metadata

class StationMetaData(Resource):

    def get(self, query=None):

        try:
            response = get_stations_metadata(query)

        except Exception as e:
            response = {
                "error": str(e)
            }

        return response

