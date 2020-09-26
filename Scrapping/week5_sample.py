import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as et

url = "http://py4e-data.dr-chuck.net/comments_42.xml"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

tree = et.fromstring(html)

results = tree.findall('.//count')

total = sum(list(map(lambda x: int(x.text), results)))
print(total)

# for dig in results:
# 	total += int(dig.text) ALTERNSTIVE






