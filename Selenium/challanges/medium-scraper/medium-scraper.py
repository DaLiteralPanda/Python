from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get("https://medium.com/search")

# Getting search bar's html stuff
search_bar = "input[type='search']"
search_bar_elem = browser.find_element_by_css_selector(search_bar)
search_bar_elem.send_keys(input("What do you want to search:- "))
sleep(5)
# Clicking the first search result and scraping its data
first_result = "//div[@class='u-paddingTop20 u-paddingBottom25 u-borderBottomLight js-block']"
first_result_elem = browser.find_element_by_xpath(first_result)
first_result_elem.click()
sleep(10)
# Getting the title
title = browser.find_element_by_xpath("//h1")
print(title.text)
para = browser.find_element_by_xpath("//div[@class='n p']/div/p")
print(para.text)
