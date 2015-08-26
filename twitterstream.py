import oauth2 as oauth
import urllib2 as urllib

# See assignment1.html instructions or README for how to get these credentials

api_key = "5n0HialKjzhg8st7ecnOqC9wK"
api_secret = "S9rb2UQ4SOrrkSyEYCT06EEZoDhl92ckTtRhWkE1kgioWtjv6n"
access_token_key = "2476222483-xqnJ7XVkDpD5dYi0hu3X2bKuFdbex9v7fgO9XwV"
access_token_secret = "fom7AAO95IDThW3yPGrnGvPWGAUAsJXB4Bo6AZwTgOGot"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/filter.json?locations=-130.0,25.0, -65.0,50.0"
  parameters = []
  response = twitterreq(url, "POST", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()