#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
vector<ll> primes;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  primes.push_back(2);
  ll n; cin >> n;
  for(ll i = 3; i*i <= n; i+=2){
    bool prime = true;
    for(ll p = 0; p < primes.size() && primes[p]*primes[p] <= i; ++p){
      if(i%primes[p] == 0){
        prime = false;
        break;
      }
    }
    if(prime){
      primes.push_back(i);
    }
  }
  for(ll i = primes.size()-1; i >= 0; --i){
    if(n % primes[i] == 0){
      cout << primes[i];
      break;
    }
  }
}
