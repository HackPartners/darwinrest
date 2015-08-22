from flask_restful import Resource, reqparse, marshal_with, fields

from darwinrest.common.darwinutil import get_service_details

from nredarwin.webservice import DarwinLdbSession

query_parser = reqparse.RequestParser()

query_parser.add_argument(
    'apiKey', dest='api_key',
    required=True,
    type=str, help='Your Darwin API Key',
)

class ServiceDetails(Resource):

    def get(self):

        args = query_parser.parse_args()

        try:
            response = get_service_details(id)
        except Exception as e:
            response = {
                "error": str(e)
            }

        return response