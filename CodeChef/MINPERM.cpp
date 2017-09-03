//Author: Andres-Felipe Ortega-Montoya
//MINPERM.cpp
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
  int TC;
  cin >> TC;
  for(int tc = 1; tc <= TC; ++tc){
    int n;
    cin >> n;
    vector<int> perm = {1};
    if(n>=2){
      perm[0] = 2;
      perm.push_back(1);
    }
    for(int i = 2; i < n; ++i){
      if(i%2){
        int t = perm[i-2];
        perm[i-2] = perm[i-1];
        perm[i-1] = t;
      }
      int t = perm[i-1];
      perm.push_back(t);
      perm[i-1] = i+1;
    }
    cout << perm[0];
    for(int i = 1; i < n;++i){
      cout << " " << perm[i];
    }
    cout << "\n";
  }
}
