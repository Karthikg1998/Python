import pandas as pd
import tweepy


def twitter_run_etl():
            #Variable declaration
            API_Key="hXA2skczxZImnohOJQlc7geWJ"
            API_Key_Secret="5SeUY9Fvbet0NpGOBCmM7UAzODOyI26w586yEWiBAaMryIjd7e"
            Bearer_Token ="AAAAAAAAAAAAAAAAAAAAAHIKkAEAAAAAs7u90SHylxZIW7ZASnn8rhTtnXw%3DPl1X1DU0KEEJhtoFJId4BShmqRqXuRu3Aor1BIbXpZZqBiEuvZ"

            access_token="1598998362379849728-vF6DsVtnYNkTOWFEVY1DcNC29bDN7W"
            access_token_secret ="Xu8wiEgYm155n7smGWyN9kehPNlZiE3ru8KybTcw9COSr"



            #Twitter Authentication
            auth = tweepy.OAuthHandler(API_Key,API_Key_Secret)
            auth.set_access_token(access_token,access_token_secret)

            #Creating  an API object

            api = tweepy.API(auth)
            try:
                api.verify_credentials()
                print('Successful Authentication')
            except:
                print('Failed authentication')





            # Getting individual account tweets
            tweets_biden = api.user_timeline(screen_name='@POTUS', count=200, include_rts=False, tweet_mode='extended')
            tweets_mkbhd = api.user_timeline(screen_name='@MKBHD', count=200, include_rts=False, tweet_mode='extended')
            tweets_fox= api.user_timeline(screen_name='@CNN', count=200, include_rts=False, tweet_mode='extended')
            tweet_list_biden = []
            tweet_list_mkbhd = []
            tweet_list_fox = []




            #Getting search tweets
            query = 'i'
            tweets_vijay = api.search_tweets(q=query,count=200)
            tweet_list_vijay=[]





            for tweet_vijay in tweets_vijay:
                text = tweet_vijay._json["text"]
                tweet_dict_vijay = {"user": tweet_vijay.user.screen_name,
                                    "text": text,
                                    "favourite_count": tweet_vijay.favorite_count,
                                    "retweet_count": tweet_vijay.retweet_count,
                                    "created_at": tweet_vijay.created_at,
                                    "Source": tweet_vijay.source}
                tweet_list_vijay.append(tweet_dict_vijay)



            for tweet_biden in tweets_biden:
                    text = tweet_biden._json["full_text"]
                    tweet_dict_biden = {"user":tweet_biden.user.screen_name,
                           "text":text,
                           "favourite_count":tweet_biden.favorite_count,
                           "retweet_count":tweet_biden.retweet_count,
                           "created_at":tweet_biden.created_at ,
                           "Source" : tweet_biden.source}
                    tweet_list_biden.append(tweet_dict_biden)


            for tweet_mkbhd in tweets_mkbhd:
                    text = tweet_mkbhd._json["full_text"]
                    tweet_dict_mkbhd = {"user":tweet_mkbhd.user.screen_name,
                           "text":text,
                           "favourite_count":tweet_mkbhd.favorite_count,
                           "retweet_count":tweet_mkbhd.retweet_count,
                           "created_at":tweet_mkbhd.created_at ,
                           "Source" : tweet_mkbhd.source}
                    tweet_list_mkbhd.append(tweet_dict_mkbhd)

            for tweet_fox in tweets_fox:
                    text = tweet_fox._json["full_text"]
                    tweet_dict_fox = {"user":tweet_fox.user.screen_name,
                           "text":text,
                           "favourite_count":tweet_fox.favorite_count,
                           "retweet_count":tweet_fox.retweet_count,
                           "created_at":tweet_fox.created_at ,
                           "Source" : tweet_fox.source}
                    tweet_list_fox.append(tweet_dict_fox)




            df1 = pd.DataFrame(tweet_list_biden)
            df2 = pd.DataFrame(tweet_list_mkbhd)
            df3= pd.DataFrame(tweet_list_fox)
            df1.to_csv("BIDEN.csv")
            df2.to_csv("MKBHD.csv")
            df3.to_csv("FOXNews.csv")

            df4 = pd.DataFrame(tweet_list_vijay)
            df4.to_csv("Happy.csv")


twitter_run_etl()




