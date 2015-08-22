
from nredarwin.webservice import DarwinLdbSession

DARWIN_WSDL='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2015-05-14'

def _get_darwin_session(api_key):
    return DarwinLdbSession(
        wsdl=DARWIN_WSDL, 
        api_key=api_key)

def _get_formatted_locations(locations):
    locat = []
    for d in locations:
        curr_locat = {
            "location": d.location_name,
            "crs": d.crs
        }
        locat.append(curr_locat)

    return locat


def get_station_board(
        api_key, 
        crs_code,
        departures,
        arrivals,
        destination,
        origin, 
        all_fields):

    crs_upper = crs_code.upper()

    darwin_session = _get_darwin_session(api_key)

    station_board = darwin_session.get_station_board(
                        crs_upper,
                        include_departures=departures,
                        include_arrivals=arrivals,
                        destination_crs=destination,
                        origin_crs=origin)

    response = []

    for station in station_board.train_services:
        board = {}

        # BASIC FIELDS
        board["platform"] = station.platform
        board["destination"] = station.destination_text
        board["origin"] = station.origin_text
        board["arrival"] = station.std
        board["departure"] = station.etd
        board["platform"] = station.platform

        if all_fields:
            board["destinations"] = _get_formatted_locations(station.destinations)
            board["origins"] = _get_formatted_locations(station.origins)
            board["operatorCode"] = station.operator_code
            board["operatorName"] = station.operator_name

        # TODO:
        print station.service_id
        
        response.append(board)

    return response

def get_service_details(api_key, id):

    darwin_session = _get_darwin_session(api_key)

    service_details = darwin_session.get_service_details(id)

    return service_details