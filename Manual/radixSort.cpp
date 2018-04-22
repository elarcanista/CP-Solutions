#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

//O(log(n))
//returns the digit d in base b of a number n
int digit(int n, int b, int d){
  for(int i = 0; i < d; ++i) //n/(b^d)
    n /= b;
  return n-(n/b*b); //n%b
}

//O(n+b)
//sorts a list
vector<int> &countingSort(vector<int> &v, int b, int d){
  vector<int> buckets[b];
  memset(buckets,0,sizeof(buckets));
  //adds all items with key k into bucket k
  for(auto &n:v)
    buckets[digit(n,b,d)].push_back(n);
  vector<int> *ans = new vector<int>;
  for(auto &i:buckets)
    for(auto &j:i)
      ans->push_back(j);
  return *ans;
}

//O((n+b)*log_b(k)) with k being the max element
vector<int> &radixSort(vector<int> &v, int b){
  int maxn = (*max_element(v.begin(), v.end()));
  int d = 0;
  //counting sort by each digit
  while(maxn){
    maxn /= 2;
    v = countingSort(v, b, d++);
  }
  return v;
}

//O(n*c) with max element k <= n^c
vector<int> &radixSort(vector<int> &v){
  return radixSort(v, v.size());
}
