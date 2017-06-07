import lxml
from bs4 import BeautifulSoup
import requests
from Search import models
from django.core import management
from django.db import connection 

class FourMin(object):
    """docstring for FourMin"""

    def SummaryService():
        print('\n Four minute Summeries \n')
        fourmin_markup = requests.get('http://fourminutebooks.com/all-summaries/')

        fourmin_soup = BeautifulSoup(fourmin_markup.content, "lxml")

        fourmin_summary_links = fourmin_soup.find_all(
            "a", class_="post_title w4pl_post_title")

        for summary_title in fourmin_summary_links:
            # As of right now they include the word summary at the end of each string..
            if summary_title:
                try:
                    fourminmodel = models.FourMinMod()
                    fourminmodel.name = summary_title.text[:-8].strip().lower()
                    fourminmodel.url = summary_title.get('href').strip()
                    fourminmodel.save()
                except Exception as e:
                    print("something went wrong ", e)
