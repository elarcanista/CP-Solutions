#include <bits/stdc++.h>
using namespace std;

//O(n)
//merges 2 sorted lists
vector<int> merge(vector<int> &a, vector<int> &b){
  vector<int> c;
  unsigned int ahead = 0, bhead = 0;
  //adds the next smallest element to the result list
  while(ahead < a.size() && bhead < b.size()){
    if(a[ahead] < b[bhead]){
      c.push_back(a[ahead]);
      ++ahead;
    }else{
      c.push_back(b[bhead]);
      ++bhead;
    }
  }
  //adds the rest of the remaining list
  c.insert(c.end(), a.begin() + ahead, a.end());
  c.insert(c.end(), b.begin() + bhead, b.end());
  return c;
}

//O(n^2)
//sorts a list
vector<int> mergeSort(vector<int> &vec){
  if(vec.size() > 1){
    //splits list in 2
    vector<int> a(vec.begin(), vec.begin() + vec.size()/2);
    vector<int> b(vec.begin() + vec.size()/2, vec.end());
    //sorts each half and merges them
    a = mergeSort(a);
    b = mergeSort(b);
    vec = merge(a, b);
  }
  return vec;
}
