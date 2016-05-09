from selenium import webdriver
import random

driver = webdriver.Chrome()
driver.get('http://www.qua.com/flights/CTU-SGN/2016-05-21/2016-05-28?from=flight_home')

result_intl_table = driver.find_element_by_id('flightList')

flights = result_intl_table.find_elements_by_class_name('result_table')

for flight in flights:
    print flight.get_attribute('innerHTML')
    
    
