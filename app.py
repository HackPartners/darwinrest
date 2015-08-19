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

app = Flask(__name__, static_url_path='')
api = Api(app)

@app.route('/')
def docs():
    return app.send_static_file('index.html')

"""
  @api {get} /status/ Get status of Darwin services
  @apiVersion 0.0.1
  @apiName Get Darwin Status
  @apiGroup GetDarwinStatus
  @apiPermission public
 
  @apiDescription Retreive the status for the OpenLBDWS API as a text from http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/.
 
  @apiSuccess {String}   OpenLBDWS      The status of the OpenLBDWS API.

  @apiExample Status example usage:
  curl -i http://darwin.hacktrain.com/status

  @apiSuccessExample Success Response Example:
  {
     "OpenLDBWS": "Available"
  }
"""
api.add_resource(LdbwsStatus, '/status')


"""
  @api {get} /board/:crs Request station board data
  @apiVersion 0.0.1
  @apiName Get Station Board
  @apiGroup GetStationBoard
  @apiPermission user
 
  @apiDescription Retrieve the details for a specific station board given a CRS code.
 
  @apiParam {Number} crs A CRS short-code of the station. These codes can be found on National Rail Enquiries website.
  @apiParam {String} apikey The API Key from Darwin OpenLBDWS.
  @apiParam {Boolean} departures Boolean stating whether departures are requested (Either departures or arrivals required).
  @apiParam {Boolean} arrivals Boolean stating whether arrivals are requested (Either departures or arrivals required).
  @apiParam {String} destination The destination as a CRS code where the service is going.
  @apiParam {String} origin The origin as a CRS code where the service is coming from.
 
  @apiSuccess {String}   arrival       The time of arrival.
  @apiSuccess {String}   departure     The time for departure.
  @apiSuccess {Date}     destination   The destination of the service.
  @apiSuccess {Number}   platform      The platform number.

  @apiExample Example usage:
  curl -i http://darwin.hacktrain.com/board/EUS?apikey=YOUR-API-KEY

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

  @apiError NoApiKey No APIKEY provided.
 
  @apiErrorExample NoApiKey Error Response Example:
      HTTP/1.1 401 Not Authenticated
      {
          "message": {
            "apikey": "(Your Darwin API Key)  Missing required parameter in the JSON body or the post body or the query string"
          }
      }
"""
api.add_resource(StationBoard, '/board/<string:crs>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
