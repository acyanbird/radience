from bs4 import BeautifulSoup as bs
import requests as rq
from selenium import webdriver
import time

URL = "https://papers.gceguide.xyz/A%20Levels/Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)"

browser = webdriver.Firefox()

browser.get(URL)  # to get the content

##print(browser.page_source)

test = browser.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[1]/a")

print(test)

browser.close()