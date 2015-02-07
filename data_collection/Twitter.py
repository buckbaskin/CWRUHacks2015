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
        self.twitter_search = Twitter(auth=OAuth(token, token_key,
                                            self.consumer_key, self.consumer_secret))
        self.twitter_stream = TwitterStream(auth=OAuth(token, token_key, self.consumer_key, self.consumer_secret))
        search_result = self.twitter_search.search.tweets(q='test')
        print 'twitter search test'
        print search_result['statuses'][0]['text']
        stream_result = self.twitter_stream.statuses.sample(language='en',locations=[-180,-90,180,90])
        print 'twitter stream test'
        for tweet in stream_result:
            print tweet
            break

        print 'successful test'

    def live(self):
        pass

def test():
    t = TheTwitter(open('simile.smile','r'))

if __name__ == '__main__':
    test()