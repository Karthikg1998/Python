import tweepy
import pandas as pd

#Get credentials
API_Key="hXA2skczxZImnohOJQlc7geWJ"
API_Key_Secret="5SeUY9Fvbet0NpGOBCmM7UAzODOyI26w586yEWiBAaMryIjd7e"
Bearer_Token ="AAAAAAAAAAAAAAAAAAAAAHIKkAEAAAAAs7u90SHylxZIW7ZASnn8rhTtnXw%3DPl1X1DU0KEEJhtoFJId4BShmqRqXuRu3Aor1BIbXpZZqBiEuvZ"

access_token="1598998362379849728-vF6DsVtnYNkTOWFEVY1DcNC29bDN7W"
access_token_secret ="Xu8wiEgYm155n7smGWyN9kehPNlZiE3ru8KybTcw9COSr"


# Twitter Authentication
auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
auth.set_access_token(access_token, access_token_secret)


# Creating  an API object

api = tweepy.API(auth,wait_on_rate_limit=True)
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')



# Gather the 2000 tweets about India and filter out any retweets 'RT'
search_term = '#india -filter:retweets'
# create a cursor object
tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en', tweet_mode='extended').items(1000)
        # tweepy.Cursor(api.search, q, tweet_mode='extended').items(tweetNumber)
# store the tweets in a variable and get the full text
all_tweets = [tweet.full_text for tweet in tweets]

# create a datframe to store the tweets with a columns call 'Tweets'
df = pd.DataFrame(all_tweets, columns=['Tweets'])
# show the first 5 rows of Data
print(df)
