#include <bits/stdc++.h>
using namespace std;

//Bijective function from N^2 to N
long long cantorPairing(long long k1, long long k2){
  return (k1+k2)*(k1+k2+1)/2+k2;
}

//Bijective function from N^n to N
long long cantorPairing(vector<long long> &v){
  long long kn = v.back();
  v.pop_back();
  if(v.empty())
    return kn;
  if(v.size() == 1)
    return cantorPairing(v[0], kn);
  return cantorPairing(cantorPairing(v), kn);
}
