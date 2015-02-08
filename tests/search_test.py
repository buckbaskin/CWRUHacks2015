__author__ = 'buckbaskin'

import time
import twitter
from data_collection.Twitter import TheTwitter
from data_representation.Network import Network

def testBFS(network, length, user_id):
    network.add_local_blocking(user_id, length)

def testLive(network, length):
    network.add_stream_blocking(length)


if __name__ == '__main__':
    length = 10
    t = TheTwitter(open('..\\simile.smile','r'))
    n = Network(t)

    screenname = 'beBaskin'
    print 'name: '+screenname
    user_id = n.twitter.user_lookup_name(screenname)[0]['id']
    print 'id: '+str(user_id)

    u_id = 2618802005
    print 'id: '+str(u_id)
    print 'screen_name: '+str(n.twitter.user_lookup_id(u_id)[0]['screen_name'])

    #print 'test: id 564193304536166400 '+n.twitter.user_lookup_id(5641933045361664)[0]

    try:
        #testBFS(n, length, user_id)
        testLive(n, length)
    except twitter.TwitterHTTPError as the:
        print 'Please wait for 15 minutes due to rate error'
        time.sleep(15*60)
        print 'And now, what you have all been waiting for....'
