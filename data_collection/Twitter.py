__author__ = 'buckbaskin'

from twitter import *
import os

class TheTwitter(object):

    def __init__(self,smile_file):
        self.consumer_key = smile_file.readline()[:-1]
        self.consumer_secret = smile_file.readline()

        if (os.path.isfile('..\\simile2.smile'))==True:
            print 'use shifted file'
            with open('..\\simile2.smile') as f:
                token = f.readline()[:-1]
                token_key = f.readline()[:-1]

        elif (os.path.isfile('simile2.smile') == False):
            print('oauth_dance')
            token,token_key = oauth_dance('The Insight Project',self.consumer_key,self.consumer_secret,token_filename='..\\simile2.smile')

        else:
            print 'use existing file'
            with open('simile2.smile','r') as f:
                token = f.readline()[:-1]
                token_key = f.readline()[:-1]
                #print '|'+token+'|'
                #print '|'+token_key+'|'
        #print 'making the twitter_object'
        self.twitter_search = Twitter(auth=OAuth(token, token_key,
                                            self.consumer_key, self.consumer_secret))
        self.twitter_stream = TwitterStream(auth=OAuth(token, token_key, self.consumer_key, self.consumer_secret))
        search_result = self.twitter_search.search.tweets(q='test')
        #print 'twitter search test'
        #print search_result['statuses'][0]['text']
        stream_result = self.twitter_stream.statuses.sample(language='en')
        #print 'twitter stream test'
        for tweet in stream_result:
            #print tweet
            break

        print 'successful twitter creation test'

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

    def friend_lookup(self, usr_id):
        print 'friend lookup for |'+str(usr_id)+'|'
        a = self.twitter_search.friends.ids(user_id=usr_id)
        print 'a a a '+str(a)
        print 'friend lookup complete for |'+str(usr_id)+'|'
        return a

    def user_lookup_id(self, user_id):
        '''returns a twitter user object, lookup 1 by id'''
        print 'lookup by id '+str(user_id)
        return self.twitter_search.users.lookup(user_id=user_id)

    def user_lookup_name(self, user_name):
        print 'lookup by name '+str(user_name)
        '''returns a twitter user object, lookup 1 by screen_name'''
        return self.twitter_search.users.lookup(screen_name=user_name)

    def bfs(self, root_id):
        b = BreadthFirst(root_id)
        return b

    ### API ###
    def live(self):
        '''Use this for streaming live generic data'''
        return self.twitter_stream.statuses.sample(language='en')
    def fill(self, user_id):
        '''Use this for filling out a network around a user'''
        return self.bfs(user_id)
    def user(self, user_id):
        '''Equivalent to fill. Complete a network around a user'''
        return self.fill(user_id)

class BreadthFirst(object):

    def __init__(self, node_id):
        self.queue = [node_id]

    def __iter__(self):
        return self

    def next(self):
        if not self.queue: raise StopIteration
        node = self.queue.pop(0) #node id
        self.queue += node.children
        return node

def test():
    t = TheTwitter(open('..\\simile.smile','r'))

if __name__ == '__main__':
    test()