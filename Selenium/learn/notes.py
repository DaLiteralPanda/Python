# Importing selenium
from selenium import webdriver
from time import sleep

# After installation of the chromedriver enter the path were you kept it
PATH = "C:/Users/rishit/miniconda3/Scripts/chromedriver.exe"
# Opening a chrome window
driver = webdriver.Chrome(PATH)

# Going to a website
driver.get("https://techstepacademy.com/training-ground")


# Making a delay
sleep(5)

# Selecting elements
### How do you select elements?
### You can select them by name by what it contains, etc

### rn we'll do it by name
label1 = driver.find_element_by_name('i1_label')
### Print the label text
print(label1.text)

# Entering text in a input field
### By name
input_by_name1 = driver.find_element_by_name('Input 1')
### By CSS Selector
input1_elem = driver.find_element_by_css_selector('input[id="ipt1"]')

## Typing something in the input
input1_elem.send_keys("Woah!")

# Clicking on elements
button1_elem = driver.find_element_by_xpath('//button[@id="b1"]')

# Clicking it
button1_elem.click()

sleep(3)
# Accepting an alert
from selenium.webdriver.common.alert import Alert

Alert(driver).accept()

sleep(1)

# Exiting the window
driver.quit()
