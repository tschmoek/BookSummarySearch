import lxml
from bs4 import BeautifulSoup
import requests


class ActionBook(object):
    """docstring for ActionBook"""
    def __init__(self, arg):
        super(ActionBook, self).__init__()
        self.arg = arg

    def SummaryService(book):
        print('\n Actionable Book Summeries \n')
        result = None
        actionbooksite = requests.get('http://www.actionablebooks.com/en-ca/search-results/?search={}&limit=summaries'.format(book))

        actionbook_soup = BeautifulSoup(actionbooksite.content, "lxml")

        actionbook_summary_links = actionbook_soup.find_all("span", class_="booktitle")
        if actionbook_summary_links:
            for link in actionbook_summary_links:
                if link.text.lower() == book.lower():
                    result = link.a.get('href')
        return result
        