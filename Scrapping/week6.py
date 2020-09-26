import urllib.request, urllib.parse
import ssl
import json

url = "http://py4e-data.dr-chuck.net/comments_685287.json ".strip()

# certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


data = urllib.request.urlopen(url).read()
data = json.loads(data)
count = 0

for items in data["comments"]:
	value = (items['count'])
	count += value

print(count)