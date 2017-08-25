//Author: Andres-Felipe Ortega-Montoya
//graph.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

const int MAXV = 20008;
vector<ii> graph[MAXV];

int d[MAXV];

void dijkstra(int s){
  priority_queue<ii> q;
  q.push({0,s});
  d[s] = 0;
  while(!q.empty()){
    int w = -q.top().first;
    int u = q.top().second;
    q.pop();
    if(w > d[u]) continue;
    for(auto &t: graph[u]){
      int nw = t.first + w;
      int v = t.second;
      if(nw < d[v]){
	d[v] = nw;
	q.push({-nw, v});
      }
    }
  }
}

void reset(int n){
  for(int i = 0; i <= n; ++i){
    graph[i].clear();
    d[i] = INF;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC;
  cin >> TC;
  for(int tc = 1; tc <= TC; ++tc){
    int n, m, s, t;
    cin >> n >> m >> s >> t;
    reset(n);
    for(int i = 0; i < m; ++i){
      int a, b, c;
      cin >> a >> b >> c;
      graph[a].push_back({c, b});
      graph[b].push_back({c, a});
    }
    dijkstra(s);
    if(d[t] == INF) cout << "Case #" << tc << ": unreachable\n";
    else cout << "Case #" << tc << ": " << d[t] << "\n";
  }
}
