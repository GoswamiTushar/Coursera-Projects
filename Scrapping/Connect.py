import oauth2 as oauth
import urllib.request, urllib.error, urllib.parse
import ssl
import json

# ignore certificate errors
ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
API_KEY = ''
API_SECRET = ''

consumer = oauth.Consumer(key = CONSUMER_KEY, 	secret = CONSUMER_SECRET )
access_token= oauth.Token(key = API_KEY, secret = API_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=geekyranjit&count=2"
response, data = client.request(r"https://api.twitter.com/1.1/trends/place.json?id=1")
# print(response)

tweets = json.loads(data)
# print(tweets)
tweets = json.dumps(tweets, sort_keys = True, indent=4)

print(tweets)
# for tweet in tweets:
# 	# print(tweet)
# 	print(tweet['text'])
