from flask_restful import Resource, reqparse, marshal_with, fields

from darwinrest.common.darwinutil import get_station_board

query_parser = reqparse.RequestParser()

def api_bool(value):
    if value in ('y', 't', 'true', 'True', 'yes', '1'):
        return True
    else:
        return False

query_parser.add_argument(
    'apiKey', dest='api_key',
    required=True,
    type=str, help='Your Darwin API Key',
)
query_parser.add_argument(
    'departures', dest='departures', default=True,
    type=api_bool, help='Include departing services in the departure board',
)
query_parser.add_argument(
    'arrivals', dest='arrivals', default=False,
    type=api_bool, help='Include arriving services in the departure board',
)
query_parser.add_argument(
    'destination', dest='destination', default=None,
    type=str, help='Filter results so they only include services calling at a particular destination',
)
query_parser.add_argument(
    'origin', dest='origin', default=None,
    type=str, help='Filter results so they only include services originating from a particular station',
)
query_parser.add_argument(
    'allFields', dest='all_fields', default=None,
    type=api_bool, help='Whether response should contain all fields',
)

class StationBoard(Resource):

    def get(self, crs=None):

        args = query_parser.parse_args()

        try:
            response = get_station_board(
                                args.api_key,
                                crs,
                                args.departures,
                                args.arrivals,
                                args.destination,
                                args.origin,
                                args.all_fields)
        except Exception as e:
            response = {
                "error": str(e)
            }

        return response

