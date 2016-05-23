#_*_ coding: utf8 _*_

import random
import urllib, urllib2
from bs4 import *
import webbrowser
import mechanize
import time
import gzip, StringIO

def gen_headers():
    headers = {}
    headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    headers["Accept-Encoding"] = "gzip, deflate"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "QN99=4828"
    headers["Host"] = "www.qua.com"
    headers["Referer"] = "http://www.qua.com/flights/CTU-SGN/2016-05-29/2016-06-05?from=home"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0"
    headers["X-Requested-With"] = "XMLHttpRequest"
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
        host = 'english.ctrip.com'
        referer = 'http://english.ctrip.com/flights/home?searchboxArg=t'
        headers = gen_headers()
        data = None
        
        print self.full_url
        
        self.full_url = 'http://www.qua.com/twell/en/groupdata?queryID=10.86.213.8%3A-5e291d1a%3A154854b54a3%3A61e7&from=home&_=1463204613420'
        
        req = urllib2.Request(self.full_url, data, headers)
        response = urllib2.urlopen(req)
        html = response.read()
        
        #=======================================================================
        # br = mechanize.Browser()
        # 
        # req = br.open(self.full_url)
        # 
        # time.sleep(3)
        # html = req.read()
        #=======================================================================

        compressedStream=StringIO.StringIO(html)
        gzipper=gzip.GzipFile(fileobj=compressedStream)
        data=gzipper.read()
        
        with open("results.html", "w") as f:
                    f.write(data)
  
        webbrowser.open("results.html")
          
        # html = urllib2.urlopen('http://english.ctrip.com/flights/chongqing-to-ho-chi-minh-city/tickets-ckg-sgn/?flighttype=s&dcity=ckg&acity=sgn&relddate=0&startdate=2016-05-06&startday=fri&relweek=0&searchboxArg=t')
          
        print data
if __name__ == '__main__':
    get_filght = getFilght()
    get_filght.get_flights()