#pragma once
#include <bits/stdc++.h>

//Binary tree where a node will always have a greater or smaller key than its
//left and right child respectively.
class BST{
public:
  BST *leftChild;
  BST *rightChild;
  int key;
  bool leaf;

  //Null node to facilitate handling
  BST():leftChild(), rightChild(), key(1<<30), leaf(true){}

  BST(int key):leftChild(new BST()), rightChild(new BST()),
               key(key), leaf(false){}

  BST(BST *leftChild, BST *rightChild, int key):
    leftChild(leftChild), rightChild(rightChild), key(key), leaf(false){}

  //O(h). Potentially h=n
  //returns the node with the smallest key
  BST* minNode() {
    if(leaf || left()->leaf)
      return this;
    return left()->minNode();
  }

  //O(h). Potentially h=n
  //returns the node with the largest key
  BST* maxNode()  {
    if(leaf || right()->leaf)
      return this;
    return right()->maxNode();
  }

  //O(h). Potentially h=n
  //returns the node with smallest key greater than n
  BST* succNode(int n)  {
    if(leaf)
      return this;
    if(n < key){
      BST* ans = left()->succNode(n);
      if(ans->leaf)
        return this;
      return ans;
    }
    if(n > key)
      return right()->succNode(n);
    return right()->minNode();
  }

  //O(h). Potentially h=n
  //returns the node with the largest key less than n
  BST* predNode(int n)  {
    if(leaf)
      return this;
    if(n < key)
      return left()->predNode(n);
    if(n > key){
      BST* ans = right()->predNode(n);
      if(ans->leaf)
        return this;
      return ans;
    }
    return left()->maxNode();
  }

  //O(h). Potentially h=n
  //Inserts a new element. Returns the root of the modified tree.
  virtual BST* insert(int n){
    if(leaf)
      return new BST(n);
    if (n < key){
      leftChild = left()->insert(n);
    }else
      rightChild = right()->insert(n);
    return this;
  }

  //O(h). Potentially h=n
  //Removes an element. Returns the root of the modified tree.
  virtual BST* remove(int n){
    if(leaf)
      return this;
    if(n < key)
      leftChild = left()->remove(n);
    else if(n > key)
      rightChild = right()->remove(n);
    else{
      if(left()->leaf)
        return right();
      if(right()->leaf)
        return left();
      key = right()->minNode()->key; //2 children case
      rightChild = right()->remove(key);
    }
    return this;
  }

  //O(n)
  //Fills a list with the tree nodes in in-order
  void sort(vector<int> &v)  {
    if(!leaf){
      left()->sort(v);
      v.push_back(key);
      right()->sort(v);
    }
  }

  virtual BST *left() const { return leftChild; }

  virtual BST *right() const { return rightChild; }
};

//O(n)
//Prints the pre-order traversal of the tree
ostream &operator<<(ostream &os, const BST &tree){
  if(tree.leaf){
    return os;
  }
  os << tree.key;
  if(tree.left()->leaf && tree.right()->leaf){
    return os;
  }
  os << "(";
  os << *tree.left();
  os << ",";
  os << *tree.right();
  os << ")";
  return os;
}
