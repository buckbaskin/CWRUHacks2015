__author__ = 'buckbaskin'

from twitter import *
import os

class Twitter(object):

    def __init__(self,smile_file):
        self.consumer_key = smile_file.readline()[:-1]
        self.consumer_secret = smile_file.readline()

        if (os.path.isfile('simile2.smile'))==False:
            print('oauth_dance')
            token,token_key = oauth_dance('The Insight Project',self.consumer_key,self.consumer_secret,token_filename='simile2.smile')
        else:
            with open('simile2.smile','r') as f:
                token = f.readline()[:-1]
                token_key = f.readline()
        global twitter_object
        twitter_object = Twitter(auth=OAuth(token, token_key,
                                            self.consumer_key, self.consumer_secret))

        twitter_object.search.tweets(q='test')
        print 'successful test'

def test():
    t = Twitter(open('simile.smile','r'))

if __name__ == '__main__':
    test()