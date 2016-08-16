//Author: Andrés Felipe Ortega Montoya
//UVa 11770 - Lighting Away
//O(|V|+|E|)
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 10001; //max number of vertices
vector<int> g [MAXV]; //directed graph of dominoes
int low[MAXV], ind[MAXV], con[MAXV], in[MAXV]; //con: scc a vertex belong, in: income of each scc
bool stacked[MAXV];
stack<int> s;
int turn, snode;


void reset(){
	for(int i = 0; i < MAXV; ++i){
		g[i].clear();
		low[i] = ind[i] = con[i] = -1;
		in[i] = 0;
		stacked[i] = false;
	}
	while(!s.empty())s.pop();
	turn = snode = 0;
}

void scc(int u){ //find strongly connected components and marks to which scc belongs a node
	ind[u] = low[u] = turn++;
	stacked[u] = true;
	s.push(u);
	for(auto &v: g[u]){
		if(ind[v] == -1){
			scc(v);
			low[u] = min(low[u], low[v]);
		}else if(stacked[v]) low[u] = min(low[u], ind[v]);
	}
	if(ind[u] == low[u]){
		int v;
		do{
			v = s.top(); s.pop();
			stacked[v] = false;
			con[v] = snode;
		}while(v != u);
		++snode;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	for(int z = 1; z <= TC; ++z){
		reset();
		int n, l; cin >> n >> l;
		while(l--){ //reads graph of dominos
			int u, v; cin >> u >> v;
			g[--u].push_back(--v);
		}
		for(int u = 0; u < n; ++u){ //finds scc
			if(ind[u] == -1) scc(u);
		}
		//calculates income of each scc
		for(int u = 0; u < n; ++u){ 
			for(auto &v: g[u]){
				if(con[u] != con[v]) ++in[con[v]];
			}
		}
		int hand = 0;
		//counts scc with income 0
		for(int i = 0; i < snode; ++i){
			if(!in[i]) ++hand;
		}
		cout << "Case " << z << ": " << hand << "\n";
	}
	return 0;
}
