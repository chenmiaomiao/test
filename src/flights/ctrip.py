from selenium import webdriver
import random

driver = webdriver.Chrome()
driver.get('http://english.ctrip.com/flights/chengdu-to-ho-chi-minh-city/tickets-ckg-sgn/?flighttype=d&acity=sgn&returndate=2016-05-17&dcity=ckg&startdate=2016-05-13')

result_intl_table = driver.find_element_by_id('flightList')

flights = result_intl_table.find_elements_by_class_name('result_table')

for flight in flights:
    print flight.get_attribute('innerHTML')
    
    
