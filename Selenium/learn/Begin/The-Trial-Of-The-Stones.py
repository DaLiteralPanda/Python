from selenium import webdriver
browser = webdriver.Chrome()

input_riddle_1 = "//input[@id='r1Input']"
button_riddle_1 = "//button[@id='r1Btn']"

input_riddle_2 = "//input[@id='r2Input']"
button_riddle_2 = "//button[@id='r2Butn']"

rich_merchant = "//div/p[text()='3000']/../span/b"

browser.get("https://techstepacademy.com/trial-of-the-stones")

# Entering the answer to first riddle
input1_elem = browser.find_element_by_xpath(input_riddle_1)
butn1_elem = browser.find_element_by_xpath(button_riddle_1)
input1_elem.send_keys("rock")
butn1_elem.click()
secret_text = browser.find_element_by_css_selector("div#passwordBanner > h4")

# Entering the answer to second riddle
input2_elem = browser.find_element_by_xpath(input_riddle_2)
butn2_elem = browser.find_element_by_xpath(button_riddle_2)
input2_elem.send_keys(secret_text.text)
butn2_elem.click()

# Entering the rich Merchant
input_rich_elem = browser.find_element_by_css_selector("input#r3Input")
text_rich = browser.find_element_by_xpath(rich_merchant)
rich_button = browser.find_element_by_css_selector("button#r3Butn")
input_rich_elem.send_keys(text_rich.text)
rich_button.click()

# Check Answer
answer_butn = browser.find_element_by_css_selector("button#checkButn")
answer_butn.click()
