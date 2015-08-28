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
  @api {get} /api/status /status
  @apiVersion 0.0.1
  @apiName Darwin API services status
  @apiGroup Status
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
  @api {get} /api/station/code/:query /station/code
  @apiVersion 0.0.1
  @apiName Station codes
  @apiGroup Station
  @apiPermission public

  @apiDescription Retreive either all station CRS codes, or a subset of codes

  @apiParam (URL Parameters) {String} [query] (Optional) A query to find all stations that contain this string.

  @apiExample Code Query Example:
  curl -i http://darwin.hacktrain.com/api/station/code/eus

  @apiSuccessExample Simple query request:
  # Query http://darwin.hacktrain.com/api/station/code/eus
  {
    "EUS": "Euston"
  }

  @apiSuccessExample All CRS Codes request:
  # Query http://darwin.hacktrain.com/api/station/code
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
api.add_resource(StationCrs, '/api/station/code', '/api/station/code/<string:query>')

"""
  @api {get} /api/station/detail/:query /station/detail
  @apiVersion 0.0.1
  @apiName Station details
  @apiGroup Station
  @apiPermission public

  @apiDescription Retreive metadata about the stations, including location, sttaion code, etc.

  @apiParam (URL Parameters) {String} [query] (Optional) A query to find all stations that contain this string in the station name.

  @apiExample Code Query Example:
  # Query http://darwin.hacktrain.com/api/station/detail/eus
  [
    {
        "crs": "EUS", 
        "owner": "Network Rail", 
        "postcode": "NW1 2RT, UK", 
        "stationName": "Euston"
    }
  ]

  @apiExample Query all stations:
  # Query http://darwin.hacktrain.com/api/station/detail
  [
    {
        "crs": "ABW", 
        "owner": "Southeastern", 
        "postcode": "SE2 9RH, UK", 
        "stationName": "Abbey Wood"
    }, 
    {
        "crs": "ABE", 
        "owner": "Arriva Trains Wales", 
        "postcode": "CF83 1AQ, UK", 
        "stationName": "Aber"
    }, 
    ...
  ]

"""
api.add_resource(StationMetaData, '/api/station/detail', '/api/station/detail/<string:query>')


