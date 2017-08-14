#python version 3.6.2
#using tweepy 

import tweepy
import itertools

def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page
        
#Api of user roshan_61
consumer_key='zTUSwg4iz6CyHoxj7BeO7ikS3'
consumer_secret='kcAXNwoeJpZbP3881f0C1KGj8mizXP9fcNMLa1u88GrmPSuUQp'
access_token='895530546368880640-xkIOYGwkmJDaSLp6RsdDMmFB3E3Uqtx'
access_token_secret='DpWt7PIIuIvXTYdvLHQJlyyIN12VlnCxW6fpcWa7oRvpY'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#created file for bot followers and following
foll=open("followers.txt","w+")
fr=open("following.txt","w+")

#created file for user followers and following
fileboltiotfollowers=open("followersboltiot.txt","w+")
fileboltiotfollowing=open ("followingboltiot.txt","w+")

#printing boltiot follower and following count
user = api.get_user('boltiot')
print (user.screen_name)
print ('follower cout')
print (user.followers_count)
print ('following cout')
print (user.friends_count)


#printing Bot following
print ('Bot following ------------------------------------------')
for status in tweepy.Cursor(api.friends).items():
    print (status.screen_name)
    fr.write(status.screen_name + "\n") #saving Bot following

#printing Bot follower
print ('Bot follower------------------------------------')
for follower in tweepy.Cursor(api.followers).items():
   print (follower.screen_name)
   foll.write(follower.screen_name + "\n") #saving Bot follower

#printing boltiot follower
print ('user userfollower---------------------------------------')
followers = api.followers_ids(screen_name='boltiot')
for page in paginate(followers, 100):
    results = api.lookup_users(user_ids=page)
    for result in results:
        print (result.screen_name)
        fileboltiotfollowers.write(result.screen_name + "\n") #saving boltiot follower

#printing boltiot following
print ('user userfollowing---------------------------------------')
following = api.friends_ids(screen_name='boltiot')
for page in paginate(following, 100):
    result = api.lookup_users(user_ids=page)
    for resultfollowing in result:
        fileboltiotfollowing.write(resultfollowing.screen_name + "\n") #saving boltiot following
        print (resultfollowing.screen_name)

#all file closed      
foll.close()
fr.close()
fileboltiotfollowers.close()
fileboltiotfollowing.close()


while True:
    #like and retweet @boitiot tweet
    try:
            tweets = api.user_timeline(screen_name = 'boltiot',count='10000')
            for tweet in tweets:
                if not tweet.favorited:
                    api.create_favorite(tweet.id)
                    print('Liked @boltiot tweet')
                if not tweet.retweeted:
                    api.retweet(tweet.id)
                    print ('retweet @botiot tweet')
    except Exception as e:
            print ('Already liked @botiot tweet')

    #like and retweet #IOT tag tweet
    try:
             cricTweet = tweepy.Cursor(api.search, q='#IOT').items()
             for tweet in cricTweet:
                if not tweet.favorited:
                   api.create_favorite(tweet.id)
                   print('Liked #IOT tweet')
                if not tweet.retweeted:
                   api.retweet(tweet.id)
                   print('Retweet #IOT tweet')
    except Exception as e:
            print ('Already tweeted')
    



