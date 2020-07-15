from selenium import webdriver
# initializing the Browser
browser = webdriver.Chrome()
# Telling it to go to this URL
browser.get("https://www.techstepacademy.com/training-ground")
# Specifing the Text Box to type in
input_element = browser.find_element_by_css_selector('input[id="ipt1"]')
input_element.send_keys("My First Automation")
# Specifing the Button to click
button_element = browser.find_element_by_css_selector('button[name="butn1"]')
button_element.click()
