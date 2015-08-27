from flask_restful import Resource, reqparse, marshal_with, fields

from darwinrest.common.darwinutil import get_station_board
from darwinrest.common.util import api_bool
from darwinrest.common.datafetcher import validate_station_string

query_parser = reqparse.RequestParser()

query_parser.add_argument(
    'apiKey', dest='api_key',
    required=True,
    type=str, help='Your Darwin API Key',
)

query_parser.add_argument(
    'rows', dest='rows', default=10,
    type=int, help='Number of rows to be retreived',
)

class StationBoard(Resource):

    def get(self, station="", direction="", secondaryStation=""):

        args = query_parser.parse_args()

        origin = ""
        destination = ""
        show_departures = True
        show_arrivals = True

        try: 
            if direction:
                if direction.upper() == "TO":
                    
                    if secondaryStation:
                        origin = validate_station_string(secondaryStation, "secondaryStation")
                    show_arrivals = False
                
                elif direction.upper() == "FROM":

                    if secondaryStation:
                        destination = validate_station_string(secondaryStation, "secondaryStation")
                    show_departures = False
                
                else:
                    return {
                        "error": "Invalid direction parameter given as '" 
                         + direction + "'. Direction supplied should be 'to' or 'from."
                    }

            response = get_station_board(
                                args.api_key,
                                validate_station_string(station, "station"),
                                show_departures,
                                show_arrivals,
                                origin,
                                destination,
                                args.rows)

        except Exception as e:
            response = {
                "error": str(e)
            }

        return response

