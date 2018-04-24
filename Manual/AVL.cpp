#include <bits/stdc++.h>
#include "BST.cpp"

//Self-balanced BST
class AVL: public BST{
public:
  int height;

  //Null node for easier handling
  AVL():BST(), height(-1){}

  AVL(int key):BST(new AVL(), new AVL(), key),height(0){}

private:
  //O(1)
  //tells if the node is left or right heavy
  int getBalance(){
    if(leaf)
      return 0;
    return right()->height - left()->height;
  }

  //O(1)
  //converts X(Y(A,B),C) into Y(A,X(B,C)) (being pre-orders of trees)
  AVL *rightRotate(){
    AVL *y = left();
    leftChild = y->right();
    y->rightChild = this;
    height = max(left()->height, right()->height)+1;
    y->height = max(y->left()->height, y->right()->height)+1;
    return y;
  }

  //O(1)
  //converts X(A,Y(B,C)) into Y(X(A,B),C) (being pre-orders of trees)
  AVL *leftRotate(){
    AVL *y = right();
    rightChild = y->left();
    y->leftChild = this;
    height = max(left()->height, right()->height)+1;
    y->height = max(y->left()->height, y->right()->height)+1;
    return y;
  }

  //O(1)
  //corrects a single violation to the invariant
  AVL* balance(){
    height = 1 + max(left()->height, right()->height);
    //Left heavy case
    if (getBalance() < -1){
      if(left()->getBalance() > 0)
        leftChild = left()->leftRotate();
      return rightRotate();
    }
    //Right heavy case
    if (getBalance() > 1){
      if(right()->getBalance() < 0)
        rightChild = right()->rightRotate();
      return leftRotate();
    }
    return this;
  }

public:
  //O(log(n))
  //Inserts a new element. Returns the root of the new balanced tree.
  virtual AVL* insert(int n){
    //Normal BST insert
    if(leaf)
      return new AVL(n);
    if (n < key)
      leftChild = left()->insert(n);
    else
      rightChild = right()->insert(n);
    return balance();
  }

  //O(log(n))
  //Removes an element. Returns the root of the new balanced tree.
  virtual AVL* remove(int n){
    //Normal BST remove
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
      key = right()->minNode()->key;
      rightChild = right()->remove(key);
    }
    return balance();
  }

  virtual AVL *left(){
    return dynamic_cast<AVL*>(BST::left());
  }

  virtual AVL *right(){
    return dynamic_cast<AVL*>(BST::right());
  }
};
