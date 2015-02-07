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
        stream_result = self.twitter_stream.statuses.sample(language='en')
        print 'twitter stream test'
        for tweet in stream_result:
            print tweet
            break

        print 'successful test'

    def live(self):
        return self.stream()

    def tweet_stream(self, mode='sample', lang='en'):
        if mode == 'firehose':
            stream_result = self.twitter_stream.statuses.firehose(lanugage=lang)
        else:
            stream_result = self.twitter_stream.statuses.sample(language=lang)

        return stream_result

    def tweet_search(self, query = 'test', lang= 'en'):
        return self.twitter_search.search.tweets(q=query,language=lang)

    def user_search(self, query):
        return self.twitter_search.search.tweets(q=query)

    def friend_lookup(self, user_id):
        return self.twitter_search.friends.ids(user_id=user_id)

    def user_lookup_id(self, user_id):
        return self.twitter_search.users.show(user_id=user_id)

    def user_lookup_name(self, user_name):
        return self.twitter_search.users.show(screen_name=user_name)

def test():
    t = TheTwitter(open('simile.smile','r'))

if __name__ == '__main__':
    test()