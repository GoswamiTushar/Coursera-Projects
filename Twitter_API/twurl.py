import urllib.request, urllib.parse, urllib.error
import auuth as oauth
import hidden

# https://apps.twitter.com/

def augment(url, parameters):
	secrets = hidden.oauth()
	consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
	token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
	oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token = token, http_method = 'GET', http_url = url, parameters = parameters)
	oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)

	return oauth_request.to_url()

if __name__ == "__main__":
	print(augment('https://twitter.com/json?', {"name":"Tushar"}))
	