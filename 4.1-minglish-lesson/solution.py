'''
Code by Jim Thompson, jim.thompson@pobox.com

Here is the approach to the problem, as viewed from the 10,000-ft
level: the list of words can be used to generate pairs of letters in
the correct order relative to each other. If we build a DAG from these
pairs such that each node represents a letter, and has a set of
outbound edges to letters that are lexically greater, then that DAG can
be used to construct a sequence of letters in lexical order from
smaller to greater. The given list of words can easily be scanned to
find pairs of letters in lexical order; these pairs can easily be
assembled into a graph.

A little thought shows that there must be a single path through the
nodes of the DAG such that every node is visited just once, and that
those nodes in that order will represent the characters of the
alphabet in lexical order.

Unfortunately, I do not know enough graph theory to easily find that
path.

However, there are a few corallary facts that I can used to deduce the
single lexical path: between any node and any lexically greater node,
there may be multiple paths. If so, then the shorter path should be
thrown out because it "jumps over" other lexical relationships that we
want to deduce. For example, let us say that we know that b < c, that
b < a, and that c < a. After building our DAG, we can see two
relationships between b and a: b < a, and b < c < a. If we through out
the shorter path b < a, then we are left with b < c < a. In this
simple example, that happens to be the single path describing the
entire letter set, in lexical order. In more complicated sets of words
and letters, many such duplicate paths must be discovered in order to
eliminate the shorter ones. That done, the remaining graph will
contain the unique path covering all letter/nodes in order.
'''

def answer(words):
    # your code here

    # Zero out the class variable containing all created nodes. Don't
    # want data hanging around from last run confusing things.
    Node.all_nodes = {}

    # Make sure nodes_seen exists and is an array.
    nodes_seen = []

    # Stage 1: iterate over the given list of words and use it to
    # build up the DAG. Do this by getting a node representing each
    # letter then linking the two nodes. (We will use an object to
    # represent each node. Each edge will be represented by references
    # to greate nodes, stored in an array in each node.

    # Loop through the given words, comparing adjacent pair (a 2-wide
    # moving window.
    for c1, c2 in listem(words):
        p = (c1, c2)

        # A small optimization: reject pairs we've seen before.
        if p not in nodes_seen:
            nodes_seen.append(p)

            # Get nodes corresponding to each of the letters.
            n1 = Node.getNode(c1)
            n2 = Node.getNode(c2)

            # Create a link from the node representing the lexically
            # lesser letter to the node representing the lexically
            # greater letter.
            n1.linkTo(n2)

    # Stage 2: Iterate over the nodes in the DAG, in the order they
    # were created (the simplest way at this point). For each node,
    # conduct a "pruning" to reject shorter paths between any given
    # pair of nodes in favor of longer paths representing those
    # nodes. (See discussion at top of file.)

    for (c, n) in Node.all_nodes.iteritems():
        n.pruneMultiPathNodes()

    # Stage 3: The hard part is done. Now we must build up the string
    # representing the letters of the alphabet in lexical order.

    result = ""

    # First we must find the node that represents the smallest
    # possible letter. Logically, that node will be the only one that
    # has no previous node.
    for (c, n) in Node.all_nodes.iteritems():
        if not n.n_has_prev:

            # We've found the starting node. Now follow the edges
            # through the succession of nodes. For each node, append
            # the letter it represents to the string.
            while n is not None:
                result += n.n_letter
                n = n.n_lexical_next

    # All done!
    return result
        

# Iterate over a list of words in lexical order and generate pairs of
# letters for the DAG.
def listem(words):

    # Iterate over the words
    for i in range(len(words) - 1):

        # Get w1 and w2, representing adjacent pairs of words.
        w1 = words[i]
        w2 = words[i + 1]

        # Iterate through the letters in each word until we find the
        # pair that defines the lexical order of the words.
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:

                # "Return" the pair. Not that the use of yield turns
                # this function into a generator.
                yield(w1[j], w2[j])
                break

