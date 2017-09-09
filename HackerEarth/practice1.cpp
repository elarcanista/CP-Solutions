//Author: Andres-Felipe Ortega-Montoya
//practice1.cpp
#include <bits/stdc++.h>
#define DEBUG
#ifdef DEBUG
#define Debug(x) cout << x
#else
#define Debug(x)
#endif

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const ll MAXN = 10000000000008;

ll fact[MAXN];

ll gcd(ll a, ll b){
  return b? gcd(b, a%b) : a;
}

ll f(ll n){
  if(fact[n]) return n;
  return fact[n] = f(n-1)*n;
}

ll choose(ll n, ll k){
  /*ll up = 1;
  for(ll i = k+1; i <= n; ++i){
    up *= i;
  }
  int down = 1;
  for(int i = 1; i <= n-k; ++i){
    down *= i;
    }*/
  return f(n)/f(k)/f(n-k);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int a, b;
  fact[0] = fact[1] = 1;
  cin >> a >> b;
  ll C = 1;, c = gcd(a,b);
  while(c != 1){
    ++C;
    a /= c;
    b /= c;
    c = gcd(a,b);
  }
  for(ll i = 2; i <= min(a,b); ++i){
    if(a%i == 0 && b%i == 0) ++C;
  }
  cout << C << "\n";
}
