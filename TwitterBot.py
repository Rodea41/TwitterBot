
import tweepy
from tweepy import OAuthHandler
from tkinter import * 

#############################################################
"""Supply information given from Twitter developer portal"""
#############################################################
consumer_key = 'Consumer key'
consumer_secret = 'Consumer_secret'
access_token = 'access_token'
access_secret = 'access_token'




####################################################
"""OAuthHandler is a class that takes 2 parameters"""
####################################################
auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#####################################
#Print the username of the account
user = api.me()
#print(user.name)
######################################

"""(OPTIONAL)
#####################################################################
Loop through everyone you are following and follow them back

for follower in tweepy.Cursor(api.followers).items():    
    follower.follow()

print ("Followed everyone that is following " + user.name)
######################################################################
"""


##################################
"""Setting up our TKinter GUI"""
#################################
root = Tk()

label1 = Label( root, text="Search")
E1 = Entry(root, bd =5)

label2 = Label( root, text="Number of Tweets")
E2 = Entry(root, bd =5)

label3 = Label( root, text="Response")
E3 = Entry(root, bd =5)

label4 = Label( root, text="Reply?")
E4 = Entry(root, bd =5)

label5 = Label( root, text="Retweet?")
E5 = Entry(root, bd =5)

label6 = Label( root, text="Favorite?")
E6 = Entry(root, bd =5)

label7 = Label( root, text="Follow?")
E7 = Entry(root, bd =5)



###########################################################
"""Create function to get user input and store in labels"""
###########################################################
def getE1():    
    return E1.get()
def getE2():    
    return E2.get()
def getE3():    
    return E3.get()
def getE4():    
    return E4.get()
def getE5():    
    return E5.get()
def getE6():    
    return E6.get()
def getE7():    
    return E7.get()


"""(OPTIONAL)
#######################################################################
#Setting up Search and respond function
def SearchFunction(keyword, numberOfTweet):
    search = str(keyword) #"Keyword"
    numberOfTweets = numberOfTweet  #"Number of tweets you wish to interact with" #Turn into string if it doesnt work

    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet() ##This can be replaced with tweet.favorite() to fave instead of retweet
            print('Retweeted the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    
    tweetId = tweet.user.id #Store twitter ID
    username = tweet.user.screen_name #Storing Username  
    phrase = 'Can\'t wait to be at Oktoberfest!!' #'What would you like your response to tweet to say'
    
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)                
            print ("Replied with " + phrase)                       
        
        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break
#####################################################################
"""



#########################################################################
"""Setting up Search/Number of Tweets/Response/Reply/Fav/Follow function"""
#########################################################################

def mainFunction():
    getE1()
    search = getE1()
    
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    
    getE3()
    phrase = getE3()
    
    getE4()
    reply = getE4()
    
    getE5()
    retweet = getE5()
    
    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break
    

    if retweet == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print('Retweeted the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed the user')
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break       

submit = Button(root, text ="Submit", command = mainFunction)

"""Label packing"""
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side =BOTTOM)

root.mainloop()

#######################################################

