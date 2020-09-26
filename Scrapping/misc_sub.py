import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import ssl
import re

url = 'http://py4e-data.dr-chuck.net/known_by_Sheigh.html'

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context = ctx)
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

count = int(input("Enter the count \n>> "))
position = int(input("Enter the position \n>> "))

tag = tags[position-1]
name = re.findall('^.+">([a-zA-Z]+).*', str(tag))
link = tag.get('href', None)
# print(tag, link, name, sep = '\n')

for i in range(count-1):
	url = link
	html = urllib.request.urlopen(url, context = ctx)
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	tag = tags[position-1]
	name = re.findall('^.+">([a-zA-Z]+).*', str(tag))
	link = tag.get('href',None)
	print("Retrieving :", link, "\nName: ", name[0])

print("Last Retrieved Name: ", name[0])


