__author__ = 'buckbaskin'

from data_collection.Twitter import TheTwitter
from data_representation import Network

def testBFS(network, length, user_id):
    network.add_local_blocking(user_id, length)

def testLive(network, length):
    network.add_stream_blocking(length)


if __name__ == '__main__':
    length = 10
    n = Network(TheTwitter(open('..\\simile.smile')))

    screenname = 'beBaskin'
    print 'name: '+screenname
    user_id = n.twitter.user_search(screenname)
    print 'id: '+user_id


    testBFS(n, length, user_id)
    testLive(n, length)