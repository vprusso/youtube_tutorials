import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Must store credential json in parent GitHub directory (as to not upload the key to public repo)
with open('..\\twitter_credentials.json') as f:
    creds = json.load(f)
    CONSUMER_KEY = creds['consumer_api_key']
    CONSUMER_SECRET = creds['consumer_api_secret_key']
    ACCESS_TOKEN = creds['access_token']
    ACCESS_TOKEN_SECRET = creds['access_token_secret']


class StdOutListener(StreamListener):
    def on_data(self, data):
        # takes data in from stream listener - the tweets
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    stream.filter(track=['impeachment'])
