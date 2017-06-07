import lxml
from bs4 import BeautifulSoup
import requests
from Search import models
from django.core import management
from django.db import connection
import re
BLINKLIST = "Search\\Utils\\Results\\Blink.html"

class Blink(object):
    """docstring for FourMin"""

    def SummaryService():
        print('\n Blink Summeries \n')
        blink_markup = requests.get('https://www.blinkist.com/en/categories/entrepreneurship-and-small-business-en.html')

        blink_soup = BeautifulSoup(blink_markup.content, "lxml")

        bookset = set()
        categories = [category.get('href') for category in blink_soup.find_all("a", class_="category-list-item__link")]
        for category in categories:
            blink_markup = requests.get('https://www.blinkist.com' + category[:-8] + "-en/books")
            
            blink_soup = BeautifulSoup(blink_markup.content, "lxml")

            for link in blink_soup.find_all("a", class_="letter-book-list__item"):
                try:
                    title = link.find("span", class_="letter-book-list__item__title").text.strip()
                    if title not in bookset:
                        bookset.add(title)
                        blinkmod = models.BlinkMod()
                        blinkmod.name = title.lower()
                        blinkmod.url = link.get("href").strip()
                        blinkmod.save()
                except Exception as e:
                    print("something went wrong ", e)
                    pass

