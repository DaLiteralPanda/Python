from selenium import webdriver
from getpass import getpass
from time import sleep

browser = webdriver.Chrome()

browser.get("https://discord.com/login")
# Signing in
login = browser.find_element_by_css_selector("input[name='email']")
login.send_keys(input("Type in an email:- "))
password = browser.find_element_by_css_selector("input[name='password']")
password.send_keys(getpass(prompt="Type in your password:- "))
login_button = browser.find_element_by_css_selector("button[type='submit']")
login_button.click()

# Going in the server
server = "a[aria-label='Tech World']"
server_elem = browser.find_element_by_css_selector(server)
server_elem.click()

vc = "//div[@class='content-3at_AU']/div[text()='General vc']"
vc_elem = browser.find_element_by_xpath(vc)

vc_mute = "//button[@aria-label='Deafen']"
vc_mute_elem = browser.find_element_by_xpath(vc_mute)

vc_elem.click()
# vc_mute_elem.click()
for i in range(0,10):
    vc_mute_elem.click()

browser.quit()
