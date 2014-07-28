# python weather.py '2379574'

# http://weather.yahooapis.com/forecastrss?w=2379574

import sys
import urllib2
import xml.etree.ElementTree as ET


WOEID = sys.argv[1] 

def get_xml_from_api():
  api_url = "http://weather.yahooapis.com/forecastrss?w=" + WOEID
  return urllib2.urlopen(api_url).read()

xml = get_xml_from_api()

print(xml)
