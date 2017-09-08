//Author: Andres-Felipe Ortega-Montoya
//651C.cpp
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

map<int, ll> x;
map<int, ll> y;
map<ii, ll> p;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  ll c = 0;
  for(int i = 0; i < n; ++i){
    int a, b;
    cin >> a >> b;
    ++p[{a,b}];
    ++x[a];
    ++y[b];
  }
  for(auto&u : x) c += u.second*(u.second-1)/2;
  for(auto&u : y) c += u.second*(u.second-1)/2;
  for(auto&u : p) c -= u.second*(u.second-1)/2;
  cout << c << "\n";
}
