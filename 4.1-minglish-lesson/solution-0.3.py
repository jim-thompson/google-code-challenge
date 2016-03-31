import pdb

abscount = 0

def answer(words):
    # your code here

    seen = []
    for c1, c2 in listem(words):
        p = (c1, c2)
        if p not in seen:
            seen.append(p)
            print "  --> " + c1 + " and " + c2
            n1 = node.getNode(c1)
            n2 = node.getNode(c2)
            n1.linkTo(n2)

def listem(words):
    for i in range(len(words) - 1):
        w1 = words[i]
        for ii in range(i + 1, len(words)):
            w2 = words[ii]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    yield(w1[j], w2[j])
                    break

class node:
    all_nodes = {}

    @classmethod
    def getNode(cls, c):
        if c not in cls.all_nodes:
            n = node(c)
            cls.all_nodes[c] = n
        else:
            n = cls.all_nodes[c]
        return n
        
    def __init__(self, c1):
        self.n_char = c1
        self.n_next = []

    def linkTo(self, n):
        if n not in self.n_next:
            print "linking" , self.n_char, "to", n.n_char
            self.n_next.append(n)

    def pad(self, depth):
        for i in range(depth):
            print ' ',

    def show(self, target_c, depth, res):
        self.pad(depth)
        print "Node", self.n_char, "looking for", target_c, "=", res

    def longestPathTo(self, target_c, depth):
        pdb.set_trace()
        global abscount
        abscount += 1
        if abscount > 100:
            print "*** TOO MUCH ***"
            self.show(target_c, depth, -99)
            return -99
#        self.pad(depth)
#        print "Node", self.n_char, "looking for", target_c
        longest = 0
        if self.n_char == target_c:
            self.show(target_c, depth, 0)
            return 0
        for nn in self.n_next:
#             if nn.n_char == target_c:
#                 return 1;
#             else:
                thislen = nn.longestPathTo(target_c, depth + 1)
                thislen += 1
                if thislen > longest:
                    longest = thislen
        if longest >= 0:
            self.show(target_c, depth, longest)
            return longest
        self.show(target_c, depth, -98)
        return -98

    def findMatchingLinkedNodes(self, target_c, depth):
        for nn in n_next:
            self.pad(depth)
            print "depth:", depth, "char:", nn.n_char





    @classmethod
    def dumpNodes(cls):
        for (c, n) in cls.all_nodes.iteritems():
            for nn in n.n_next:
                print c, "->", nn.n_char

if __name__ == '__main__':

#    print answer(['c', 'cac', 'cb', 'bcc', 'bcc', 'ba'])
#    print answer(['y', 'z', 'xy'])
#     print answer(['ba', 'ab', 'cb'])
#     print
    
    n_a = node.getNode('a')
    n_b = node.getNode('b')
    n_c = node.getNode('c')
    n_z = node.getNode('z')

    n_a.linkTo(n_b)
    n_b.linkTo(n_c)
    n_c.linkTo(n_z)

    n_a.linkTo(n_c)
    n_a.linkTo(n_z)

    n_a.findMatchingNodes(1, 'z')
    
#     node.dumpNodes()

#     longestPathTo = n_a.longestPathTo('a', 0)
#     print "'a' longest path to to 'a'", longestPathTo

#     longestPathTo = n_a.longestPathTo('b', 0)
#     print "'a' longest path to to 'b'", longestPathTo

#     longestPathTo = n_a.longestPathTo('c', 0)
#     print "'a' longest path to to 'c'", longestPathTo

#     longestPathTo = n_a.longestPathTo('z', 0)
#     print "'a' longest path to to 'z'", longestPathTo

