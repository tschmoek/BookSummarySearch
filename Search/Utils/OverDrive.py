import lxml
from bs4 import BeautifulSoup
import requests
SUMMARYfh = "Search\\Utils\\Results\\Summary.txt"
class OverDrive(object):
    """docstring for OverDrive"""
    def __init__(self, arg):
        super(OverDrive, self).__init__()
        self.arg = arg
        
    def SummaryService(book):
        sumFile = open(SUMMARYfh, "w", encoding='utf-8')
        result = ''
        overdrive_markup = requests.get('https://www.overdrive.com/search?q={}'.format(book))
        li = []

        overdrive_soup = BeautifulSoup(overdrive_markup.content, "lxml")
        for link in overdrive_soup.find_all(class_='title-result-row__title'):
            for title in link('a'):
                if title.get('data-title').lower() == book.lower():
                    li.append(title.get('href'))
        if li:
            # Just grab the first one off the list..
            overdrive_markup = requests.get('https://www.overdrive.com' + li[0])
            overdrive_soup = BeautifulSoup(overdrive_markup.content, "lxml")

            for url in li[:1]:
                result = 'https://www.overdrive.com' + url
            sumFile.writelines('''<div class="row">
                                    <div class="col-md-2"></div>
                                    <div class="col-md-8">
                                    <h4>''')
            sumFile.writelines(overdrive_soup.find(class_='title-page__blurb').text)
            sumFile.writelines('''</h4><br><br> <h4 class="text-center">-From Overdrive</h4>
                                    </div>
                                    </div>''')
        return result