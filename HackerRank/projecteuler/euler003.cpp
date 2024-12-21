// https://www.hackerrank.com/contests/projecteuler/challenges/euler003/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
vector<ll> primes;

ll lprime(ll n){
  for(ll i = primes[primes.size()-1]+2; i*i <= n; i+=2){
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
      return primes[i];
    }
  }
  return n;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  primes.push_back(2);
  primes.push_back(3);
  ll t,n; cin >> t;
  while(t--){
    cin >> n;
    ll maxp = lprime(n);
    ll lastp = maxp;
    n /= lastp;
    while((lastp = lprime(n)) != n){
      n /= lastp;
      maxp = max(maxp, lastp);
    }
    cout << max(maxp, lastp) << "\n";
  }
}
