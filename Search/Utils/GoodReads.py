import lxml
from bs4 import BeautifulSoup
import requests

class GoodReads(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

    def SummaryService(book):
        print('\n Good Reads Summeries\n')
        
        goodreads_markup = requests.get('https://www.goodreads.com/search?q={}'.format(book))

        goodreads_soup = BeautifulSoup(goodreads_markup.content, "lxml")

        goodreads_links = goodreads_soup.find_all('a',class_='bookTitle')

        goodreads_links = goodreads_links[:1] #Shortening the list to just the first result
        for link in goodreads_links:
            return 'https://www.goodreads.com' + link.get('href')
        