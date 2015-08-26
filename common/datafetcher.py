from bs4 import BeautifulSoup
import urllib2
import json
import os

## Initialization

## This stations_and_codes variable contains an dictionary where the keys are station CRS
## codes and the value is their respective printable station name.
filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/stationcodes.json'))
with open(filepath) as json_file:
    stations_and_codes = json.load(json_file)


## TODO
filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/stationdata.json'))
with open(filepath) as json_file:
    stations_data = json.load(json_file)

def get_ldbws_status():
    """
    This function retreives the url for the OpenLDBWS status and returns
    a string of the value it contains.

    Currently the way this is built is very fragile, as any changes in 
    the website would break it. Good thing is, the website will rarely change...
    """
    page = urllib2.urlopen("http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/").read()
    status_soup = BeautifulSoup(page, "lxml")
    # We get the span elements. There are only 2 span elements
    # of which they contain the status for the OpenLDBWS API
    # and the OpenLDBWS registration - we're only interested on the former
    status_elm = status_soup.findAll("span")
    # We extract the text from the first one and return it
    status_text = status_elm[0].findAll(text=True)
    
    return status_text[0]


def get_stations_and_codes(query):
    """
    This function returns all an array of objects containing stations 
    and their respective station codes for all the instances that are
    matched with the query given by the parameter.
    """

    found_stations = stations_and_codes

    if query:
        found_stations = (dict((k, v) 
                            for k, v in stations_and_codes.items() 
                            if query.upper() in v.upper()))

    return found_stations

def get_stations_metadata(query):
    """
    This function returns not only the codes for the stations, but as well
    it returns the details of the stations, such as geolocation, etc.
    """
    found_stations = stations_data

    if query:
        found_stations = [i for i in stations_data 
                            if query.upper() in i["crs"].upper()]

    return found_stations

