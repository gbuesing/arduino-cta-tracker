import sys
import datetime
import urllib2
import xml.etree.ElementTree as ET

# Southbound Damen & Irving Park:
#   python cta_bus.py '50' '8827'
#
# Northbound Damen & Irving Park:
#   python cta_bus.py '50' '8951'
#
# Westbound Irving Park & Wolcott
#   python cta_bus.py '80' 5686'
#
# Eastbound Irving Park & Wolcott
#   python cta_bus.py '80' 5661'

# Get stop ids for route:
#  curl 'http://www.ctabustracker.com/bustime/api/v1/getstops?key=key&rt=80&dir=Eastbound'

# date +'%l:%M%p %h %e'

API_KEY = 'key'
ROUTE_ID = sys.argv[1] 
STOP_ID = sys.argv[2]
DELIMETER = ' '

def get_xml_from_api():
  api_url = "http://www.ctabustracker.com/bustime/api/v1/getpredictions?key=" + API_KEY + "&rt=" + ROUTE_ID + "&stpid=" + STOP_ID
  return urllib2.urlopen(api_url).read()

def extract_minutes_from_xml(xml):
  tree = ET.fromstring(xml)
  out = []
  for elem in tree.findall('prd/prdtm'):
    datestr = elem.text
    minutes = get_minutes_from_now(datestr)
    out.append(minutes)
  return out

def get_minutes_from_now(datestr):
  now = datetime.datetime.now()
  obj = datetime.datetime.strptime(datestr, '%Y%m%d %H:%M')
  delta = obj - now
  minutes = delta.total_seconds() / 60
  return int(round(minutes))


xml = get_xml_from_api()
# print(xml)
minutes = extract_minutes_from_xml(xml)
minutes_str = DELIMETER.join(map(str, minutes))

print(minutes_str)


