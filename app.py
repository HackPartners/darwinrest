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

app = Flask(__name__)
api = Api(app)

"""
  @api {get} /api/status/ Get status of Darwin services
  @apiVersion 0.0.1
  @apiName Get Darwin Status
  @apiGroup GetDarwinStatus
  @apiPermission public
 
  @apiDescription Retreive the status for the OpenLBDWS API as a text from http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/.
 
  @apiSuccess {String}   OpenLBDWS      The status of the OpenLBDWS API.

  @apiExample Status example usage:
  curl -i http://darwin.hacktrain.com/api/status

  @apiSuccessExample Success Response Example:
  {
     "OpenLDBWS": "Available"
  }
"""
api.add_resource(LdbwsStatus, '/api/status')


"""
  @api {get} /api/board/:crs Request station board data
  @apiVersion 0.0.1
  @apiName Get Station Board
  @apiGroup GetStationBoard
  @apiPermission user
 
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
  @api {get} /api/service/:id Request details for service
  @apiVersion 0.0.1
  @apiName Get Service Details
  @apiGroup GetServiceDetails
  @apiPermission user
 
  @apiDescription Retrieve the details for a specific service given a service ID.
 
  @apiParam {Number} Id The id for the service that is to be retreived.
  
  @apiSuccess {String}   arrival       The time of arrival.
  @apiSuccess {String}   departure     The time for departure.
  @apiSuccess {Date}     destination   The destination of the service.
  @apiSuccess {Number}   platform      The platform number.

  @apiExample Example usage:
  curl -i http://darwin.hacktrain.com/api/service/13?apiKey=YOUR-API-KEY

  @apiSuccessExample Success Response Example:
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
api.add_resource(ServiceDetails, '/api/service/<int:id>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
