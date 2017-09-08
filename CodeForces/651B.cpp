//Author: Andres-Felipe Ortega-Montoya
//651B.cpp
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

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  map<int, int> s;
  for(int i = 0; i < n; ++i){
    int t;
    cin >> t;
    ++s[t];
  }
  int cont = 0;
  bool good = true;
  while(good){
    good = false;
    map<int, int>::iterator it = s.begin();
    for(;it != s.end(); ++it){
      if(it->second){
        it->second -= 1;
        good = true;
        ++cont;
      }
    }
    --cont;
  }
  ++cont;
  cout << cont << "\n";
}
