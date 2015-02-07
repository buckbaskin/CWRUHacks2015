__author__ = 'buckbaskin'

from data_collection.Twitter import TheTwitter
import threading
import os

class Network(object):
    def __init__(self, twitter):
        self.nodes = dict()# list of nodes (id , Node object)
        self.connections = dict() # list of connections (id , connection weight))
        self.twitter = twitter

    def add_node(self, node, connections_list):
        self.nodes[node.id] = node
        self.connections[node.id] = dict()
        for connection in connections_list: #connection is a node_id
            self.connections[node.id][connection.id] = 1.0
        return True

    def add_nodes(self, node_list, max_depth):
        count = 0
        for node in node_list:
            self.add_node(node_list)
            count = count+1
            if (count == max_depth):
                break;
        return True

    def lookup_node(self, node_id):
        try:
            return self.nodes[node_id]
        except KeyError as ke:
            self.add_node(self.make_node(node_id))
            return self.lookup_node(node_id)

    def get_connections(self, node_id):
        return self.connections[node_id]

    def help_stream(self, stream_iterator, length):
        count = 0
        for tweet in stream_iterator:
            self.add_node(self.make_node(tweet['id']), self.make_connections(tweet['id']))
            count = count + 1
            if count == length:
                break

    def help_network(self, bfs_iterator, length):
        count = 0
        for tweet in bfs_iterator:
            self.add_node(self.make_node(tweet['id']), self.make_connections(tweet['id']))
            count = count + 1
            if count == length:
                break

    def make_node(self, user_id):
        data = self.twitter.user_lookup_id(user_id)
        n = Node(user_id, self)
        return n

    def make_connections(self, user_id):
        data = self.twitter.friend_lookup(user_id)
        connect = dict()
        for friend in data:
            connect[friend['id']] = 1.0
        return connect

    ### API ###

    def add_stream_thread(self, max_depth):
        '''use this for continuous adding from stream on a separate thread. Possibly infinite calls? planned'''
        t = threading.Thread(target=self.help_stream, args=(self.twitter.live(), max_depth))
        t.daemon = True
        t.start()

    def add_stream_blocking(self, max_depth):
        '''use this for finite adding from stream on the same thread.'''
        self.add_nodes(self.twitter.live(), max_depth)

    def add_local_blocking(self, user_id, max_depth):
        ''' use this for finite adding from a local network on the same thread. '''
        self.add_nodes(self.twitter.fill(user_id), max_depth)

    def add_local_thread(self, max_depth):
        '''Use this for continuous adding from stream on a separate thread. Possibly infinite calls? planned'''
        t = threading.Thread(target=self.help_network, args=(self.twitter.fill(), max_depth))
        t.daemon = True
        t.start()


class Node(object):
    def __init__(self,user_id, network):
        self.user_id = user_id
        self.network = network

    def get_connections(self):
        return self.network.get_connections(self.user_id)

def test():
    #print 'cwd directory'+str(os.getcwd())
    t = TheTwitter(open('..\\simile.smile','r'))
    net = Network(t)
    #print 'network made'
    n = Node('1',net)
    #print 'new node n'
    print 'successful network representation test'

if __name__ == '__main__':
    test()