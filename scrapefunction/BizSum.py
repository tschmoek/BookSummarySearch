import lxml
from bs4 import BeautifulSoup
import requests
# from Search import models
from django.core import management
from django.db import connection
import re


def SummaryService():
    # http://www.bizsum.com/summaries/all?page=359&amp%3Bsort_by=&audio=false&p=&sort_by=date&sort_order=desc
    file = open('C:\\Source\\BookSummarySearch\\BizSum.txt', 'w', encoding='utf-8')
    print('\n Biz Summeries \n')
    baseurl ='http://www.bizsum.com'

    bookset = set()
    cnt = 1
    for val in range(359,360):
        biz_markup = requests.get(baseurl + '/summaries/all?page={}&amp%3Bsort_by=&audio=false&p=&sort_by=date&sort_order=desc'.format(val))

        biz_soup = BeautifulSoup(biz_markup.content, "lxml")
        # print(biz_soup)

        for link in biz_soup.find_all('span',class_="catalog-title"):
            name = link.a.text.lower() 
            if name not in bookset:
                print('{} {}'.format(name,cnt))
                cnt += 1
                bookset.add(name)
                fullurl = baseurl + link.a.get('href')
                file.writelines(fullurl + ',')
                file.writelines(name + "\n")
