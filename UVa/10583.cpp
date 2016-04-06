//Author: Andrés Felipe Ortega Montoya
//UVa 10583 - Ubiquitous Religions
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 50000;
vector<int> g [MAXV];
bool visited [MAXV];

void reset(){
	for(int i = 0; i < MAXV; ++i){
		g[i].clear();
		visited[i] = false;
	}
}

void dfs(int u){ //simple dfs
	visited[u] = true;
	for(auto &v: g[u]){
		if(!visited[v]) dfs(v);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC = 1;
	int n, l;
	while(cin >> n >> l && (n || l)){ //reads until reaches a "0 0"
		reset();
		while(l--){ //reads undirected graph of people of same religion
			int u, v; cin >> u >> v;
			g[--u].push_back(--v);
			g[v].push_back(u);
		}
		int rel = 0;
		for(int i = 0; i < n; ++i){ //counts connected components
			if(!visited[i]){
				dfs(i);
				++rel;
			}
		}
		cout << "Case " << TC++ << ": " << rel << "\n";
	}
	return 0;
}
