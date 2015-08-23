from flask_restful import Resource, reqparse, marshal_with, fields

from darwinrest.common.darwinutil import get_service_details
from darwinrest.common.util import api_bool

from nredarwin.webservice import DarwinLdbSession

query_parser = reqparse.RequestParser()

query_parser.add_argument(
    'apiKey', dest='api_key',
    required=True,
    type=str, help='Your Darwin API Key',
)

query_parser.add_argument(
    'id', dest='id',
    required=True,
    type=str, help='The ID of the service',
)

query_parser.add_argument(
    'allFields', dest='all_fields',
    type=api_bool, help='Whether all fields should be displayed.',
)

class ServiceDetails(Resource):

    def get(self):

        args = query_parser.parse_args()

        try:
            response = get_service_details(
                            args.api_key, 
                            args.id, 
                            all_fields=args.all_fields)
            
        except Exception as e:
            response = {
                "error": str(e)
            }

        return response