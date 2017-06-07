

import lxml
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getAbstracts():
    file = open('C:\\Source\\RealEstateScripts\\Info', "w", encoding='utf-8')

    print('\n Scraping getAbstract \n')
    
    # homelightsite = requests.get()

    driver = webdriver.Firefox(executable_path=r'C:\Users\Tanner\Desktop\geckodriver-v0.16.1-win64\geckodriver.exe')
    # https://www.homelight.com/agents/bradley-haag-ca-01255517
    driver.get('https://www.getabstract.com/en/explore?offset=140&audioOnly=false&sorting=online_date&languageIds=1&sumSourceTypes=BOOK&sumSourceTypes=VIDEO&sumSourceTypes=ARTICLE')
    driver.implicitly_wait(4)
    driver.find_element_by_id('sumSourceType-ARTICLE').click()
    driver.find_element_by_id('sumSourceType-VIDEO').click()
    while(True):
    	WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "clearfix.col-sm-12.explore-next")))
    	driver.find_element_by_css_selector('clearfix.col-sm-12.explore-next').find_element_by_tag_name('button').click()


    driver.close()


getAbstracts()
# button

# sumSourceType-BOOK

# label