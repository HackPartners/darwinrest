
from nredarwin.webservice import DarwinLdbSession

DARWIN_WSDL='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2015-05-14'

def _get_darwin_session(api_key):
    return DarwinLdbSession(
        wsdl=DARWIN_WSDL, 
        api_key=api_key)

def get_station_board(
        api_key, 
        crs_code,
        departures,
        arrivals,
        destination,
        origin):

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

        board["platform"] = station.platform
        board["destination"] = station.destination_text
        if arrivals: board["arrival"] = station.std
        if arrivals: board["departure"] = station.etd
        
        response.append(board)

    return response

def get_service_details(id):

    darwin_session = _get_darwin_session(api_key)

    service_details = darwin_session.get_service_details(id)

    return service_details