# YouTube Video: https://www.youtube.com/watch?v=wlnx-7cm4Gg
import json

from tweepy.streaming import StreamListener
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import Stream

# Must store credential json in parent GitHub directory (as to not upload the key to public repo)
with open('C:\\Users\\jmfor\\Documents\\GitHub\\twitter_credentials.json') as f:
    creds = json.load(f)
    CONSUMER_KEY = creds['consumer_api_key']
    CONSUMER_SECRET = creds['consumer_api_secret_key']
    ACCESS_TOKEN = creds['access_token']
    ACCESS_TOKEN_SECRET = creds['access_token_secret']

# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        # if no twitter user is specified, Tweepy defaults to the authenticated account
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
        
    def get_user_timeline_tweets(self, num_tweets):
        # get the tweets from a specified user
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        # get the friend list of a specified twitter user
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        # get tweets from the specified user's timeline
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


# # # # TWITTER AUTHENTICATOR # # # #
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
       auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
       auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
       return auth


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authentication and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        if status == 420:
            # Return False on data method in case rate limit occurs
            return False
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["philadelphia eagles", "dallas cowboys"]
    fetched_tweets_filename = "twitter_python\\part_2_cursor_and_pagination\\data\\tweets.json"

    # twitter_streamer = TwitterStreamer()
    # twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

    twitter_client = TwitterClient('Eagles')
    print(twitter_client.get_user_timeline_tweets(1))