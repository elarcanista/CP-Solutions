//Author: Andrés Felipe Ortega Montoya
//13057 - Prove Them All
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 10000; // max num of vertex
vector<int> V[MAXV]; // stores graph
int disc[MAXV]; //stores order of traversal
int dmin[MAXV]; //stores minimum disc reachable(only back-edges)
stack<int> s; //helps to identify differen scc
bool stacked[MAXV]; //tells if a node is on s
int sum, counter; //tells how many scc are there - counts number of visited vertex
int snode[MAXV]; //stores to which scc belong each vertex
int nV[MAXV]; //stores how many edges enter the scc

void reset(){
	for(int i = 0; i < MAXV; ++i){
		V[i].clear();
		disc[i] = dmin[i] = snode[i] = -1;
		nV[i] = 0;
		stacked[i] = false;
	}
	while(!s.empty()) s.pop();
	sum = counter = 0;
}

//tarjan's strongly connected components
void scc(int u){
	disc[u] = dmin[u] = counter++;
	s.push(u);
	stacked[u] = true;
	for(auto &v: V[u]){
		if(disc[v] == -1) scc(v);
		if(stacked[v]) dmin[u] = min(dmin[u], dmin[v]);
	}
	if(disc[u] == dmin[u]){
		int v;
		do{
			v = s.top(); s.pop();
			stacked[v] = false;
			snode[v] = sum;
		}while(u != v);
		++sum;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	for(int i = 1; i <= TC; ++i){
		reset();
		int m, n; cin >> m >> n;
		while(n--){
			int a, b; cin >> a >> b;
			V[--a].push_back(--b);
		}
		for(int u = 0; u < m; ++u){
			if(disc[u] == -1){
				scc(u);	
			} 
		}
		
		for(int u = 0; u < m; ++u){
			for(auto &v: V[u]){
				if(snode[u] != snode[v]){ //if u and v are from differents scc sum 1 to income
					++nV[snode[v]];
				} 
			}
		}
		
		int ans = 0;
		for(int u = 0; u < sum; ++u){ //couns scc with 0 income
			if(!nV[u]) ++ans;
		}
		cout << "Case " << i << ": " << ans << "\n";
	}
	return 0;
}
