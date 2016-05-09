#_*_ coding: utf8 _*_

import random
import urllib, urllib2
from bs4 import *
import webbrowser
import mechanize
import time
import json
import pprint

def gen_headers(host, referer):
    headers = {}
    
    headers['Host'] = host
    headers['Referer'] = referer
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    headers['Accept-Language'] = "en-US,en;q=0.8,de-DE;q=0.6,de;q=0.4"
    # headers['Accept-Encoding'] = 'gzip, deflate, sdch'
    headers['Keep-Alive'] = '300'
    headers['Connection'] = 'keep-alive'
    headers['Cache-Control'] = 'max-age=0'
    headers['Accept'] = 'text/html, */*; q=0.01'
    headers['X-Requested-With'] = 'XMLHttpRequest'
    headers['DNT'] = '1'

    return headers

def get_full_url(url_root, url_dict):
    url_para = urllib.urlencode(url_dict)
    
    return url_root+url_para
    
def get_ctrip_url(dcity, acity, url_dict):
    url_root = 'http://english.ctrip.com/flights/chengdu-to-ho-chi-minh-city/tickets-' + dcity + '-' + acity + '/?'
    
    return get_full_url(url_root, url_dict)
    
class getFilght():
    def __init__(self):
        url_ctrip_dict = {'flighttype': 'd', 
                          'dcity': 'ckg', 
                          'acity': 'sgn', 
                          'startdate': '2016-05-06', 
                          'returndate': '2016-05-07'
                          }
        self.full_url = get_ctrip_url(url_ctrip_dict['dcity'], url_ctrip_dict['acity'], url_ctrip_dict)
        
    def get_flights(self):
        host = 'sijipiao.alitrip.com'
        referer = 'https://s.taobao.com/search?q=%E6%9C%BA%E7%A5%A8&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160506'
        headers = gen_headers(host, referer)
        data = None
        
        print self.full_url
        
        self.full_url = 'https://sijipiao.alitrip.com/ie/flight_search_poller.do?_ksTS=1462540408929_1011&callback=jsonp1012&searchBy=tbsearch&depCity=CTU&arrCity=SGN&depDate=2016-05-13&arrDate=2016-05-17&tripType=1&agentId=-1&queryRecordId=50f09b9bd8244cf69ee66f4b4d4876a2&mode=outbound&b2g=0&formNo=-1&cardId='
        
        req = urllib2.Request(self.full_url, data, headers)
        response = urllib2.urlopen(req)
        html = response.read()
        
        flights_info = json.loads(html)
        pprint(flights_info)
        # br = mechanize.Browser()
        
        # req = br.open(self.full_url)
        
        # time.sleep(3)
        # html = req.read()
        
        with open("results.html", "w") as f:
            f.write(html)
  
        webbrowser.open("results.html")
        
        f.close()
          
        # html = urllib2.urlopen('http://english.ctrip.com/flights/chongqing-to-ho-chi-minh-city/tickets-ckg-sgn/?flighttype=s&dcity=ckg&acity=sgn&relddate=0&startdate=2016-05-06&startday=fri&relweek=0&searchboxArg=t')
          
        print html
if __name__ == '__main__':
    get_filght = getFilght()
    get_filght.get_flights()