# Objecs of class Node will represent each letter in the alphabet.
class Node:

    # Dictionary containing all nodes created.
    all_nodes = {}

    # Get a node representing the given letter. If the node for this
    # letter has already been created, return it. If not, then create
    # the node and add it to the dictionary before returning.

    @classmethod
    def getNode(NodeClass, letter):
        # Node in the dictionary?
        if letter not in NodeClass.all_nodes:

            # No, create it now.
            node = Node(letter)
            NodeClass.all_nodes[letter] = node
        else:
            #Yes!
            node = NodeClass.all_nodes[letter]

        # Return the node.
        return node
        
    def __init__(self, letter):
        self.n_lexical_next = None
        self.n_has_prev = False
        self.n_letter = letter
        self.n_linked = []

    # To this node add the given node as a linked-to node.
    def linkTo(self, n):
        if n not in self.n_linked:
            self.n_linked.append(n)

    # Find the longest path between this node and any node
    # representing the given letter. This function is recursive, so
    # the recursion depth is passed in and passed - incremented - in
    # subsequent calls.
    def longestPathTo(self, target_letter, depth):
        longest = 0

        # If *this* is the node representing the given letter, then
        # the depth defaults to zero and we can return.
        if self.n_letter == target_letter:
            return 0

        # Loop through this node's linked-to nodes.
        for nn in self.n_linked:

            # For each directly linked node, find the longest path
            # through the DAG to the node representing the given
            # letter.
            thislen = nn.longestPathTo(target_letter, depth + 1)

            # Check to see whether this is a longer path than
            # previously encountered.
            thislen += 1
            if thislen > longest:
                longest = thislen

        # If we've found a positive length then return it as the value
        # of this function.
        if longest >= 0:
            return longest

        # Execution should never reach this point (given the
        # guarantees in the problem statement), but if it does, return
        # a dummy value for debugging.
        return -98


    # Generator function to search through all nodes that are
    # descendents of this node, looking for nodes representing the
    # given letter. When matches are found, yield them to the calling
    # function.

    def _findMatchingLinkedNodes(self, depth, target_letter):

        # First: loop through the directly linked nodes. For each
        # match found, yield a tuple reprsenting (a) the search depth
        # where the match was found, and (b) the node found.
        for nn in self.n_linked:
            if nn.n_letter == target_letter:

                # Found a match, create and return the tuple.
                tpl = (depth, nn)
                yield(tpl)

        # Next: use recursion to search through the deeper-linked
        # nodes.
        for nn in self.n_linked:
            for (_depth, _nn) in nn._findMatchingLinkedNodes(depth + 1, target_letter):
                yield(_depth, _nn)

    # Find every node linked from this node, find any nodes that are
    # linked by multiple paths. Eliminate the shorter paths. This is
    # where we find, for each linked node, the node that lexically
    # follows this node. We do this by iterating over the directly
    # linked nodes; any directly linked node that ALSO has a longer
    # path is not a candidate for this node's lexical next.
    def pruneMultiPathNodes(self):

        # Mark all nodes as possibly being the lexical-next node.
        for nn in self.n_linked:
            nn.n_possible = True

        # Loop over all nodes linked directly from this node
        for nn in self.n_linked:

            # For each of these directly linked nodes, check whether
            # longer paths also exist.
            for (length, nnn) in self._findMatchingLinkedNodes(1, nn.n_letter):
                if length > 1:
                    #  Longer path exists, therefore it's not possible
                    #  that the node is lexically next.
                    nn.n_possible = False

        # Now iterate over the directly linked nodes. Find the node
        # that's possibly the lexical next; there will only be one
        # possible next node, which MUST be the lexical next. 
        for nn in self.n_linked:
            if (nn.n_possible):

                # If it's possible... it must be.
                self.n_lexical_next = nn

                # Also note which nodes have previous nodes - we'll
                # use this later to find the starting node (it'll be
                # the one that has no previous.)
                nn.n_has_prev = True

    @classmethod
    def dumpNodes(NodeClass):
        print
        print "Dump part 1:"
        for (c, n) in NodeClass.all_nodes.iteritems():
            for nn in n.n_linked:
                print c, "->", nn.n_letter,
                if nn.n_has_prev:
                    print
                else:
                    print "<--"

        print "Dump part 2:"
        for (c, n) in NodeClass.all_nodes.iteritems():
            print "n.n_letter:", n.n_letter, "n.n_lexical_next", n.n_lexical_next, "n.n_has_prev", n.n_has_prev
            

        print "Dump part 3:"
        for (c, n) in NodeClass.all_nodes.iteritems():
            if not n.n_has_prev:
                while n is not None:
                    print n.n_letter, "-->",
                    n = n.n_lexical_next


if __name__ == '__main__':

    print answer(['c', 'cac', 'cb', 'bcc', 'bcc', 'ba'])
    Node.dumpNodes()

    print answer(['y', 'z', 'xy'])
    Node.dumpNodes()

    print answer(['ba', 'ab', 'cb'])
    Node.dumpNodes()
