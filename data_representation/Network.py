__author__ = 'buckbaskin'

import twitter
from data_collection.Twitter import TheTwitter
import threading
import os

class Network(object):
    def __init__(self, twitter):
        self.nodes = dict()# list of nodes (id , Node object)
        self.connections = dict() # list of connections (id , connection weight))
        self.twitter = twitter

    def add_node(self, node, connections_list):
        print 'add node'
        print 'node node '+str(node)
        self.nodes[node.user_id] = node
        print 'self.nodes worked'
        self.connections[node.user_id] = dict()
        print 'enter try catch'
        try:
            print 'try connections_list as a list'
            for connection in connections_list: #connection is a node_id
                self.connections[node.user_id][connection.user_id] = 1.0
            print 'connections_list as a list'
        except:
            print 'try connections_list as a dict'
            self.connections[node.user_id] = connections_list
            print 'connections_list as a dict'
        return True

    def add_nodes(self, node_list, max_depth):
        count = 0
        for node in node_list:
            print 'node '+str(node['user']['id'])+' added as part of node_list'
            try:
                print 'trying [u][i] --> '+ str(node['user']['id'])
                a = self.make_node(node['user']['id'])
                print 'just a for now'
                b = self.make_connections(node['user']['id'])
                print 'both a and b'
                self.add_node(a, b)
                print 'add node with user extra'
            except twitter.TwitterHTTPError as te:
                print 'pass up twitter rate error'
                raise te
            except:
                try:
                    print 'trying [i]'
                    self.add_node(self.make_node(node['id']), self.make_connections(node['id']))
                    print 'add node without user extra'
                except:
                    print 'trying _'
                    self.add_node(self.make_node(node), self.make_connections(node))
                    print 'add node plain pain train crane'
            count = count+1
            if (count == max_depth):
                break
        print 'return that thing to be true cuz I\'m done'
        return True

    def lookup_node(self, node_id):
        print 'lookup_node '+str(node_id)
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
        print 'making a node for id '+str(user_id)
        data = self.twitter.user_lookup_id(user_id)
        n = Node(user_id, self)
        return n

    def make_connections(self, user_id):
        print 'make connections for '+str(user_id)
        print 'user_id goes to screen name --> '+str(self.twitter.user_lookup_id(user_id)[0]['screen_name'])
        try:
            'friend lookup by user id'
            data = self.twitter.friend_lookup(user_id)
            data = data['ids']
            'friend lookup by user id worked'
        except Exception as e:
            print '----EXCEPTION type '+e.__class__.__name__+'----\n'+str(e)+'\n----EXCEPTION----'
            'friend lookup by screenname'
            #if (isinstance(e,twitter.TwitterHttpError)):
            #    print 'pass up the twitter error, this means I\'m over rate'
            raise e
            #data = self.twitter.friend_lookup(self.twitter.user_lookup_id(user_id)[0]['screen_name'])['ids']
        print 'data data '+str(data)
        connect = dict()
        print 'made connect dict. start for loop'
        for friend in data:
            print 'friend friend '+str(friend)
            #if (not str(friend) == 'next_cursor_str' and not str(friend) == 'previous_cursor'):
            try:
                connect[friend['user']['id']] = 1.0
            except:
                try:
                    connect[friend['id']] = 1.0
                except:
                    connect[friend] = 1.0
        print('return connect')
        return connect

    ### API ###

    def add_stream_thread(self, max_depth):
        '''use this for continuous adding from stream on a separate thread. Possibly infinite calls? planned'''
        t = threading.Thread(target=self.help_stream, args=(self.twitter.live(), max_depth))
        t.daemon = True
        t.start()

    def add_stream_blocking(self, max_depth):
        '''use this for finite adding from stream on the same thread.'''
        print 'add stream blocking '
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

    def __str__(self):
        return '<Node user_id: '+str(self.user_id)+' network '+str(self.network)+" >"

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