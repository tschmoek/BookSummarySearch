import re
import lxml
from bs4 import BeautifulSoup
import requests
from Search import models

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Consider using selenium to login to this service to get the library page scraped..
class ReadItForMe(object):
    """docstring for ReadItForMe"""
    def __init__(self, arg):
        super(ReadItForMe, self).__init__()
        self.arg = arg
        
    def SummaryService():
        driver = webdriver.Firefox(executable_path=r'C:\Users\Tanner\Desktop\geckodriver-v0.16.1-win64\geckodriver.exe')
        print('\n Read it for me Summeries \n')

        driver.get("https://pro.readitfor.me/library")


        username = driver.find_element_by_name("email")
        password = driver.find_element_by_name("password")
        username.send_keys("")
        password.send_keys("")
        password.send_keys(Keys.RETURN)

        category = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "ctg_filter")))
        readitforme_markup = driver.page_source

        readitforme_soup = BeautifulSoup(readitforme_markup, "lxml")

        readitforme_summary_links = readitforme_soup.find_all('a',attrs={"data-target": "#upgrade"})


        uniqueList = set([link.text.strip() for link in readitforme_summary_links if link])

        for booktitle in uniqueList:
            if booktitle:
                readitforme = models.ReadItForMeMod()
                readitforme.name = booktitle.lower()
                readitforme.url = "https://readitfor.me/"
                readitforme.save()
        driver.close()
                
