# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:27:04 2022

@author: hnrne
"""

from itertools import zip_longest
from selenium import webdriver
from time import sleep
import csv
path = r'C:\Users\hnrne\Downloads\chromedriver_win32 (1)\chromedriver'
# open the browser
browser = webdriver.Chrome(executable_path=path)
# load the webpage
browser.get('https://www.amazon.in')
browser.maximize_window()
# get the input elements
input_search = browser.find_element_by_id('twotabsearchtextbox')
search_button = browser.find_element_by_xpath("(//input[@type='submit'])[1]")
# send the input to the webpage
input_search.send_keys("Smartphones under 10000")
sleep(1)
search_button.click()
products = []
prices=[]
ratings=[]
total=[]
for i in range(10):
    print('Scraping page', i+1)
    product = browser.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
    price= browser.find_elements_by_xpath("//span[@class='a-price-whole']")
    rating = browser.find_elements_by_xpath("//span[@class='a-size-base s-underline-text']")
    
   
    for p in product:
        products.append(p.text)
    for i in price:
        prices.append(i.text)
    for k in rating:
        ratings.append(k.text)
        
    
        
        
    total=[products,prices,ratings]
        
    next_button = browser.find_element_by_xpath("//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
    next_button.click()
    sleep(2)


print(total)

header=['productname','price']
data=[products,prices]
with open(r"C:\Users\hnrne\Downloads\amap.csv", 'w', newline='',encoding='UTF8') as output_file:
    dict_writer = csv.writer(output_file)
    dict_writer.writerow(header)
    dict_writer.writerow(data)


