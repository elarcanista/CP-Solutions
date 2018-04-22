#include <bits/stdc++.h>
using namespace std;

class heap{
  //nodes are always smaller than its children
  //parent = n/2, left_child = n*2, right_child = n*2+1
  vector<int> vec;

  //O(log(n))
  //changes the tree to solve a single violation to the invariant
  bool fix(unsigned int n){
    //smallest children
    unsigned int l = (n*2 < vec.size() && vec[n] > vec[n*2]? n*2:n);
    unsigned int r = (n*2+1 < vec.size() && vec[n] > vec[n*2+1]? n*2+1:n);
    unsigned int child = (vec[l] < vec[r]? l:r);
    if(vec[n] > vec[child]){
      //swaps and go to the next layer
      int temp = vec[n];
      vec[n] = vec[child];
      vec[child] = temp;
      fix(child);
      return true;
    }
    return false;
  }

public:
  //O(log^2(n))
  //inserts a new element
  void push(int k){
    vec.push_back(k);
    unsigned int n = (vec.size()-1)/2;
    while(n && fix(n)){
      n /= 2;
    }
  }

  //O(log(n))
  //returns the biggest element and deletes it
  int pop(){
    int temp = vec[1];
    vec[1] = vec[vec.size()-1];
    vec.pop_back();
    fix(1);
    return temp;
  }

  heap(){}

  //O(n)
  //converts a list into a min heap
  heap(vector<int> v){
    vec.push_back(0);
    vec.insert(vec.end(), v.begin(),v.end());
    for(unsigned int i = v.size()/2; i > 0; --i){
      fix(i);
    }
  }
};
