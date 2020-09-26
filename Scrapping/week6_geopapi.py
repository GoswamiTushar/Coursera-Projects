import urllib.request, urllib.parse
import ssl
import json

api_key = False

if api_key is False:
	api_key = 42
	service_url = "http://py4e-data.dr-chuck.net/json?".strip()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input("Enter the address \n>> ");

url = service_url + urllib.parse.urlencode({'key': api_key,'sensor': 'false', 'address' : address})

print("Retriving", url, sep = '\n')

data = urllib.request.urlopen(url, context = ctx).read().decode()

print("Retrived ", len(data), " Characters")

# print(data)

try:
	js = json.loads(str(data))
except:
	js = None

# print(js)

if 'status' not in js or js['status'] != 'OK':  
	print('==== Failure To Retrieve ====')
	print(data)

placeid = js["results"][0]["place_id"]  
print('Place ID ', placeid) 