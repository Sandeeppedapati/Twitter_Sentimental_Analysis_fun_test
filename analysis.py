# We need to install the dependencies first  they are text blob(a natural language processing library forn python absolutely useful for the beginners)
#and tweepy(used to access the api of the twitter)

import tweepy 
from textblob import TextBlob
consumer_key = " Consumer Token created during our twitter app"
consumer_secret = "Consumer secret Key created during our twitter app"
access_key = " Consumer Token created during our twitter app"
access_secret = " Acess secretkey  created during our twitter app"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)

api = tweepy.API(auth)

public_tweets = api.search('SandeepPedapati')

file = open("sentimental_analysis.csv","w")

for tweets in public_tweets :
    print(tweets.text)
    file.write(tweets.text)
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment)
    file.write(", ")
    if(analysis.sentiment.polarity > 0) :
        file.write("positive \n")
    elif(analysis.sentiment.polarity == 0) :
        file.write("neutral \n")
    else :
        file.write("negative \n")
        
file = open("sentimental_analysis.csv","r")
print(file.read())
