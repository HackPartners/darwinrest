from flask_restful import Resource, reqparse

import json

from darwinrest.common.darwinutil import get_station_board

query_parser = reqparse.RequestParser()

query_parser.add_argument(
    'apikey', dest='api_key',
    required=True,
    type=str, help='Your Darwin API Key',
)
query_parser.add_argument(
    'departures', dest='departures', default=True,
    type=bool, help='Include departing services in the departure board',
)
query_parser.add_argument(
    'arrivals', dest='arrivals', default=False,
    type=bool, help='Include arriving services in the departure board',
)
query_parser.add_argument(
    'destination', dest='destination', default=None,
    type=str, help='Filter results so they only include services calling at a particular destination',
)
query_parser.add_argument(
    'origin', dest='origin', default=None,
    type=str, help='Filter results so they only include services originating from a particular station',
)

class StationBoard(Resource):

    def get(self, crs=None):

        args = query_parser.parse_args()

        print args

        station_boards = get_station_board(
                            args.api_key,
                            crs,
                            args.departures,
                            args.arrivals,
                            args.destination,
                            args.origin)

        return station_boards