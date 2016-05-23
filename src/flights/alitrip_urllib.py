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
    
    # headers[":authority"] = "sijipiao.alitrip.com"
    # headers[":method"] = "GET"
    # headers[":path"] = "/ie/flight_searcher.htm?searchBy=1281&b2g=0&formNo=-1&agentId=-1&tripType=1&depCityName=%B3%C9%B6%BC&depCity=CTU&arrCityName=%BA%FA%D6%BE%C3%F7%CA%D0&arrCity=SGN&depDate=2016-05-15&arrDate=2016-05-17&cardId="
    # headers[":scheme"] = "https"
    headers["authority"] = "sijipiao.alitrip.com"
    headers["method"] = "GET"
    headers["path"] = "/ie/flight_searcher.htm?searchBy=1281&b2g=0&formNo=-1&agentId=-1&tripType=1&depCityName=%B3%C9%B6%BC&depCity=CTU&arrCityName=%BA%FA%D6%BE%C3%F7%CA%D0&arrCity=SGN&depDate=2016-05-15&arrDate=2016-05-17&cardId="
    headers["scheme"] = "https"
    headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    headers["accept-encoding"] = "gzip, deflate, sdch"
    headers["accept-language"] = "en-US,en;q=0.8,de-DE;q=0.6,de;q=0.4"
    headers["cookie"] = "orderBy=undefined; cna=BaCUD0iUcxQCAW8JseqUNmxX; uss=U7KrNWkROJbJykFwT%2FLPuoJVlJp%2FhKlcgaj95YO3Bxv98P8DOAmkZKM%3D; tracknick=oldseedling; cookie2=1ab5280e3ee1cde301d04426756de072; t=b329f85021ccf41822767ae95b9e96c1; _tb_token_=CJAKFK1UGrME; l=AktLl5lYWGrJSUKc-YXAjGXWW/U0d19i"
    # headers["referer:https"] = "//sijipiao.alitrip.com/ie/flight_searcher.htm?searchBy=1281&spm=181.7091613.a1z67.1002&tripType=1&depCityName=%B3%C9%B6%BC&depCity=CTU&depDate=2016-05-15&arrCityName=%BA%FA%D6%BE%C3%F7%CA%D0&arrCity=SGN&arrDate=2016-05-17"
    headers["referer"] = "//sijipiao.alitrip.com/ie/flight_searcher.htm?searchBy=1281&spm=181.7091613.a1z67.1002&tripType=1&depCityName=%B3%C9%B6%BC&depCity=CTU&depDate=2016-05-15&arrCityName=%BA%FA%D6%BE%C3%F7%CA%D0&arrCity=SGN&arrDate=2016-05-17"
    headers["upgrade-insecure-requests"] = "1"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"

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
        
        self.full_url = 'https://sijipiao.alitrip.com/ie/flight_searcher.htm?searchBy=1281&b2g=0&formNo=-1&agentId=-1&tripType=1&depCityName=%B3%C9%B6%BC&depCity=CTU&arrCityName=%BA%FA%D6%BE%C3%F7%CA%D0&arrCity=SGN&depDate=2016-05-15&arrDate=2016-05-17&cardId='
        
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