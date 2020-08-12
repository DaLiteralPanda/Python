# Run this with hydrogen (an atom package) only i havent tested it with terminal

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get('https://repl.it/')

start_cofing_btn = browser.find_element_by_xpath('//span[text()="Start coding"]')
start_cofing_btn.click()

python_btn = browser.find_element_by_xpath("//ul[@id='languageSelector-menu']/li/div/div[@class='jsx-927367763 content']/div[text()='Python']")
python_btn.click()

create_repl_btn = browser.find_element_by_xpath("//span[text()='Create repl']")
create_repl_btn.click()

# Set sleep up to your pc timing
sleep(8)

# Code Lines Element
code_line = '//div[@class="jsx-2481271225 monaco-editor-plugin"]'
code_line_elem = browser.find_element_by_xpath(code_line)
code_line_elem.click()

# Write the code
code = input("Type in some python code :- ")

from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(browser)
actions.send_keys(code)
actions.perform()

# Clicking the run button
run_elem = browser.find_element_by_xpath('//div[@class="jsx-428003656 ws-header-cta"]')
run_elem.click()
