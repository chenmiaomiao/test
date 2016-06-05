import pprint
import json
import urllib2

a = urllib2.urlopen("https://sijipiao.alitrip.com/ie/flight_search_poller.do?_ksTS=1462540408929_1011&callback=jsonp1012&searchBy=tbsearch&depCity=CTU&arrCity=SGN&depDate=2016-05-13&arrDate=2016-05-17&tripType=1&agentId=-1&queryRecordId=50f09b9bd8244cf69ee66f4b4d4876a2&mode=outbound&b2g=0&formNo=-1&cardId=")

c = a.read()

print c

b = json.loads(c)

pprint(b)