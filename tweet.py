import tweepy
from keys import (
    consumer_key, consumer_secret, access_token, access_token_secret,
)

from clock import get_time


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def tweet():
    time = get_time()
    if time is not None:
        api.update_status(time)


if __name__ == '__main__':
    tweet()
