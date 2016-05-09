# _*_ coding: utf8 _*_

import urllib2
from selenium import webdriver
import webbrowser
import  urlparse
from urllib import urlencode
import time
from selenium.webdriver.support.ui import WebDriverWait
import pprint
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from lxml import etree as ET
import re
import sqlite3

#===============================================================================
# req = urllib2.urlopen("https://sijipiao.alitrip.com/ie/flight_searcher.htm?searchBy=1281&b2g=0&formNo=-1&agentId=-1&tripType=1&depCity=CKG&arrCity=SGN&depDate=2016-05-13&arrDate=2016-05-17&cardId=")
# html = req.read()
# with open('alitrip_results.html', 'w') as fhand:
#     fhand.write(html)
# webbrowser.open('alitrip_results.html')
# print html
#===============================================================================

# driver = webdriver.PhantomJS(executable_path='C:/PROGRAMS/phantomjs.exe')
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 60)

conn = sqlite3.connect('flights.sqlite')
cur = conn.cursor()

# convert date to string, vice versa
def date_interconvert(date_data):
    if type(date_data) != datetime:
        return datetime.strptime(date_data, '%Y-%m-%d')
    if type(date_data)== datetime:
        return date_data.strftime('%Y-%m-%d')

def update_url(hotname, parameters, new_dict):
    url_dict = urlparse.parse_qs(parameters)
        
    for key in new_dict.keys():
        url_dict[key] = new_dict[key]
    
    new_parameters = urlencode(url_dict, True)
    
    return hotname+new_parameters

def gen_alitrip_url(dep_city, arr_city, dep_date, arr_date):
    default_hotname = 'https://sijipiao.alitrip.com/ie/flight_searcher.htm?'
    default_parameters = 'searchBy=1281&b2g=0&formNo=-1&agentId=-1&tripType=1&depCity=CKG&arrCity=SGN&depDate=2016-05-13&arrDate=2016-05-17&cardId='

    new_dict = {}
    new_dict['depCity'] = dep_city
    new_dict['arrCity'] = arr_city
    new_dict['depDate'] = date_interconvert(dep_date)
    new_dict['arrDate'] = date_interconvert(arr_date)
    
    full_url = update_url(default_hotname, default_parameters, new_dict)
    
    return full_url

#===============================================================================
# def parse_flight(flight_raw):
#     # get flight_raw info
#     wait.until(lambda driver: driver.find_element_by_xpath(".//span[@class='J_line']").is_displayed())
#     flight_info_raw = flight_raw.find_elements_by_xpath(".//span[@class='J_line']")
#     flight_info = map(lambda each: each.text, flight_info_raw)
#     
#     # get time
#     wait.until(lambda driver: driver.find_element_by_xpath(".//td[@class='col-time']/div").is_displayed())
#     time_raw = flight_raw.find_elements_by_xpath(".//td[@class='col-time']/div")
#     time = map(lambda each_seg: [each_part.text for each_part in each_seg.find_elements_by_xpath(".//p/span")], time_raw)
#     
#     # get airport
#     wait.until(lambda driver: driver.find_element_by_xpath(".//td[@class='col-airport']/div/div").is_displayed())
#     airport_raw = flight_raw.find_elements_by_xpath(".//td[@class='col-airport']/div/div")
#     airport = map(lambda each: each.text, airport_raw)
#     
#     # get totaltime
#     wait.until(lambda driver: driver.find_element_by_xpath(".//td[@class='col-totaltime']/div").is_displayed())
#     totaltime_raw = flight_raw.find_elements_by_xpath(".//td[@class='col-totaltime']/div")
#     totaltime = map(lambda each: each.text, totaltime_raw)
#     
#     # get price
#     wait.until(lambda driver: driver.find_element_by_xpath(".//td[@class='col-price']//p[@class='total-price']/span").is_displayed())
#     price_raw = flight_raw.find_elements_by_xpath(".//td[@class='col-price']//p[@class='total-price']/span")
#     price = map(lambda each: each.text, price_raw)
#     
#     return flight_info, time, airport, totaltime, price
#===============================================================================

