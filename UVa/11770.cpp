//UVa 11770 - Lighting Away
//O(|V|+|E|)
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INFI = 1 << 30;
const ll INFLL = 1LL << 62;

const int MAXN = 301;
vector<int> g[MAXN];
stack<int> s;
bool stacked[MAXN];
int indexn[MAXN];
int lowest[MAXN];
int scc[MAXN];
int in[MAXN];
int counter;
int sccCounter;

void reset(){
	for(int i = 0; i < MAXN; ++i){
		g[i].clear();
		stacked[i] = false;
		indexn[i] = lowest[i] = scc[i] = -1;
		in[i] = 0;
	}
	//scc.clear();
	while(!s.empty()) s.pop();
	counter = 0;
	sccCounter = 0;
}

void tarjan(int u){
	lowest[u] = indexn[u] = counter++;
	s.push(u);
	stacked[u] = true;
	for(auto &v: g[u]){
		if(indexn[v] == -1){
			tarjan(v);
			lowest[u] = min(lowest[u], lowest[v]);
		}else if(stacked[v]){
			lowest[u] = min(lowest[u], indexn[v]);
		}
	}
	if(lowest[u] == indexn[u]){
		int v;
		do{
			v = s.top();
			s.pop();
			scc[v] = sccCounter;
			stacked[v] = false;
		}while(v != u);
		++sccCounter;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int V; cin >> V;
	for(int z = 1; z <= V; ++z){
		reset();
		int n, m; cin >> n >> m;
		while(m--){
			int u, v; cin >> u >> v;
			g[--u].push_back(--v);
		}
		for(int i = 0; i < n; ++i){
			if(indexn[i] == -1){
				tarjan(i);
			}
		}
		int noIn = 0;
		for(int u = 0; u < n; ++u){
			for(auto &v: g[u]){
				if(scc[u] != scc[v]){
					++in[scc[u]];
				}
			}
		}
		for(int i = 0; i < sccCounter; ++i){
			if(!in[i]) ++noIn;
		}
		cout << "Case " << z << ": " << noIn << "\n";
	}
	return 0;
}
