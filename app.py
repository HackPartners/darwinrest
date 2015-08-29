#Adding to pythonpath
import sys
import os
directory = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.append(directory)

from flask import Flask
from flask_restful import Api
from resources.stationboard import StationBoard
from resources.servicedetails import ServiceDetails
from resources.ldbwsstatus import LdbwsStatus
from resources.stationcrs import StationCrs
from resources.stationmetadata import StationMetaData

app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
  # This function enables CORS in all requests
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET')
  return response

api.add_resource(LdbwsStatus, '/api/status')

api.add_resource(StationCrs, '/api/station/code', '/api/station/code/<string:query>')

api.add_resource(StationMetaData, '/api/station/detail', '/api/station/detail/<string:query>')

api.add_resource(
  StationBoard, 
  '/api/train/<string:station>',
  '/api/train/<string:station>/<string:direction>',
  '/api/train/<string:station>/<string:direction>/<string:secondaryStation>')

api.add_resource(ServiceDetails, '/api/service')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)

