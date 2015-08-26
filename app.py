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

"""
  @api {get} /api/status /api/status
  @apiVersion 0.0.1
  @apiName Darwin API services status
  @apiGroup Core data
  @apiPermission public
 
  @apiDescription Retreive the status for the OpenLBDWS API as a text from http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/.
 
  @apiSuccess {String}   OpenLBDWS      The status of the OpenLBDWS API.

  @apiExample Status example usage:
  curl -i http://darwin.hacktrain.com/api/status

  @apiSuccessExample Success Response Example:
  # Query http://darwin.hacktrain.com/api/status 
  {
     "OpenLDBWS": "Available"
  }
"""
api.add_resource(LdbwsStatus, '/api/status')

"""
  @api {get} /api/crs/:query /api/crs
  @apiVersion 0.0.1
  @apiName Station codes
  @apiGroup Core data
  @apiPermission public

  @apiDescription Retreive either all crs codes, or a subset of codes

  @apiParam {String} query (Optional) A query to find all stations that contain this string.

  @apiExample Code Query Example:
  curl -i http://darwin.hacktrain.com/api/crs/eus

  @apiSuccessExample Simple query request:
  # Query http://darwin.hacktrain.com/api/crs/eus
  {
    "EUS": "Euston"
  }

  @apiSuccessExample All CRS Codes request:
  # Query http://darwin.hacktrain.com/api/crs
  {
    ...
    "ZBB": "Barbican",
    "ZBK": "Barking Underground",
    "ZCW": "Canada Water",
    "ZEL": "Elephant & Castle (Underground)",
    "ZFD": "Farringdon",
    "ZHS": "High Street Kensington Underground",
    "ZWL": "Whitechapel"
  }
"""
api.add_resource(StationCrs, '/api/crs', '/api/crs/<string:query>')


api.add_resource(StationMetaData, '/api/station', '/api/station/<string:query>')

"""
  @api {get} /api/board/:crs /api/board
  @apiVersion 0.0.1
  @apiName Station board
  @apiGroup Darwin core
  @apiPermission public
 
  @apiDescription Retrieve the details for a specific station board given a CRS code.
 
  @apiParam {Number} crs A CRS short-code of the station. These codes can be found on National Rail Enquiries website.
  @apiParam {String} apiKey The API Key from Darwin OpenLBDWS.
  @apiParam {Boolean} departures (Optional) Boolean stating whether departures are requested (Either departures or arrivals required).
  @apiParam {Boolean} arrivals (Optional) Boolean stating whether arrivals are requested (Either departures or arrivals required).
  @apiParam {String} destination (Optional) The destination as a CRS code where the service is going.
  @apiParam {String} origin (Optional) The origin as a CRS code where the service is coming from.
  @apiParam {String} allFields (Optional) Flag that states whether all additional fields will be returned.
 
  @apiSuccess {String}   arrival       The time of arrival.
  @apiSuccess {String}   departure     The time for departure.
  @apiSuccess {Date}     destination   The destination of the service.
  @apiSuccess {Number}   platform      The platform number.

  @apiExample Usage Simple Request:
  curl -i http://darwin.hacktrain.com/api/board/EUS?apiKey=YOUR-API-KEY

  @apiSuccessExample Success Simple Response Example:
  # Query http://darwin.hacktrain.com/api/board/EUS?apiKey=YOUR-API-KEY 
  [
    {
        "arrival": "19:14", 
        "departure": "On time", 
        "destination": "Tring", 
        "platform": "10"
    }, 
    {
        "arrival": "19:17", 
        "departure": "On time", 
        "destination": "Manchester Piccadilly", 
        "platform": null
    }
  ]
"""
api.add_resource(StationBoard, '/api/board/<string:crs>')


"""
  @api {get} /api/service/:id /api/service
  @apiVersion 0.0.1
  @apiName Service details
  @apiGroup Darwin core
  @apiPermission user
 
  @apiDescription Retrieve the details for a specific service given a service ID.
 
  @apiParam {Number} Id The id for the service that is to be retreived.
  @apiParam {Number} allFields A flag that states whether all fields should be included.
  
  @apiSuccess {String}   arrival       The time of arrival.
  @apiSuccess {String}   departure     The time for departure.
  @apiSuccess {Date}     destination   The destination of the service.
  @apiSuccess {Number}   platform      The platform number.

  @apiExample Example usage:
  curl -i http://darwin.hacktrain.com/api/service?id=SERVICE_ID&apiKey=YOUR-API-KEY

  @apiSuccessExample Success Response Example:
  # Query http://darwin.hacktrain.com/api/service?id=SERVICE_ID&apiKey=YOUR-API-KEY
  {
    "crs": "EUS", 
    "isCancelled": null, 
    "locationName": "London Euston", 
    "operatorCode": "VT", 
    "operatorName": "Virgin Trains", 
    "platform": null, 
    "scheduledArrivalTime": null, 
    "scheduledDepartureTime": "15:17"
  }

  @apiSuccessExample Success Response With allFields:
  # Query http://darwin.hacktrain.com/api/service?allFields=True&id=SERVICE_ID&apiKey=YOUR-API-KEY
  {
    "actualArrivalTime": null, 
    "actualDepartureTime": "On time", 
    "crs": "EUS", 
    "disruptionReason": null, 
    "estimatedArrivalTime": null, 
    "estimatedDepartureTime": null, 
    "generatedAt": "2015-08-23 16:06:02.010761+01:00", 
    "isCancelled": null, 
    "locationName": "London Euston", 
    "operatorCode": "VT", 
    "operatorName": "Virgin Trains", 
    "platform": null, 
    "previousCallingPointList": [], 
    "scheduledArrivalTime": null, 
    "scheduledDepartureTime": "15:17", 
    "subsequentCallingPointList": [
      {
        "callingPoints": [
            {
                "actualTime": "15:46", 
                "crs": "MKC", 
                "estimatedTime": null, 
                "locationName": "Milton Keynes Central", 
                "scheduledTime": "15:50"
            }, 
            {
                "actualTime": null, 
                "crs": "SOT", 
                "estimatedTime": "On time", 
                "locationName": "Stoke-on-Trent", 
                "scheduledTime": "16:50"
            }, 
            {
                "actualTime": null, 
                "crs": "SPT", 
                "estimatedTime": "On time", 
                "locationName": "Stockport", 
                "scheduledTime": "17:18"
            }, 
            {
                "actualTime": null, 
                "crs": "MAN", 
                "estimatedTime": "On time", 
                "locationName": "Manchester Piccadilly", 
                "scheduledTime": "17:29"
            }
        ], 
        "changeRequired": false, 
        "isCancelled": false, 
        "serviceType": "train"
      }
    ]
  }
"""
api.add_resource(ServiceDetails, '/api/service')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
