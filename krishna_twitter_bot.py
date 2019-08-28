#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: pandian_krishna
"""

import tweepy
import os
import random


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'#use a text file to store the previous tweet data 

def retrieveId():           #retrieves previous tweet id
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
    
def storeId(last_seen_id):  #stores new previous id
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return last_seen_id

def reply():    #this functions i the one that responds
    
    last_seen_id = retrieveId() 
    mentions = api.mentions_timeline(last_seen_id)  #checks timeline
    
    for tweet in mentions:
        print(str(tweet.id) + ' - ' + tweet.text + '\n')    #self-reference print
        lastId = tweet.id
        storeId(lastId)
        
        if '#pokedexentry' in tweet.text.lower():
            path =''  #add file directory
            files = os.listdir(path)    #chooses a random file
            index = random.randrange(0, len(files))
            filename = path + '/' + files[index]
            printstringoriginal = '@' + tweet.user.screen_name + '\n' 'Pokedex Number: ' + files[index][0:3] + '\n'
            
            i = 0
            while(files[index][3+i] != '.'):    #gets the pokemon name
                i += 1
            printstringfinal = printstringoriginal + 'Pokemon Name: ' + files[index][3:4+i] 
            
            print(filename) #debugging and this shows what will be tweeted and the file directory
            print('\n')
            print(printstringfinal)
            
            tweet.favorite()    #retweets favorites
            tweet.retweet()     
            api.update_with_media(filename, printstringfinal, tweet.id) #this is the actual tweet
            
def main():
        reply()

if __name__ == "__main__":
    main()
