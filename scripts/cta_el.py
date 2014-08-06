"""
Script for pulling train times from CTA train tracker API for a specific stop ID,
for displaying via Arduino Yun on an LCD.

Requires CTA_TRAIN_TRACKER_API_KEY constant set in config.py.

Usage:

  python cta_el.py stopid

e.g:
  
  python cta_el.py '30282'

To find a specific stop id, you'll need to refer to the Stop List Quick Reference Zipfile, which you can download from here: http://www.transitchicago.com/developers/ttdocs/#_Toc296199909

Necesary to first install python-expat on Yun -- SSH in and run:
  opkg update
  opkg install python-expat
"""
import sys
import datetime
import urllib2
import xml.etree.ElementTree as ET
import config


STOP_ID = sys.argv[1]
DELIMETER = ' '

def get_xml_from_api():
  api_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=" + config.CTA_TRAIN_TRACKER_API_KEY + "&stpid=" + STOP_ID
  return urllib2.urlopen(api_url).read()

def extract_minutes_from_xml(xml):
  tree = ET.fromstring(xml)
  out = []
  for elem in tree.findall('eta/arrT'):
    datestr = elem.text
    minutes = get_minutes_from_now(datestr)
    out.append(minutes)
  return out

def get_minutes_from_now(datestr):
  now = datetime.datetime.now()
  obj = datetime.datetime.strptime(datestr, '%Y%m%d %H:%M:%S')
  delta = obj - now
  minutes = delta.total_seconds() / 60
  return int(round(minutes))


xml = get_xml_from_api()
# xml = '''<?xml version="1.0" encoding="utf-8"?><ctatt><tmst>20140708 20:16:54</tmst><errCd>0</errCd><errNm /><eta><staId>41460</staId><stpId>30282</stpId><staNm>Irving Park</staNm><stpDe>Service toward Loop</stpDe><rn>429</rn><rt>Brn</rt><destSt>30249</destSt><destNm>Loop</destNm><trDr>5</trDr><prdt>20140708 20:15:55</prdt><arrT>20140708 20:20:55</arrT><isApp>0</isApp><isSch>0</isSch><isDly>0</isDly><isFlt>0</isFlt><flags /><lat>41.96621</lat><lon>-87.6941</lon><heading>89</heading></eta><eta><staId>41460</staId><stpId>30282</stpId><staNm>Irving Park</staNm><stpDe>Service toward Loop</stpDe><rn>424</rn><rt>Brn</rt><destSt>0</destSt><destNm>Loop</destNm><trDr>5</trDr><prdt>20140708 20:16:42</prdt><arrT>20140708 20:29:42</arrT><isApp>0</isApp><isSch>1</isSch><isDly>0</isDly><isFlt>0</isFlt><flags /><lat /><lon /><heading /></eta></ctatt>'''
# print(xml)
minutes = extract_minutes_from_xml(xml)
minutes_str = DELIMETER.join(map(str, minutes))

print(minutes_str)