def parse_flight(flight_raw):
    html = flight_raw.get_attribute('innerHTML')
    bs = BeautifulSoup(html, 'html.parser')
    
    tds = bs('td')
    
    flight_info = []
    flight_time = []
    flight_airport = []
    valid_flight = 0
    
    for td in tds:            
        if 'col-flightinfo' in td['class']:
            airlines = td.find_all('span', attrs = {'class': 'J_line'})
            for airline in airlines:
                flight_info.append(airline.string)
            if len(flight_info) > 0:
                valid_flight += 1
                
        elif 'col-time' in td['class']:
            time_all = td.find_all('div', class_ = re.compile("time"))
            for time_per_airline in time_all:
                dep_and_arr = time_per_airline.find_all('span')
                flight_time.append([each.string for each in dep_and_arr])
            if len(flight_time) > 0:
                valid_flight +=1
            
        elif 'col-airport' in td['class']:
            airport_all = td.div.find_all('div')
            for airport in airport_all:
                flight_airport.append(''.join(airport.strings))
            if len(flight_airport) > 0:
                valid_flight +=1
                
        elif 'col-totaltime' in td['class']:
            totaltime = td.div.string
            totaltime_number = re.findall('\D*(\d+)\D*', totaltime)[0]
            if len(totaltime_number) > 0:
                valid_flight += 1
            
        elif 'col-price' in td['class']:
            price = ''.join(td.select_one(".total-price").span.strings)
            price_number = re.findall("\D*(\d+)\D*", price)[0]
            if len(price_number) > 0:
                valid_flight += 1
                
    if valid_flight == 5:    
        return flight_info[0], flight_time[0][0], flight_time[-1][-1], flight_airport[0], flight_airport[-1], totaltime_number, price_number
    else:
        return None
    
def get_flights(dep_city, arr_city, dep_date, arr_date):
    full_url = gen_alitrip_url(dep_city, arr_city, dep_date, arr_date)
    driver.get(full_url)
    
    # include tax in price
    wait.until(lambda driver: driver.find_element_by_xpath("//label[@for='notax']").is_displayed())
    tax_switch = driver.find_element_by_xpath("//label[@for='notax']")
    tax_switch.click()
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='J_DepResultContainer']").is_displayed())
    flights_raw = driver.find_elements_by_xpath("//div[@id='J_DepResultContainer']/div[@class='J_FlightItem item-root']")    
        
    for flight_raw in flights_raw:
        flight = []
        flight.extend(parse_flight(flight_raw))
        flight.extend((dep_city, arr_city, dep_date, arr_date))
        print flight
        cur.execute("INSERT INTO Flights (flightinfo, departuretime, arrivaltime, departureairport, arrivalairport, totaltime, price, departurecity, arrivalcity, leavedate, returndate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                    flight)
        conn.commit()
        
def find_best(days_min, days_max, date_start, date_end):
    cur.execute("DROP TABLE IF EXISTS Flights")
    cur.execute("CREATE TABLE IF NOT EXISTS Flights (flightinfo TEXT, departuretime TEXT, arrivaltime TEXT, departureairport TEXT, arrivalairport TEXT, totaltime INTEGER, price INTEGER, departurecity TEXT, arrivalcity TEXT, leavedate TEXT, returndate TEXT, type TEXT DEFAULT 'Leave')") 
    
    date_start = date_interconvert(date_start)
    date_end = date_interconvert(date_end)
    
    date_offset = timedelta(0)
    
    for date in range((date_end - date_start).days + 1):
        dep_date = date_start + date_offset
        arr_date = dep_date + timedelta(days_min-1)
        for days in range(days_max - days_min + 1):
            get_flights('CTU', 'SGN', dep_date, arr_date)
            arr_date += timedelta(1)
        date_offset += timedelta(1)
    
if __name__ == '__main__':    
    # get_flights('CKG', 'SGN', '2016-06-01', '2016-06-03')
    find_best(3, 5, '2016-05-10', '2016-05-30')
    
    cur.close()
    conn.close()
    print 'Eureka! '
