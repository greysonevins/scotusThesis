import os
import tweepy
import threading
import json
import csv


consumer_key = os.environ["NA_CONSUMER_KEY"]
consumer_secret = os.environ["NA_CONSUMER_SECRET"]
access_token = os.environ["NA_ACCESS_TOKEN"]
access_token_secret = os.environ["NA_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
TRACKED_WORDS=[
        "#scotus",
        "#notoriousrbg",
        "#RBG",
        "Anthony Kennedy",
        "Clarence Thomas",
        "Ruth Bader Ginsburg",
        "Stephen Breyer",
        "Samuel Alito",
        "Sonia Sotomayor",
        "Elena Kagan",
        "Neil Gorsuch",
        "John Roberts",
        "Justice Kennedy",
        "Justice Thomas",
        "Justice Ginsburg",
        "Justice Breyer",
        "Justice Alito",
        "Justice Sotomayor",
        "Justice Kagan",
        "Justice Gorsuch",
        "Justice Roberts",
        "Justice Scalia",
        "SCOTUS",
        "#Kennedy",
        "#Thomas",
        "#Ginsburg",
        "#Breyer",
        "#Alito",
        "#Sotomayor",
        "#Kagan",
        "#Gorsuch",
        "#Roberts",
        "#AnthonyKennedy",
        "#ClarenceThomas",
        "#RuthBaderGinsburg",
        "#StephenBreyer",
        "#SamuelAlito",
        "#SoniaSotomayor",
        "#ElenaKagan",
        "#NeilGorsuch",
        "#JohnRoberts",
        "Trump v. Hawaii",
        "travel ban",
        "#MuslimBan"
        ]

class MyStreamListener(tweepy.StreamListener):
        #create file checker

        def __init__(self, async, *args):
            print(aync)

        #
            # if os.path.isfile(fname):
        #         fileE = True
        #     else:
        #         print("none")
        #add data to file on call
        # def on_status(self, status):
        #     fname = "tweetsStreamed.csv"
        #     headers = ["Text", "User_ID", "Verified", "Urls", "Mentions",
        #                 "Hashtags", "Timestamp_ms", "Created_at", "ID", "Source",
        #                 "Soucre_url", "Geo", "Coordinates", "Retweeted_status",
        #                 "Possibly_sensitive", "Is_quote_status",
        #                 "In_reply_to_status_id"]
        #     try:
        #         text = status.extended_tweet["full_text"]
        #     except AttributeError:
        #         text = status.text
        #     user_id = status.user.id
        #     verified = status.user.verified
        #     try:
        #         urls = status.entities["urls"]
        #     except AttributeError:
        #         urls = None
        #     try:
        #         mentions = status.entities["user_mentions"]
        #     except AttributeError:
        #         mentions = None
        #     try:
        #         hashtags = status.entities["hashtags"]
        #     except AttributeError:
        #         hashtags = None
        #     timestamp_ms = status.timestamp_ms
        #     created_at = status.created_at
        #     id = status.id
        #     source = status.source
        #     soucre_url = status.source_url
        #     geo = status.geo
        #     coordinates = status.coordinates
        #     try:
        #         retweeted_status = status.retweeted_status
        #     except AttributeError:
        #         retweeted_status = None
        #     try:
        #         possibly_sensitive = status.possibly_sensitive
        #     except AttributeError:
        #         possibly_sensitive = None
        #
        #     is_quote_status = status.is_quote_status
        #     try:
        #         in_reply_to_status_id = status.in_reply_to_status_id
        #     except AttributeError:
        #         in_reply_to_status_id = None
        #
        #     if os.path.isfile(fname):
        #         with open("tweetsStreamed.csv", "a") as cd:
        #             addTweet = csv.writer(cd)
        #             addTweet.writerow([text, user_id, verified, urls, mentions,
        #                     hashtags, timestamp_ms, created_at, id, source, soucre_url,
        #                      geo, coordinates, retweeted_status, possibly_sensitive,
        #                      is_quote_status, in_reply_to_status_id])
        #         with open("tweetsStreamed.csv")  as cd:
        #             reader = csv.DictReader(cd, delimiter = ",")
        #             print("how many tweets: ", len(list(reader)))
        #     else:
        #         with open("tweetsStreamed.csv", "w") as newC:
        #             newF = csv.writer(newC)
        #             newF.writerow(headers)
        #             newF.writerow([text, user_id, verified, urls, mentions,
        #                 hashtags, timestamp_ms, created_at, id, source, soucre_url,
        #                  geo, coordinates, retweeted_status, possibly_sensitive,
        #                  is_quote_status, in_reply_to_status_id])

        def on_data(self, data):
            print(self.__dict__)
            fname = "test.txt"
            if os.path.isfile(fname):
                with open("test.txt", "a") as myfile:
                    myfile.write(data + "\n")
            else:
                with open("test.txt", "w") as myfile:
                    myfile.write(data + "\n")
            return True

        def on_disconnect(self, notice):
            print(notice)
            return

        def on_warning(self, notice):
            print(notice)
            return
        def on_error(self, status_code):
            print(status_code)
            if status_code == 420:
                return False
        def on_exception(self, exception):
            print(exception)
            return

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=TRACKED_WORDS, languages=['en'],stall_warnings=True, async=True)


# class JsonFile(jsonData):
#
#     def isFile():
#         if exists:
#             pass
#         else:
#             make
#         "twitterSteam.csv"
#
#     def addToFile():
#
#         "twitterSteam.json"
