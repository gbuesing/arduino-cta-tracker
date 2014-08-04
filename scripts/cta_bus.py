"""
Script for pulling bus times from CTA Bus Tracker API for a specific stop ID,
for displaying via Arduino Yun on an LCD.

Requires CTA_BUS_TRACKER_API_KEY constant set in config.py.

Usage:

  python cta_bus.py routeid stopid

e.g:
  
  python cta_bus.py '50' '8827'

To get stopids for a route:

  http://www.ctabustracker.com/bustime/api/v1/getstops?key=key&rt=80&dir=Eastbound

Necesary to first install python-expat on Yun -- SSH in and run:
  opkg update
  opkg install python-expat
"""
import sys
import datetime
import urllib2
import xml.etree.ElementTree as ET
import config

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

ROUTE_ID = sys.argv[1] 
STOP_ID = sys.argv[2]
DELIMETER = ' '

def get_xml_from_api():
  api_url = "http://www.ctabustracker.com/bustime/api/v1/getpredictions?key=" + config.CTA_BUS_TRACKER_API_KEY + "&rt=" + ROUTE_ID + "&stpid=" + STOP_ID
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


