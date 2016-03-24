//Author: Andrés Felipe Ortega Montoya
//UVa 11838 - Come and Go
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 2005;
vector<int> V [MAXV];
int num[MAXV]; //stores order of visit
int num_min[MAXV]; //store minimum num reachable from this (no cross-edges)
bool visited[MAXV]; //tells if a vertex is on s
int _count, sum; //counts visits / scc
stack<int> s; //keep track of cycles

void reset(){
	for(int i = 0; i < MAXV; ++i){
		V[i].clear();
		num[i] = -1;
		num_min[i] = -1;
		visited[i] = false;
	}
	while(!s.empty()) s.pop();
	_count = 0;
	sum = 0;
}

void scc(int u){ //Tarjan's algorithm for SCC
	num[u] = num_min[u] = _count++;
	s.push(u);
	visited[u] = true;
	for(int i = 0; i < V[u].size(); ++i){
		if(num[V[u][i]] == -1) scc(V[u][i]);
		if(visited[V[u][i]])num_min[u] = min(num_min[u], num_min[V[u][i]]);
	}
	if (num[u] == num_min[u]) {
    ++sum;
    int v;
    do {
      v = s.top(); s.pop();
      visited[v] = 0;
    } while (u != v);
  }
} 

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m; 
	while((cin >> n >> m) && n && m){
		reset();
		while(m--){
			int v, w, p; cin >> v >> w >> p;
			V[--v].push_back(--w);
			if(p == 2) V[w].push_back(v);
		}
		for(int i = 0; i < n; ++i){
			if(num[i] == -1) scc(i);
		}
		cout << (sum == 1) << "\n";
	}
	return 0;
}
