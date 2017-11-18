import csv
import os
#os.environ['http_proxy'] = ""  
#os.environ['https_proxy'] = ""
import tweepy
import textblob
import sys

if(len(sys.argv)) >=2:
	topic = sys.argv[1]
else:
	print ('You haven\'t specified a topic.\n Default is India.')
	topic = 'India'

consumer_key = '***********'
consumer_secret = '***********'
access_token = '***********'
access_secret = '***********'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
public_tweets = api.search(topic,count = 100)
# print (type(public_tweets))


sentimentDict = {
    'Positive' : [],
    'Negative' : [],
    'pos_count' : 0,
    'neg_count' : 0
}


for tweet in public_tweets:
#     print(tweet.text)
    analysis = textblob.TextBlob(tweet.text)
    if(analysis.sentiment.polarity > 0.0):
        sentimentDict['Positive'].append(tweet.text)
        sentimentDict['pos_count'] +=1
    elif (analysis.sentiment.polarity < 0.0):
        sentimentDict['Negative'].append(tweet.text)
        sentimentDict['neg_count'] +=1
# print (sentimentDict['pos_count'])

filename = topic + '.csv'

with open(filename,'w') as tw:
#     twwriter = csv.writer(tw)
    tw.write('Number of Positive tweets are = %s\n' % str(sentimentDict['pos_count']))
    tw.write('Number of Negative tweets are = %s\n' % str(sentimentDict['neg_count']))
    tw.write('\nHere\'s a list of positive tweets:- \n\n ')
    for j in sentimentDict['Positive']:
            try:
                tw.write('\t%s\n\n'%j)
            except:
                pass
    tw.write('\n\n\n\nHere\'s a list of negative tweets:- \n\n ')
    for j in sentimentDict['Negative']:
            try:
                tw.write('\t%s\n\n'%j)
            except:
                pass

print ('The analysis file has been created under alias %s.csv' % topic)