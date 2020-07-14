from selenium import webdriver

from upgraded_pom.traning_ground_page import TraningGroundPage

browser = webdriver.Chrome()
test_value = "it worked"

# Test
trng_page = TraningGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == "Button1"
trng_page.button1.click()
