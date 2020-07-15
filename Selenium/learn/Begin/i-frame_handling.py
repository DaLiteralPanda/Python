from selenium import webdriver

browser = webdriver.Chrome()
# Page with i-frame
browser.get("http://techstepacademy.com/iframe-training")
# This wont work
welcome_text = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")
# You need to switch to the i-frame
i_frame = browser.find_element_by_css_selector("iframe")
i_frame
browser.switch_to.frame(i_frame)
# Now we try again with that element
welcome_text = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")
welcome_text
# How to Switch back to the original page
title_text = browser.find_element_by_css_selector("div#block-5d3de848045889000188d389") # Does not work
# Switch to default content
browser.switch_to.default_content()
# Try that code again
title_text = browser.find_element_by_css_selector("div#block-5d3de848045889000188d389 div p")
title_text.text
