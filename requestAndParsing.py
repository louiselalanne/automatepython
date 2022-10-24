# What you'll need
#
#pip3 install request
#pip3 install lxml
#pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')

print(soup)