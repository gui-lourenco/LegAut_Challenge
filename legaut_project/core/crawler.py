import requests as req
import urllib
from bs4 import BeautifulSoup
import re

def get_google_first_page(name):
    result = []
    text = urllib.parse.quote_plus(f'"{name}"')
    url = 'https://google.com/search?q=' + text
    response = req.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    for r in soup.find_all('div', attrs = {'class': 'ZINbbc'}):
        try:
            link = r.find('a', href = True)
            title = r.find('div', attrs={'class':'vvjwJb'}).get_text()

            if link != '' and title != '': 
                clean = re.search('\/url\?q\=(.*)\&sa',link['href'])
                if clean is None:
                    continue

                result.append((title, clean.group(1)))

        except:
            continue
    
    return result