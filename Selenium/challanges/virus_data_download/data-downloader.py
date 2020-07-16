from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

duplodnaviria = "https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&utm_source=nuccore&utm_medium=referral&utm_campaign=COVID-19&VirusLineage_ss=Duplodnaviria,%20taxid:2731341"

riboviria = "https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&utm_source=nuccore&utm_medium=referral&utm_campaign=COVID-19&VirusLineage_ss=Riboviria%20(RNA%20viruses),%20taxid:2559587"

monodnaviria = "https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&utm_source=nuccore&utm_medium=referral&utm_campaign=COVID-19&VirusLineage_ss=Monodnaviria%20(single-stranded%20DNA%20viruses),%20taxid:2731342"

varidnaviria = "https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Varidnaviria,%20taxid:2732004"

browser.get(duplodnaviria)
sleep(10)

# Encasing it in a for loop
for i in range(0,5):
    checkbox_even = "//tr[@class='even']/td/label"
    checkbox_even_elem = browser.find_element_by_xpath(checkbox_even)
    checkbox_even_elem.click()
    sleep(0.2)
    # Getting the download buttons element
    download_btn_elem = browser.find_element_by_xpath('//button[text()="Download"]')
    download_btn_elem.click()
    sleep(0.2)
    download_btn_next = browser.find_element_by_xpath('//button[text()="Next"]')
    download_btn_next.click()
    sleep(0.2)
    download_btn_next_2 = browser.find_element_by_xpath('//button[text()="Next"]')
    download_btn_next_2.click()
    sleep(0.2)
    download_btn_elem_2 = browser.find_element_by_xpath("//h4[text()='Step 3 of 3: Select FASTA definition line']/../button[2]")
    download_btn_elem_2.click()
    sleep(7)

    # Clicking the checkbox again to deselect it
    checkbox_even_elem.click()
    sleep(1)
    # Now getting checking the boxes by odd placement
    checkbox_odd = "//tr[@class='odd']/td/label"
    checkbox_odd_elem = browser.find_element_by_xpath(checkbox_odd)
    checkbox_odd_elem.click()
    sleep(0.2)
    # Getting the download buttons element
    download_btn_elem = browser.find_element_by_xpath('//button[text()="Download"]')
    download_btn_elem.click()
    sleep(0.2)
    download_btn_next = browser.find_element_by_xpath('//button[text()="Next"]')
    download_btn_next.click()
    sleep(0.2)
    download_btn_next_2 = browser.find_element_by_xpath('//button[text()="Next"]')
    download_btn_next_2.click()
    sleep(0.2)
    download_btn_elem_2 = browser.find_element_by_xpath("//h4[text()='Step 3 of 3: Select FASTA definition line']/../button[2]")
    download_btn_elem_2.click()
    sleep(7)

    # Clicking the checkbox again to deselect it
    checkbox_odd_elem.click()
    sleep(1)
    # Going to the nest page
    next_page_btn = '//button[@aria-label="Next Page"]'
    next_page_btn_elem = browser.find_element_by_xpath(next_page_btn)
    next_page_btn_elem.click()
    sleep(10)
