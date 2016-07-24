from gpiozero import MotionSensor
import time
import math
import random
from twython import Twython
import requests

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

count = 0
# Tweets sent out
tweet1 = "OM NOM NOM NOM"
tweet2 = "I tried to eat a clock. It was very time consuming."
tweet3 = "I decided that becoming a vegetarian was a missed steak."
tweet4 = "Lunch brought to you by Purr-rina."
tweet5 = "Don't go bacon my heart."
tweet6 = "You're a real pizza work!"

# GIFs attached
gif1 ="http://gph.is/1Ji71oP"
gif2 ="http://gph.is/1sym07H"
gif3 ="http://imgur.com/gallery/mbJYWWw"
gif4 ="http://imgur.com/gallery/EtNci8r"
gif5 ="http://imgur.com/gallery/sgUmC0A"
gif6 ="http://gph.is/1UO2HO5"
gif7 ="http://imgur.com/gallery/NUyttbn"
gif8 ="http://imgur.com/gallery/HvFYkgM"
gif9 ="http://imgur.com/gallery/Grn8K8Q"
gif10 ="http://imgur.com/gallery/h3iscCt"
gif11 = "http://gph.is/1PASG9S"
gif12 = "http://gph.is/17BBJDW"
gif13 = "http://gph.is/1syLf1O"
gif14 = "http://gph.is/29abSJt"
gif15 = "http://gph.is/28LOLbT"
gif16 = "http://gph.is/28PZe5S"
gif17 = "http://gph.is/28Qi3pu"
gif18= "http://imgur.com/t/cat_gifs/xd39slz"

# set tweets to an array
tweetBank = [tweet1, tweet2, tweet3, tweet4, tweet5, tweet6]
#set gifs to an array
gifBank = [gif1, gif2, gif3, gif4, gif5, gif6, gif7, gif8, gif9, gif10, gif11, gif12, gif13, gif14, gif15, gif16, gif17, gif18]

# sense motion
pir = MotionSensor(4)
# loop until detecting motion
while True:
  if pir.motion_detected:
  # randomly select a tweet and gif
randTweet = random.choice(tweetBank)
randGif = random.choice(gifBank)
  print("Motion detected!")
  count = count + 1
# send tweet
  api.update_status(status=randTweet + " %s tweets! %s" %(count, randGif))
  print "Tweeted:" + randTweet + " %s tweets! %s" %(count, randGif)
  # sleep for 10 mins
time.sleep(600.00)
  else:
print("No motion")
time.sleep(5)
