#include <bits/stdc++.h>
using namespace std;

//O(n^2)
//Sorts a list
void insertionSort(vector<int> &vec){
  for(unsigned int i = 1; i < vec.size(); ++i){
    int track = i;
    //swap backwards until finding the right place
    while(track && vec[track]<vec[track-1]){
      int temp = vec[track-1];
      vec[track-1] = vec[track];
      vec[track] = temp;
      --track;
    }
  }
}
