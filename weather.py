# python weather.py

# http://weather.yahooapis.com/forecastrss?w=2379574

import sys
import urllib2
import xml.etree.ElementTree as ET


WOEID = '2379574'

def get_xml_from_api():
  api_url = "http://weather.yahooapis.com/forecastrss?w=" + WOEID
  return urllib2.urlopen(api_url).read()

xml = get_xml_from_api()
# print(xml)
tree = ET.fromstring(xml)

item = tree.find("channel/item")
condition = item.find('yweather:condition', {'yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0'})
forecast = item.find('yweather:forecast', {'yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0'})

print(condition.attrib['temp'] + ' ' + condition.attrib['text'])
print('H:' + forecast.attrib['high'] + ' L:' + forecast.attrib['low'])

