#_*_ coding: utf8 _*_

import random
import urllib, urllib2
from bs4 import *
import webbrowser
import mechanize
import time

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
        host = 'english.ctrip.com'
        referer = 'http://english.ctrip.com/flights/home?searchboxArg=t'
        headers = gen_headers(host, referer)
        data = None
        
        print self.full_url
        
        self.full_url = 'http://english.ctrip.com/flights/chengdu-to-ho-chi-minh-city/tickets-ctu-sgn/?flighttype=d&dcity=ctu&acity=sgn&relddate=0&relrdate=1&startdate=2016-05-06&returndate=2016-05-07&startday=fri&returnday=sat&relweek=0&searchboxArg=t'
        
        #=======================================================================
        # req = urllib2.Request(self.full_url, data)
        # response = urllib2.urlopen(req)
        # html = response.read()
        #=======================================================================
        
        br = mechanize.Browser()
        
        req = br.open(self.full_url)
        
        time.sleep(3)
        html = req.read()
        
        with open("results.html", "w") as f:
            f.write(html)
  
        webbrowser.open("results.html")
          
        # html = urllib2.urlopen('http://english.ctrip.com/flights/chongqing-to-ho-chi-minh-city/tickets-ckg-sgn/?flighttype=s&dcity=ckg&acity=sgn&relddate=0&startdate=2016-05-06&startday=fri&relweek=0&searchboxArg=t')
          
        print html
if __name__ == '__main__':
    get_filght = getFilght()
    get_filght.get_flights()