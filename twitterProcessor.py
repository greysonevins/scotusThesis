import json
import pandas as pd
from hatesonar import Sonar
from textblob import TextBlob

twitterDataFile = "twitter_data.txt"
twitterFile = open(twitterDataFile, "r")
twitterData = []
for line in twitterFile:
    try:
        tweet = json.loads(line)
        twitterData.append(tweet)
    except Exception as e:
        continue

tweets = pd.DataFrame()
sonar = Sonar()
def getSonar(text):
    value = sonar.ping(text=text)
    topClass = value["top_class"]
    hateSpeechConfidence = value["classes"][0]["confidence"]
    offensiveConfidence = value["classes"][1]["confidence"]
    neitherConfidence = value["classes"][2]["confidence"]
    return topClass, hateSpeechConfidence, offensiveConfidence, neitherConfidence


tweets["text"] = list(map(lambda tweet: tweet["extended_tweet"]["full_text"]
                if "extended_tweet" in tweet else tweet['text'], twitterData))



topClassList = []
hateSpeechConfidenceList = []
offensiveConfidenceList = []
neitherConfidenceList = []
sentimentList = []
subjectivitySentimentList = []
for text in tweets["text"]:
    topClass, hateSpeechConfidence, offensiveConfidence, neitherConfidence = getSonar(text)
    topClassList.append(topClass)
    hateSpeechConfidenceList.append(hateSpeechConfidence)
    offensiveConfidenceList.append(offensiveConfidence)
    neitherConfidenceList.append(neitherConfidence)
    blob = TextBlob(text)
    sentimentList.append(blob.sentiment.polarity)
    subjectivitySentimentList.append(blob.sentiment.subjectivity)


tweets["sentiment polarity"] = sentimentList
tweets["sentiment subjectivity"] = subjectivitySentimentList
tweets["topClass"] = topClassList
tweets["hateSpeechConfidence"] = hateSpeechConfidenceList
tweets["offensiveConfidence"] = offensiveConfidenceList
tweets["neitherConfidence"] = neitherConfidenceList


hateSpeech = tweets[tweets["topClass"] == "hate_speech"]
offensiveSpeech = tweets[tweets["topClass"] == "offensive_language"]

hateSpeech.to_csv("hateTweets.csv")
offensiveSpeech.to_csv("offensiveTweets.csv")



#
#
# # tweets["hashtags"] = map(lambda tweet: tweet["extended_tweet"]["full_text"]
# #                 if "extended_tweet" in tweet else tweet['text'], twitterData)
# print(pd.value_counts(tweets['topClass'].values, sort=False))
# print(tweets['sentiment polarity'].mean())
# print(tweets['sentiment subjectivity'].mean())
# print(tweets['hateSpeechConfidence'].mean())
# print(tweets['offensiveConfidence'].mean())
# print(tweets['neitherConfidence'].mean())


print(len(twitterData))