"""
  @api {get} /api/train/:station /train/:station
  @apiVersion 0.0.1
  @apiName Station train
  @apiGroup Train
  @apiPermission public
 
  @apiDescription Retreive arrival and departure services at station requested.
"""
"""
  @api {get} /api/train/:station/from /train/:station/from
  @apiVersion 0.0.1
  @apiName Station train arrivals
  @apiGroup Train
  @apiPermission public
 
  @apiDescription Retreive arrival services at station requested.
""" 
"""
  @api {get} /api/train/:station/to /train/:station/to
  @apiVersion 0.0.1
  @apiName Station train departures
  @apiGroup Train
  @apiPermission public
 
  @apiDescription Retreive departure services at station requested.
"""  
"""
  @api {get} /api/train/:station/{from|to}/:station2 /train/:station1/{from|to}/:station2
  @apiVersion 0.0.1
  @apiName Station train with secondary
  @apiGroup Train
  @apiPermission public
 
  @apiDescription Retreive arrival/departure services at station requested, towards/from a secondary sation.
  

  @apiParam (URL Parameters) {Number} station Station name or CRS code.
  @apiParam (URL Parameters) {String} [direction] (Optional) Parameter can be 'to' or 'from'. 'to' would display departures, 'from' would display arrivals.
  @apiParam (URL Parameters) {String} [station2] (Optional) Secondary station to filter to/from. If empty, it would display ALL stations.
  @apiParam (Query Parameters) {String} apiKey The API Key from Darwin OpenLBDWS.
  @apiParam (Query Parameters) {String} [rows] The number of rows to be retreived (default is 10).
 
  @apiSuccess (SUCCESS RESPONSE: HTTP 200) {String}   arrival       The time of arrival.
  @apiSuccess (SUCCESS RESPONSE: HTTP 200) {String}   departure     The time for departure.
  @apiSuccess (SUCCESS RESPONSE: HTTP 200) {Date}     destination   The destination of the service.
  @apiSuccess (SUCCESS RESPONSE: HTTP 200) {Number}   platform      The platform number.

  @apiExample Usage Simple Request:
  curl -i http://darwin.hacktrain.com/api/train/EUS?rows=2&apiKey=YOUR-API-KEY
  curl -i http://darwin.hacktrain.com/api/train/Euston/to?rows=2&apiKey=YOUR-API-KEY
  curl -i http://darwin.hacktrain.com/api/train/eus/from?rows=2&apiKey=YOUR-API-KEY
  curl -i http://darwin.hacktrain.com/api/train/Eus/to/manchester piccadilly?rows=2&apiKey=YOUR-API-KEY

  @apiSuccessExample Show two arrivals/departures in Euston:
  # Query http://darwin.hacktrain.com/api/train/EUS?apiKey=YOUR-API-KEY&rows=2 
  [
    {
        "destinations": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "estimatedArrivalTime": "On time", 
        "estimatedDepartureTime": null, 
        "operatorCode": "LO", 
        "operatorName": "London Overground", 
        "origins": [
            {
                "stationCode": "WFJ", 
                "stationName": "Watford Junction"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": "06:58", 
        "scheduledDepartureTime": null, 
        "serviceId": "PGNBaWyyxk+/9QaM6/qJfg=="
    }, 
    {
        "destinations": [
            {
                "stationCode": "BHM", 
                "stationName": "Birmingham New Street"
            }
        ], 
        "estimatedArrivalTime": null, 
        "estimatedDepartureTime": "On time", 
        "operatorCode": "VT", 
        "operatorName": "Virgin Trains", 
        "origins": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": null, 
        "scheduledDepartureTime": "07:03", 
        "serviceId": "U1mT5TgI+OtTvJdX/YUw3g=="
    }
  ]

  @apiSuccessExample Show two departures from Euston:
  # Query http://darwin.hacktrain.com/api/train/EUS/to?apiKey=YOUR-API-KEY&rows=2 
  [
    {
        "destinations": [
            {
                "stationCode": "BHM", 
                "stationName": "Birmingham New Street"
            }
        ], 
        "estimatedArrivalTime": null, 
        "estimatedDepartureTime": "On time", 
        "operatorCode": "VT", 
        "operatorName": "Virgin Trains", 
        "origins": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": null, 
        "scheduledDepartureTime": "07:03", 
        "serviceId": "U1mT5TgI+OtTvJdX/YUw3g=="
    }, 
    {
        "destinations": [
            {
                "stationCode": "TRI", 
                "stationName": "Tring"
            }
        ], 
        "estimatedArrivalTime": null, 
        "estimatedDepartureTime": "On time", 
        "operatorCode": "LM", 
        "operatorName": "London Midland", 
        "origins": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": null, 
        "scheduledDepartureTime": "07:05", 
        "serviceId": "U4fjw0Pa5LGyiqSSe4iVfw=="
    }
  ]

  @apiSuccessExample Show two arrivals at Euston:
  # Query http://darwin.hacktrain.com/api/train/EUS/from?apiKey=YOUR-API-KEY&rows=2 
  [
    {
        "destinations": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "estimatedArrivalTime": "07:00", 
        "estimatedDepartureTime": null, 
        "operatorCode": "VT", 
        "operatorName": "Virgin Trains", 
        "origins": [
            {
                "stationCode": "BHM", 
                "stationName": "Birmingham New Street"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": "07:05", 
        "scheduledDepartureTime": null, 
        "serviceId": "MkleuTHM5ectE6FH3gqJeQ=="
    }, 
    {
        "destinations": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "estimatedArrivalTime": "06:33", 
        "estimatedDepartureTime": null, 
        "operatorCode": "CS", 
        "operatorName": "Caledonian Sleeper", 
        "origins": [
            {
                "stationCode": "GLC", 
                "stationName": "Glasgow Central"
            }, 
            {
                "stationCode": "EDB", 
                "stationName": "Edinburgh"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": "07:07", 
        "scheduledDepartureTime": null, 
        "serviceId": "GfHrh9RjISGaAUSKcgm+4g=="
    }
  ]

  @apiSuccessExample Show two services towards manchester:
  # Query http://darwin.hacktrain.com/api/train/EUS/manchester piccadilly?apiKey=YOUR-API-KEY&rows=2 
  [
    {
        "destinations": [
            {
                "stationCode": "MAN", 
                "stationName": "Manchester Piccadilly"
            }
        ], 
        "estimatedArrivalTime": null, 
        "estimatedDepartureTime": "On time", 
        "operatorCode": "VT", 
        "operatorName": "Virgin Trains", 
        "origins": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": null, 
        "scheduledDepartureTime": "07:20", 
        "serviceId": "uLG1cVJVkAj3QojNJaCqPA=="
    }, 
    {
        "destinations": [
            {
                "stationCode": "MAN", 
                "stationName": "Manchester Piccadilly"
            }
        ], 
        "estimatedArrivalTime": null, 
        "estimatedDepartureTime": "On time", 
        "operatorCode": "VT", 
        "operatorName": "Virgin Trains", 
        "origins": [
            {
                "stationCode": "EUS", 
                "stationName": "London Euston"
            }
        ], 
        "platform": null, 
        "scheduledArrivalTime": null, 
        "scheduledDepartureTime": "07:35", 
        "serviceId": "RvS3rQNXy8JBgRNrgIBdmw=="
    }
  ]

"""
api.add_resource(
  StationBoard, 
  '/api/train/<string:station>',
  '/api/train/<string:station>/<string:direction>',
  '/api/train/<string:station>/<string:direction>/<string:secondaryStation>')


"""
  @api {get} /api/service/:id /service
  @apiVersion 0.0.1
  @apiName Service details
  @apiGroup Service
  @apiPermission user
 
  @apiDescription Retrieve the details for a specific service given a service ID.
 
  @apiParam (URL Parameters) {Number} Id The id for the service that is to be retreived.
  @apiParam (URL Parameters) {Number} [allFields] A flag that states whether all fields should be included.
  
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
