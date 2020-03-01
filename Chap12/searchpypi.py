#! python3
# searchpypi.py - Opens several search results
import logging
# logging.disable(logging.CRITICAL)  # comment to enable debug logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')

import requests, sys, webbrowser, bs4
print('Searching...')  # display text while downloading the search result page
logging.debug('sys.argv variable is (%s)' %sys.argv)
searchStr = 'https://google.com/search?q=' 'https://pypi.org/search/?q='+' '.join(sys.argv[1:])
logging.debug('searchStr variable is (%s)' %searchStr)
res = requests.get(searchStr)
logging.debug('res variable is (%s)' %res)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
logging.debug('linkElems variable is (%s)' %linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
