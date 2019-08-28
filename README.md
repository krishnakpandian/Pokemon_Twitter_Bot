# Pokemon_Twitter_Bot
Made a Twitter Bot that will tweet at you a random pokemon image with their dex number and their name!

First of all, I want to thank the original poster for the images of all the pokemon. "https://www.mediafire.com/file/t884pz2tj7hw93t/Pokemon_References.zip/file"
All of the images are official artwork and fair use.

This twitter bot utilizes a lot of the twitter API functions to check if there are any mentions, to like and retweet any new tweets, and to respond. This bot uses an additional text file to store the id of the last tweet so it can continue rerunning it's code. If you are using a database you can store that information there instead. 

There are some limitations from what I've learned as twitter's text limit prevented me from adding the actual pokedex entry of the pokemon due to character limitations and I also found out from testing that Twitter has an api limitation so if you want to have this continuously running in a database import a time function with a time.sleep(900) after the main(). 

This was super fun, the twitter documentation is super nice and I definitely want to make more bots for different platforms and I want to see how well those API's are. This was one of my favorite projects to work on. If you want to see the actual bot, you can look at @kpbr0 on twitter. It isn't active right now because I ran out of credits but you can see all the successful runs it had.
