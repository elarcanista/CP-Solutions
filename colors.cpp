//Author: Andres Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXN = 10;

vector<int> g[MAXN];
int c[MAXN];
int m, V;

void reset(){
	for(int i = 0; i < MAXN; ++i){
		g[i].clear();
		c[i] = INF;
	}
}

bool safe(int u){
	for(auto &v: g[u]){
		if(c[u] == c[v]){
			return false;
		}
	}
	return true;
}

bool color(int u){
	if(u == V) return true;
	for(int i = 0; i < m; ++i){
		c[u] = i;
		if(safe(u) && color(u+1)) return true;
		c[u] = INF;
	}
	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	reset();
	int u, v;
	cin >> V >> m;
	while(cin >> u >> v){
		g[--u].push_back(--v);
		g[v].push_back(u);
	}
	cout << (color(0)) << "\n";
	for(int i = 0; i < V; ++i){
		cout << i+1 << " " << c[i] << "\n";
	}
	return 0;
}
