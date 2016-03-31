#include <stdio.h>

struct node { 
    int data; 
    struct node* left; 
    struct node* right; 
}; 

 
/* 
 Helper function that allocates a new node 
 with the given data and NULL left and right 
 pointers. 
*/ 
struct node* newNode(int data) { 
  struct node* node = new(struct node);    // "new" is like "malloc" 
  node->data = data; 
  node->left = 0; 
  node->right = 0;

  return(node); 
} 
 

/* 
 Give a binary search tree and a number, inserts a new node 
 with the given number in the correct place in the tree. 
 Returns the new root pointer which the caller should 
 then use (the standard trick to avoid using reference 
 parameters). 
*/ 
struct node* insert(struct node* node, int data) { 
  // 1. If the tree is empty, return a new, single node 
  if (node == 0) { 
    return(newNode(data)); 
  } 
  else { 
    // 2. Otherwise, recur down the tree 
    if (data <= node->data) node->left = insert(node->left, data); 
    else node->right = insert(node->right, data);

    return(node); // return the (unchanged) node pointer 
  } 
} 

// Utility that prints out an array on a line. 
void printArray(int ints[], int len) { 
  int i; 
  for (i=0; i<len; i++) { 
    printf("%d ", ints[i]); 
  } 
  printf("\n"); 
} 

/* 
 Recursive helper function -- given a node, and an array containing 
 the path from the root node up to but not including this node, 
 print out all the root-leaf paths. 
*/ 
void printPathsRecur(struct node* node, int path[], int pathLen) { 
  if (node==0) return;

  // append this node to the path array 
  path[pathLen] = node->data; 
  pathLen++;

  // it's a leaf, so print the path that led to here 
  if (node->left==0 && node->right==0) { 
    printArray(path, pathLen); 
  } 
  else { 
  // otherwise try both subtrees 
    printPathsRecur(node->left, path, pathLen); 
    printPathsRecur(node->right, path, pathLen); 
  } 
}

/* 
 Given a binary tree, print out all of its root-to-leaf 
 paths, one per line. Uses a recursive helper to do the work. 
*/ 
void printPaths(struct node* node) { 
  int path[1000];
  printPathsRecur(node, path, 0);
  printf("\n");
}
 
int main(int argc, const char *argv[])
{
  node *n = newNode(5);
  n = insert(n, 2);
  n = insert(n, 9);
  n = insert(n, 1);
  n = insert(n, 8);

  printPaths(n);

  n = newNode(5);
  n = insert(n, 9);
  n = insert(n, 8);
  n = insert(n, 2);
  n = insert(n, 1);

  printPaths(n);

  n = newNode(1);
  n = insert(n, 2);
  n = insert(n, 3);
  n = insert(n, 4);
  n = insert(n, 5);
  n = insert(n, 6);
  n = insert(n, 7);
  n = insert(n, 8);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(2);
  n = insert(n, 1);
  n = insert(n, 3);
  n = insert(n, 4);
  n = insert(n, 5);
  n = insert(n, 6);
  n = insert(n, 7);
  n = insert(n, 8);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(3);
  n = insert(n, 1);
  n = insert(n, 2);
  n = insert(n, 4);
  n = insert(n, 5);
  n = insert(n, 6);
  n = insert(n, 7);
  n = insert(n, 8);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(4);
  n = insert(n, 1);
  n = insert(n, 2);
  n = insert(n, 3);
  n = insert(n, 5);
  n = insert(n, 6);
  n = insert(n, 7);
  n = insert(n, 8);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(5);
  n = insert(n, 1);
  n = insert(n, 2);
  n = insert(n, 3);
  n = insert(n, 4);
  n = insert(n, 6);
  n = insert(n, 7);
  n = insert(n, 8);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(6);
  n = insert(n, 1);
  n = insert(n, 2);
  n = insert(n, 3);
  n = insert(n, 4);
  n = insert(n, 5);
  n = insert(n, 7);
  n = insert(n, 8);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(7);
  n = insert(n, 1);
  n = insert(n, 2);
  n = insert(n, 3);
  n = insert(n, 4);
  n = insert(n, 5);
  n = insert(n, 6);
  n = insert(n, 8);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(8);
  n = insert(n, 1);
  n = insert(n, 2);
  n = insert(n, 3);
  n = insert(n, 4);
  n = insert(n, 5);
  n = insert(n, 6);
  n = insert(n, 7);
  n = insert(n, 9);

  printPaths(n);

  n = newNode(9);
  n = insert(n, 1);
  n = insert(n, 2);
  n = insert(n, 3);
  n = insert(n, 4);
  n = insert(n, 5);
  n = insert(n, 6);
  n = insert(n, 7);
  n = insert(n, 8);

  printPaths(n);

  return 0;
}
