//Author: Andres-Felipe Ortega-Montoya
//kruskal.cpp
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

vector< tuple<double, int, int> > edges;

int MST(int t){
  setUn();
  sort(edges.begin(), edges.end());
  int cost = 0;
  for(int i = 0; i < (int)edges.size(); ++i){
    bool f = merge(get<1>(edges[i]), get<2>(edges[i]));
    cost += (get<0>(edges[i])) * f;
  }
  return cost;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
}
