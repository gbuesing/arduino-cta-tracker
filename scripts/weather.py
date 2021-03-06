# python scripts/weather.py current

# http://weather.yahooapis.com/forecastrss?w=2379574

import sys
import urllib2
import xml.etree.ElementTree as ET


WOEID = '2379574' # Chicago, IL
QUERY = sys.argv[1]
XML_NS = {'yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0'}

def get_xml_from_api():
  api_url = "http://weather.yahooapis.com/forecastrss?w=" + WOEID
  return urllib2.urlopen(api_url).read()

xml = get_xml_from_api()
# print(xml)

tree = ET.fromstring(xml)


if 'current' == QUERY:
  condition = tree.find('channel/item/yweather:condition', XML_NS)
  print(condition.attrib['temp'] + ' ' + condition.attrib['text'])

if 'forecast' == QUERY:
  forecast = tree.find('channel/item/yweather:forecast', XML_NS)
  print('High ' + forecast.attrib['high'] + ' Low ' + forecast.attrib['low'])

if 'sunset' == QUERY:
  astronomy = tree.find('channel/yweather:astronomy', XML_NS)
  print(astronomy.attrib['sunrise'] + '/' + astronomy.attrib['sunset'])
