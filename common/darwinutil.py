
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
            "stationName": d.location_name,
            "stationCode": d.crs
        }
        locat.append(curr_locat)

    return locat

def _get_calling_point_lists(calling_point_lists):
    response = []
    for cp_list in calling_point_lists:
        response_container = {}
        response_container["serviceType"] = cp_list.service_type
        response_container["changeRequired"] = cp_list.service_change_required
        response_container["isCancelled"] = cp_list.association_is_cancelled

        response_container["callingPoints"] = []

        for cp in cp_list.calling_points:
            response_item = {}
            response_item["locationName"] = cp.location_name
            response_item["stationCode"] = cp.crs
            response_item["actualTime"] = cp.at
            response_item["estimatedTime"] = cp.et
            response_item["scheduledTime"] = cp.st
            
            response_container["callingPoints"].append(response_item)

        response.append(response_container)
    return response

def get_station_board(
        api_key, 
        station_code,
        departures,
        arrivals,
        destination,
        origin,
        rows):

    darwin_session = _get_darwin_session(api_key)

    station_board = darwin_session.get_station_board(
                        station_code,
                        include_departures=departures,
                        include_arrivals=arrivals,
                        destination_crs=destination,
                        origin_crs=origin,
                        rows=rows)

    response = []

    for station in station_board.train_services:
        board = {}

        # BASIC FIELDS
        board["platform"] = station.platform
        board["scheduledDepartureTime"] = station.std
        board["estimatedDepartureTime"] = station.etd
        board["scheduledArrivalTime"] = station.sta
        board["estimatedArrivalTime"] = station.eta
        board["platform"] = station.platform
        board["serviceId"] = station.service_id
        board["destinations"] = _get_formatted_locations(station.destinations)
        board["origins"] = _get_formatted_locations(station.origins)
        board["operatorCode"] = station.operator_code
        board["operatorName"] = station.operator_name

        response.append(board)

    return response

def get_service_details(api_key, service_id, all_fields=False):

    darwin_session = _get_darwin_session(api_key)

    service_details = darwin_session.get_service_details(service_id)

    service_response = {}
    # standard fields
    service_response["isCancelled"] = service_details.is_cancelled
    service_response["locationName"] = service_details.location_name
    service_response["stationCode"] = service_details.crs
    service_response["platform"] = service_details.platform
    service_response["scheduledArrivalTime"] = service_details.sta
    service_response["scheduledDepartureTime"] = service_details.std
    service_response["operatorCode"] = service_details.operator_code
    service_response["operatorName"] = service_details.operator_name

    if all_fields:
        service_response["disruptionReason"] = service_details.disruption_reason
        service_response["generatedAt"] = str(service_details.generated_at)
        service_response["actualArrivalTime"] = service_details.ata
        service_response["actualDepartureTime"] = service_details.atd
        service_response["estimatedArrivalTime"] = service_details.eta
        service_response["estimatedDepartureTime"] = service_details.etd

        service_response["subsequentCallingPointList"] = _get_calling_point_lists(service_details.subsequent_calling_point_lists)
        service_response["previousCallingPointList"] = _get_calling_point_lists(service_details.previous_calling_point_lists)

    print service_details.previous_calling_point_lists
    print service_details.subsequent_calling_point_lists
    print service_details.previous_calling_points
    print service_details.subsequent_calling_points

    return service_response


