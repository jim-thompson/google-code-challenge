'''
This is the final version that passed google/foo.bar verification test
and now requires cleanup and comments.
'''

import pdb

abscount = 0

def answer(words):
    # your code here

    node.all_nodes = {}

    seen = []
    for c1, c2 in listem(words):
        p = (c1, c2)
        if p not in seen:
            seen.append(p)
            n1 = node.getNode(c1)
            n2 = node.getNode(c2)
            n1.linkTo(n2)
    for (c, n) in node.all_nodes.iteritems():
        n.pruneMultiPathNodes()

    result = ""

    for (c, n) in node.all_nodes.iteritems():
        if not n.n_has_prev:
            while n is not None:
                result += n.n_char
                n = n.n_lexical_next

    return result
        

def listem(words):
    for i in range(len(words) - 1):
        w1 = words[i]
#         for ii in range(i + 1, len(words)):
#             w2 = words[ii]
        w2 = words[i + 1]
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
        self.n_lexical_next = None
        self.n_has_prev = False
        self.n_char = c1
        self.n_next = []

    def linkTo(self, n):
        if n not in self.n_next:
            self.n_next.append(n)

    def longestPathTo(self, target_c, depth):
        pdb.set_trace()
        longest = 0
        if self.n_char == target_c:
            self.show(target_c, depth, 0)
            return 0
        for nn in self.n_next:
            thislen = nn.longestPathTo(target_c, depth + 1)
            thislen += 1
            if thislen > longest:
                longest = thislen
        if longest >= 0:
            self.show(target_c, depth, longest)
            return longest
        self.show(target_c, depth, -98)
        return -98

    def _findMatchingLinkedNodes(self, depth, target_c):
        for nn in self.n_next:
            if nn.n_char == target_c:
                #self.pad(depth)
                # print "depth:", depth, "char:", nn.n_char
                tpl = (depth, nn)
                yield(tpl)
        for nn in self.n_next:
            for (_depth, _nn) in nn._findMatchingLinkedNodes(depth + 1, target_c):
                yield(_depth, _nn)

    def pruneMultiPathNodes(self):
        # Loop over all nodes linked directly from this node
        for nn in self.n_next:
            nn.n_possible = True
        for nn in self.n_next:
            # For each of these directly linked nodes, check whether
            # longer paths also exist.
            for (length, nnn) in self._findMatchingLinkedNodes(1, nn.n_char):
                if length > 1:
                    nn.n_possible = False
        for nn in self.n_next:
            if (nn.n_possible):
                self.n_lexical_next = nn
                nn.n_has_prev = True

    @classmethod
    def dumpNodes(cls):
#         print "Dump 1:"
#         for (c, n) in cls.all_nodes.iteritems():
#             for nn in n.n_next:
#                 print c, "->", nn.n_char,
#                 if nn.n_has_prev:
#                     print
#                 else:
#                     print "<--"

        print "Dump 2:"
        for (c, n) in cls.all_nodes.iteritems():
            print "n.n_char:", n.n_char, "n.n_lexical_next", n.n_lexical_next, "n.n_has_prev", n.n_has_prev
            

#         print "Dump 3:"
#         for (c, n) in cls.all_nodes.iteritems():
#             if not n.n_has_prev:
#                 while n is not None:
#                     print n.n_char, "-->",
#                     n = n.n_lexical_next
                

if __name__ == '__main__':

    print answer(['c', 'cac', 'cb', 'bcc', 'bcc', 'ba'])
    node.dumpNodes()

    print answer(['y', 'z', 'xy'])
    node.dumpNodes()

    print answer(['ba', 'ab', 'cb'])
    node.dumpNodes()
    
#     n_a = node.getNode('a')
#     n_b = node.getNode('b')
#     n_c = node.getNode('c')
#     n_z = node.getNode('z')

#     n_a.linkTo(n_b)
#     n_b.linkTo(n_c)
#     n_c.linkTo(n_z)

#     n_a.linkTo(n_c)
#     n_a.linkTo(n_z)

#     print
#     for (depth, nn) in n_a._findMatchingLinkedNodes(1, 'z'):
#         print "depth:", depth, "char:", nn.n_char

#     print
#     n_a.pruneMultiPathNodes()
#     n_b.pruneMultiPathNodes()
#     n_c.pruneMultiPathNodes()
#     n_z.pruneMultiPathNodes()
    
#     node.dumpNodes()

#     longestPathTo = n_a.longestPathTo('a', 0)
#     print "'a' longest path to to 'a'", longestPathTo

#     longestPathTo = n_a.longestPathTo('b', 0)
#     print "'a' longest path to to 'b'", longestPathTo

#     longestPathTo = n_a.longestPathTo('c', 0)
#     print "'a' longest path to to 'c'", longestPathTo

#     longestPathTo = n_a.longestPathTo('z', 0)
#     print "'a' longest path to to 'z'", longestPathTo

