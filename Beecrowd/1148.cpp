//Author: Andrés Felipe Ortega Montoya
//URI 1148 - Countries at War
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAXN = 500;
vector<ii> g [MAXN];
stack<int> s;
int dist[MAXN];
int low [MAXN];
int order[MAXN];
int curr;
int cscc;
int scc[MAXN];
bool stacked[MAXN];

void resetd(){
	for(int i = 0; i < MAXN; ++i) dist[i] = 1<<30;
}

void reset(){
	for(int i = 0; i < MAXN; ++i){
		g[i].clear();
		low[i] = -1;
		order[i] = -1;
		scc[i] = -1;
		stacked[i] = false;
	}
	while(!s.empty()) s.pop();
	curr = -1;
	cscc = 0;
}

void tarjan(int v){
	low[v] = order[v] = ++curr;
	s.push(v);
	stacked[v] = true;
	for(auto &u: g[v]){
		if(order[u.second] == -1){
			tarjan(u.second);
			low[v] = min(low[v], low[u.second]);
		}else if(stacked[u.second]){
			low[v] = min(low[v], order[u.second]);
		}
	}
	if(low[v] == order[v]){
		int u;
		do{
			u = s.top(); s.pop();
			stacked[u] = false;
			scc[u] = cscc;
		}while(u != v);
		++cscc;
	}
}

void dijkstra(int v, int f){
	priority_queue<ii, vector<ii>, greater<ii> > q;
	q.push({0, v});
	dist[v] = 0;
	while(!q.empty()){
		int u = q.top().second;
		int w = q.top().first;
		q.pop();
		if(w > dist[u]) continue;
		for(auto &x: g[u]){
			int neww = w;
			if(scc[u] != scc[x.second]){
				neww += x.first;
			}
			if(neww < dist[x.second]){
				dist[x.second] = neww;
				q.push({neww, x.second});
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int v, e;
	while(cin >> v >> e && (v || e)){
		reset();
		while(e--){
			int a, b, c; cin >> a >> b >> c;
			g[--a].push_back({c, --b});
		}
		for(int i = 0; i < v; ++i){
			if(order[i] == -1) tarjan(i);
		}
		int k; cin >> k;
		while(k--){
			resetd();
			int a, b; cin >> a >> b;
			//cout << scc[--a] << " " << scc[--b] << "\n";
			dijkstra(--a, --b);
			if(dist[b] == (1<<30)){
				cout << "Nao e possivel entregar a carta\n";
			}else{
				cout << dist[b] << "\n";
			}
		}
		cout << "\n";
	}
	return 0;
}
