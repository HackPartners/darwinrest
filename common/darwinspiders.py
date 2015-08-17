from bs4 import BeautifulSoup
import urllib2

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
