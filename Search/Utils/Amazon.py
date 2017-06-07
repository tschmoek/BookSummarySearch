import re
import lxml
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from random import randint, random


def Amazon(booklist,fh):

    file = open(fh, "w", encoding='utf-8')

    for book in booklist:
        
        updatedProxy = updateProxy()
        amazon_markup = requests.get('https://www.amazon.com/s/keywords={}'.format(book),headers=updatedProxy['newHeader'], proxies=updatedProxy['newHeader'])

        amazon_soup = BeautifulSoup(amazon_markup.content, "lxml")
        fh = open("Search\\Utils\\amz.html", "w", encoding='utf-8')
        

        detailslink = getDetailsPage(amazon_soup)
        file.writelines(detailslink)

        # updatedProxy = updateProxy()
        # detailspage = requests.get(detailslink,headers=updatedProxy['newHeader'], proxies=updatedProxy['newHeader'])

        # amazon_soup = BeautifulSoup(detailspage.content, "lxml")

        # for val in amazon_soup.find_all(attrs={"data-hook": 'review-collapsed'}):
        


def getDetailsPage(soup):
    for link in soup.find_all(id='result_0'):
        return str(link.find('a','s-access-detail-page').get('href'))


def updateProxy():
    headers = requests.utils.default_headers()
    ua = UserAgent()

    proxy = requests.get('https://api.proxicity.io/v2/48a0b3a4a933e08f1929f5273f3d7deceafdff6b3d69f62e299094a5bf7f97b7/proxy?isAnonymous=true&httpsSupport=true&country=US').json()
    if proxy:
        while not proxy['supportedWebsites']['amazon.com']:
            print('Getting new proxy.. Amazon is False\n')
            proxy = requests.get('https://api.proxicity.io/v2/48a0b3a4a933e08f1929f5273f3d7deceafdff6b3d69f62e299094a5bf7f97b7/proxy?isAnonymous=true&httpsSupport=true&country=US').json()

    headers.update(
        {
            'User-Agent': ua.random,
        }
    )
    return {'newHeader': headers,
            'newProxy':proxy}

