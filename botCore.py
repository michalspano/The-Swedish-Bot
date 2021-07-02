#  Libs to be used
import logging
import tweepy
import time
import gspread
import discord
from config import export_API

logger = logging.getLogger("Exception logger")
client = discord.Client()


class TwitterDataModel:
    def __init__(self, api, keyword, lang, tweet_range):
        self.api = api
        self.keyword, self.lang = keyword, lang
        self.tweet_range = tweet_range

    def export_twitter_data(self):
        tweets = [tweet for tweet in tweepy.Cursor(self.api.search,
                                                   q=f"{self.keyword}-filter:retweets",
                                                   rpp=20,
                                                   result_type="recent",
                                                   tweet_mode="extended",
                                                   lang=self.lang).items(self.tweet_range)]
        for tweet in tweets:
            tweet_status = self.api.get_status(tweet.id)
            retweeted, liked = tweet_status.retweeted, tweet_status.favorited
            if hasattr(tweet, "possibly_sensitive"):
                if not retweeted and not liked and not tweet_status.possibly_sensitive:
                    GoogleSpreadSheet(tweet).format_tweet()
                    tweet.favorite(), tweet.retweet()
                    print(f"Retweeted at {tweet.id}")
                    break


class GoogleSpreadSheet:
    def __init__(self, tweet):
        self.tweet = tweet
        self.gs = gspread.service_account(filename="credentials.json")
        self.sh = self.gs.open("@TheSwedishBot-spreadsheet").sheet1

    def format_tweet(self):
        display_user_name = self.tweet.user.screen_name
        url_f = f"https://twitter.com/{display_user_name}/status/{self.tweet.id}"
        favorite_count, retweet_count = self.tweet.favorite_count, self.tweet.retweet_count
        sh_data = [url_f, str(self.tweet.created_at), self.tweet.full_text,
                   display_user_name, favorite_count,
                   retweet_count, self.tweet.lang]
        self.sh.append_row(sh_data)
        return


def main(key_tags, lang, time_interval):
    api = export_API()
    while True:
        logger.info("**Parsing tweets**")
        TwitterDataModel(api, key_tags, lang, 15).export_twitter_data()
        time.sleep(time_interval)


if __name__ == "__main__":
    main("#Sweden OR #Sverige", "en OR sv", 15)
