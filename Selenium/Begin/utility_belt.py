from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions	import alert_is_present
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://www.techstepacademy.com/training-ground")

# Click an Alert
alert = Alert(browser)
# Gets Text from the alert
alert.text
# Accept or Dismiss an Alert
alert.accept()
alert.dismiss()

# Wait, until something has happened
WebDriverWait(browser, 10).until(alert_is_present()) # This is an explicit wait
print("An Alert Appeared")

# Selection Box
sel = browser.find_element_by_id('sel1')
my_select = Select(sel)
# Options
my_select.options
# Select by visible Text
my_select.select_by_visible_text('Beets')
