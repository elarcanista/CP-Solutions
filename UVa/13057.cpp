//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 10000;
vector<int> V[MAXV];
int disc[MAXV];
int dmin[MAXV];
stack<int> s;
bool stacked[MAXV];
int sum, counter;
int snode[MAXV];
int nV[MAXV];

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
				if(snode[u] != snode[v]){
					++nV[snode[v]];
					//cout << u << " " << v << " " << snode[v] << " " << "\n";
				} 
			}
		}
		
		int ans = 0;
		for(int u = 0; u < sum; ++u){
			//cout << nV[u] << "\n";
			if(!nV[u]) ++ans;
		}
		cout << "Case " << i << ": " << ans;
	}
	return 0;
}
