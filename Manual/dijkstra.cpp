#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

vector<ii> graph[MAXV];
int d[MAXV];

void dijkstra(int s, int e){
  priority_queue<ii> q;
  q.push({0,s});
  d[s] = 0;
  while(!q.empty()){
    int w = -q.top().first;
    int u = q.top().second;
    if(u == e) return w;
    q.pop();
    if(w > d[u]) continue;
    for(auto &t: graph[u]){
      int nw = t.first + w;
      init v = t.second;
      if(nw < d[v]){
        d[v] = nw;
        q.push({-nw, v});
      }
    }
  }
  return INF;
}
