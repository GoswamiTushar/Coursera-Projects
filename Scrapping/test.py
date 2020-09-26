import urllib.request, urllib.error, urllib.parse
import ssl
from bs4 import BeautifulSoup

url = 'https://www.glauniversity.in:8085'
html = urllib.request.urlopen(url).read()
print(html)
#soup = BeautifulSoup(html, 'html.parser').read()

print(type(html))

# tags = soup('a')

# #print(soup)

# for tag in tags:
#     print(tag.get('href', None))

# #print(soup)
