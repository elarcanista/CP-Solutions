//Author: Andres-Felipe Ortega-Montoya
//10179.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAXN = 1E9 + 7;
vector<int> primes;
bitset<MAXN> posibles;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  primes.push_back(2);
  for(int i = 3; i*i<=MAXN; i+=2){
    if(!posibles[i]){
      primes.push_back(i);
      for(int j = i*i; j*j <= MAXN; j+=i){
	posibles.set(j);
      }
    }
  }
  while(cin >> n && n){
    int temp = n;
    for(auto& a: primes){
      if(a >= n) break;
      if(n%a == 0){
	temp /= a;
	temp *= a-1;
	while(n%a == 0) n/= a;
      }
    }
    if(n != 1){
      temp /= n;
      temp *= n-1;
    }
    cout << temp << "\n";
  }
}
