#include <bits/stdc++.h>

class AVL{
  int key;
  AVL *left;
  AVL *right;
  int height;
  bool leaf;

  //O(1)
  //tells if the node is left or right heavy
  int balance(){
    if(leaf)
      return 0;
    return right->height - left->height;
  }

  //O(1)
  //converts X(Y(A,B),C) into Y(A,X(B,C)) (being pre-orders of trees)
  AVL *rightRotate(){
    AVL *y = left;
    left = y->right;
    y->right = this;
    height = max(left->height, right->height)+1;
    y->height = max(y->left->height, y->right->height)+1;
    return y;
  }

  //O(1)
  //converts X(A,Y(B,C)) into Y(X(A,B),C) (being pre-orders of trees)
  AVL *leftRotate(){
    AVL *y = right;
    right = y->left;
    y->left = this;
    height = max(left->height, right->height)+1;
    y->height = max(y->left->height, y->right->height)+1;
    return y;
  }

public:
  //O(log(n))
  //Inserts a new element and balances the tree
  AVL* insert(int n){
    //Normal BST insert
    if(leaf)
      return new AVL(n);
    if (n < key)
      left = left->insert(n);
    else
      right = right->insert(n);
    height = 1 + max(left->height, right->height);
    //Left heavy case
    if (balance() < -1){
      if(left->balance() > 0)
        left = left->leftRotate();
      return rightRotate();
    }
    //Right heavy case
    if (balance() > 1){
      if(right->balance() < 0)
        right = right->rightRotate();
      return leftRotate();
    }
    return this;
  }

  //O(n)
  //Fills a list with the tree nodes in in-order
  void AVLSort(vector<int> &v){
    if(!leaf){
      left->AVLSort(v);
      v.push_back(key);
      right->AVLSort(v);
    }
  }

  //Null node
  AVL():key(0), left(NULL), right(NULL), height(-1),leaf(true){}

  AVL(int key):key(key), left(new AVL()), right(new AVL()), height(0),
               leaf(false){}
};
