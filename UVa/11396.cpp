//UVa 11396 - Claw Decomposition
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INFI = 1 << 30;
const ll INFLL = 1LL << 62;

const int MAXN = 301;
vector<int> g[MAXN];
short g2[MAXN];

void reset(){
	for(int i = 0; i < MAXN; ++i){
		g[i].clear();
		g2[i] = -1;
	}
}

bool bipartite(int source){
	queue<int> q;
	q.push(source);
	g2[source] = 1;
	while(!q.empty()){
		int u = q.front();
		q.pop();
		for(auto &v: g[u]){
			if(g2[v] == -1){
				g2[v] = !g2[u];
				q.push(v);
			}else if(g2[v] == g2[u]) return false;
		}
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int V;
	while(cin >> V && V){
		reset();
		int u, v;
		while(cin >> u >> v && (u || v)){
			g[--u].push_back(--v);
			g[v].push_back(u);
		}
		bool bi = true;
		for(int i = 0; i < V; ++i){
			if(g2[i] == -1 && !bipartite(i)){
				bi = false;
				cout << "NO\n";
				break;
			}
		}
		if(bi)cout << "YES\n";
	}
	return 0;
}
