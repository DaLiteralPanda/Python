from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.techstepacademy.com/training-ground")

# Opening a Tab
browser.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
# Displays Tabs
browser.window_handles
len(browser.window_handles)
handles = browser.window_handles # Making a variable for simplicity
# Switching to the other Tab(Window)
browser.switch_to.window(handles[1])
