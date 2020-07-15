class TraningGroundPage:
    def __init__(self, driver): # Initisialzing
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground/"

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inpt = self.driver.find_element_by_id('ipt1')
        inpt.clear()
        inpt.send_keys(text)
        return None

    def get_input_text(self):
        inpt = self.driver.find_element_by_id('ipt1')
        elem_text = inpt.get_attribute('value')
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element_by_id('b1')
        button.click()
        return None


# Test Setup
from selenium import webdriver

browser = webdriver.Chrome()
test_val = "It worked"

# Test
trng_page = TraningGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input('It worked')
trng_page.click_button_1()
txt_from_input = trng_page.get_input_text()
assert txt_from_input == test_val, f"Test Failed: Input did not match expected ({test_val})."
print("Test Passed.")
