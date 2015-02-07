__author__ = 'buckbaskin'

from twitter import *
import os

class TheTwitter(object):

    def __init__(self,smile_file):
        self.consumer_key = smile_file.readline()[:-1]
        self.consumer_secret = smile_file.readline()

        if (os.path.isfile('simile2.smile'))==False:
            print('oauth_dance')
            token,token_key = oauth_dance('The Insight Project',self.consumer_key,self.consumer_secret,token_filename='simile2.smile')
        else:
            print 'use existing file'
            with open('simile2.smile','r') as f:
                token = f.readline()[:-1]
                token_key = f.readline()[:-1]
                #print '|'+token+'|'
                #print '|'+token_key+'|'
        print 'making the twitter_object'
        self.twitter_object = Twitter(auth=OAuth(token, token_key,
                                            self.consumer_key, self.consumer_secret))

        self.twitter_object.search.tweets(q='test')
        print 'successful test'

def test():
    t = TheTwitter(open('simile.smile','r'))

if __name__ == '__main__':
    test()