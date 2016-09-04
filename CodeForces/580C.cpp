//Author: Andres Felipe Ortega Montoya
//CodeForces 580C - Kefa and Park
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INFI = 1 << 30;
const ll INFLL = 1LL << 62;
const int MAXN = 100005;

bool cat[MAXN];
vector<int> g[MAXN];
int father[MAXN];
int C;

void reset(){
  for(int i = 0; i < MAXN; ++i){
    cat[i] = 0;
    g[i].clear();
    father[i] = -1;
  }
}

int dfs(int u, int seguidos){
  if(cat[u]) ++seguidos;
  else seguidos = 0;
  if(seguidos > C) return 0;
  if(g[u].size() == 1 && u) return 1;
  int sum = 0;
  for(auto &v: g[u]){
    if(father[u] != v){
      father[v] = u;
      sum += dfs(v, seguidos);
    }
  }
  return sum;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int V;
  while(cin >> V >> C){
    reset();
    for(int i = 0; i < V; ++i){
      cin >> cat[i];
    }
    for(int i = 0; i < V-1; ++i){
      int u, v;
      cin >> u >> v;
      --u;
      --v;
      g[u].push_back(v);
      g[v].push_back(u);
    }
    cout << dfs(0,0) << "\n";
  }
  return 0;
}

