import lxml
from bs4 import BeautifulSoup
import requests


class ProxyService(object):
    """docstring for ActionBook"""
    def __init__(self, arg):
        super(ActionBook, self).__init__()
        self.arg = arg


    def getProxies():
        file = open("proxies.txt", "w", encoding='utf-8')

        print('\n Getting Proxies\n')
        
        proxiesSite = requests.get('https://hidemy.name/en/proxy-list/')
        print(proxiesSite.content)
        proxiesSoup = BeautifulSoup(proxiesSite.content, "lxml")

        proxies = proxiesSoup.find_all(class_="tdl")

        for link in proxies:
        	print(link)
        file.close()
