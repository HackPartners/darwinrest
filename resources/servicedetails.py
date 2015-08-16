from flask_restful import Resource

from nredarwin.webservice import DarwinLdbSession

class ServiceDetails(Resource):

    def get(self):
        pass