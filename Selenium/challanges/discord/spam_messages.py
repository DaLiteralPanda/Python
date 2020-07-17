from selenium import webdriver
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://discord.com/login")
sleep(2)

# Signing in
login = browser.find_element_by_css_selector("input[name='email']")
login.send_keys(input("Type in an email:- "))
password = browser.find_element_by_css_selector("input[name='password']")
password.send_keys(getpass(prompt="Type in your password:- "))
login_button = browser.find_element_by_css_selector("button[type='submit']")
login_button.click()

# Going in the dm
dm = "a#private-channels-3"
dm_elem = browser.find_element_by_css_selector(dm)
dm_elem.click()

# Manually go to the dm
message_box = '//div[@class="textArea-12jD-V textAreaSlate-1ZzRVj slateContainer-3Qkn2x"]/div/div'
message_box_elem = browser.find_element_by_xpath(message_box)

for i in range(0,100):
    message_box = '//div[@class="textArea-12jD-V textAreaSlate-1ZzRVj slateContainer-3Qkn2x"]/div/div'
    message_box_elem = browser.find_element_by_xpath(message_box)
    message_box_elem.send_keys("happy birthday boiiii :joy:")
    sleep(1)
    message_box = '//div[@class="textArea-12jD-V textAreaSlate-1ZzRVj slateContainer-3Qkn2x"]/div/div'
    message_box_elem = browser.find_element_by_xpath(message_box)
    message_box_elem.send_keys(Keys.ENTER)
    sleep(2)
