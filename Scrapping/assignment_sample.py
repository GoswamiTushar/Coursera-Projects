import urllib.request, urllib.parse
import ssl
import re
import bs4


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

tags = soup('span')
s = ''
cn = 0
l = []


for tag in tags:
    cn += 1
    s += str(tag)

l = list(map(int, re.findall(r'([0-9]+)', s)))

print(cn, sum(l))