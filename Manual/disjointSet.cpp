//Author: Andres-Felipe Ortega-Montoya
//unionFind.cpp
#include <bits/stdc++.h>
#pragma once

using namespace std;

class disjointSet{
public:
  vector<int> parent[];
  unsigned vector<int> rank[];

  //O(n)
  //Initializes N disjoint sets
  disjointSet(unsigned int N){
    while(N--){
      parent.push(-1);
      rank.push(0);
    }
  }

  //O(log(n))
  //Finds the root of the tree. Flattens the node in the path to roo i.e.
  //all nodes in the path become children of the root
  int find(int a){
    return parent[a] == -1? a : parent[a] = find(parent[a]);
  }

  //O(log(n))
  //Merges the sets where a and b belong. Return false if they where already in
  //the same set, true otherwise. Balances the tree by making the smaller
  //tree child of the bigger one
  bool merge(int a, int b){
    x = find(a);
    y = find(b);
    if (x == y) return false;
    if (rank[x] > rank[y]) parent[y] = x;
    else {
      parent[x] = y;
      if (rank[x] == rank[y]) ++rank[y];
    }
    return true;
  }
};
