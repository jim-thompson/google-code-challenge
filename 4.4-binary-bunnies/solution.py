# Code by Jim Thompson, jim.thompson@pobox.com

import math

# Note: this code represents nodes in a binary tree using a triple
# (v, l, r), where v is the value of the node, l is the left subtree,
# and r is the right subtree. A value of None for l or r indicates no
# subtree.

def answer(seq):
    # Your code here

    # Build the tree from the given sequence of values
    node = build_tree(seq)

    # Count the number of duplicate orderings that will produce the
    # same tree
    d = count_insertion_orderings(node)

    # Stringize and return
    return str(d)

def insert_node(node, value):
    # If an empty node is passed in, create and return a new one
    if node is None:
        return (value, None, None)

    # Break up the node tuple.
    (node_v, node_l, node_r) = node

    # Insert the node to the left or right depending on its
    # value. This builds a sorted b-tree (Binary Search Tree).
    if value <= node_v:
        node_l = insert_node(node_l, value)
    else:
        node_r = insert_node(node_r, value)

    # Re-form and return the node tuple.
    node = (node_v, node_l, node_r)
    return node

def build_tree(values):
    # Build up a tree from a sequence of values by iterating over the
    # values and inserting each into the tree.
    node = None
    for v in values:
        node = insert_node(node, v)
    return node

def count_leaves(node):
    # Count the number of leaf nodes in the tree by descending
    # recursively through it.
    if node is None:
        return 0
    (node_v, node_l, node_r) = node
    return 1 + count_leaves(node_l) + count_leaves(node_r)

def count_insertion_orderings(node):
    # Count the number of value sequences that will produce the same
    # tree. This is a Python implementation of an algorithm found on
    # StackOverflow: http://tinyurl.com/nlsl3pw

    # Default case
    if node is None:
        return 1

    # Break up the node tuple
    (node_v, node_l, node_r) = node    

    # Count the leaves in the two subtrees
    count_l = count_leaves(node_l)
    count_r = count_leaves(node_r)

    # Compute the number of combinations in which the subtree values
    # can be interleaved. (l + r)! / l! r!
    nCr = math.factorial(count_l + count_r) / \
          (math.factorial(count_l) * math.factorial(count_r))

    # Now the number of orderings is the number of combinations
    # computed above times the number of orderings that will produce
    # each of the left and right subtrees.
    return nCr * \
           count_insertion_orderings(node_l) * \
           count_insertion_orderings(node_r)

def print_tree(node, depth=0):
    # Test function to print a tree
    if node is None:
        return
    (node_v, node_l, node_r) = node
    print ' ' * 2 * depth, node_v
    print_tree(node_l, depth + 1)
    print_tree(node_r, depth + 1)

def test(values):
    # Test function to build trees and print them.
    n = build_tree(values)

    c = count_leaves(n)
    print c, "Leaves:"

    dups = count_insertion_orderings(n)
    print dups, "Duplicates produce same tree."

    print_tree(n)

# Main for running from the command line
if __name__ == '__main__':
    v1 = [5, 9, 8, 2, 1]
    v2 = [5, 2, 9, 1, 8]
    v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    test(v1)
    test(v2)
    test(v3)
