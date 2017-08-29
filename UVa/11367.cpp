//Author: Andres-Felipe Ortega-Montoya
//11367.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXV = 1000;
const int MAXC = 101;

int p[MAXV];
vector<ii> g[MAXV];
int d[MAXV][MAXC];

int dijkstra(int s, int e, int c){
  priority_queue<tuple<int, int, int> > q;
  q.push({0, s, 0});
  for(int i = 0; i < MAXV; ++i)
    for(int j = 0; j <= c; ++j)
      d[i][j] = INF;
  d[s][0] = 0;
  while(!q.empty()){
    int w = -get<0>(q.top());
    int u = get<1>(q.top());
    int f = get<2>(q.top());
    if(u == e) return w;
    q.pop();
    for(int i = 1; f+i <= c; ++i){
      int nw = w + i*p[u];
      if(nw < d[u][f+i]){
        d[u][f+i] = nw;
        q.push({-nw,u,f+i});
      }
    }
    for(auto& t: g[u]){
      int nf = f - t.first;
      if(nf >= 0 && w < d[t.second][nf]){
        d[t.second][nf] = w;
        q.push({-w,t.second,nf});
      }
    }
  }
  return INF;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int V, E;
  cin >> V >> E;
  for(int i = 0; i < V; ++i){
    int temp;
    cin >> temp;
    p[i] = temp;
  }
  for(int i = 0; i < E; ++i){
    int u, v, w;
    cin >> u >> v >> w;
    g[u].push_back({w,v});
    g[v].push_back({w,u});
  }
  int q;
  cin >> q;
  for(int i = 0; i < q; ++i){
    int c,s,e;
    cin >> c >> s >> e;
    c = dijkstra(s,e,c);
    if(c == INF) cout << "impossible\n";
    else cout << c << "\n";
  }
}
