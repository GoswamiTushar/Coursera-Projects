import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as et
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_685286.xml"
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'lxml')

tree = et.fromstring(str(soup))
#tree = et.fromstring(html) alternatively, it needs string

results = tree.findall('.//count')

total = sum(list(map(lambda x: int(x.text), results)))
print(total)
