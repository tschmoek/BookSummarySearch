from bs4 import BeautifulSoup
import requests

bookname = []
bookurl =[]
file = open('C:\\Source\\BookSummarySearch\\Kirkus.txt', 'a', encoding='utf-8')
i = 2584
bookset = set()
baseurl = 'https://www.kirkusreviews.com'
while(i < 2700):
    try:
        url = 'https://www.kirkusreviews.com/book-reviews/non_fiction/?page={}&sort=published&availability=available&stars=na'.format(i)

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.content, 'lxml')
        
        book_urls = soup.find_all('a',attrs={'itemprop':'url'})
        deleteDups = set()
        for book in book_urls:
            if book.span.text not in deleteDups and book.span.text not in bookset:
                deleteDups.add(book.span.text)
                bookset.add(book.span.text)
                urlBook = '{0}{1}, {2}\n'.format(baseurl,book.get('href'),book.span.text.lower())
                file.writelines(urlBook)
        print("Page " + str(i) + " completed!")
        i += 1
    except Exception as e:
        print('Loop should be done at this point.. Page count is {}'.format(i))
        print('\nJust to be sure, heres the exception ',e)
        break
    else:
        pass
    finally:
        pass

file.close()

