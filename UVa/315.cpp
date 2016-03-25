//Author: Andrés Felipe Ortega Montoya
//UVa 315 - Network
#include <bits/stdc++.h>
using namespace std;

const int MAX = 100;
vector<int> V[MAX];
int d[MAX];
int low[MAX];
int paren[MAX];
int artV[MAX]; //stores if a node is an articulation point
int tick;
int crit;

void reset(){
	for(int i = 0; i < MAX; ++i){
		d[i] = low[MAX] = paren[i] = -1;
		V[i].clear();
		artV[i] = false;
	}
	tick = crit = 0;
}

void art(int u){
	d[u] = low[u] = tick++;
	int child = 0;
	for(int i = 0; i < V[u].size(); ++i){
		int v = V[u][i];
		if(d[v] == -1){ //if v is not yet visited
			++child;
			paren[v] = u; //u is parent of v
			art(v);
      low[u]  = min(low[u], low[v]); //updates low
      if (paren[u] == -1 && child > 1) artV[u] = true; //if u is root and has more than 1 child
			if (paren[u] != -1 && low[v] >= d[u]) artV[u] = true; //if u is not root and low of v >= num of u
		}else if(paren[u] != v) low[u] = min(low[u], d[v]); //updates low
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	while(cin >> n && n){
		reset();
		cin.ignore();
		string line;
		int t;
		while(getline(cin, line) && line[0] != '0'){
			stringstream ss(line);
			int u, v; ss >> u;
			--u;
			while(ss >> v){
				V[u].push_back(--v);
				V[v].push_back(u);
			}
		}
		for(int i = 0; i < n; ++i){
			if(d[i] == -1) art(i);
		}
		for(int i = 0; i < n; ++i){
			if(artV[i]){
				 ++crit;
			}
		}
		cout << crit << "\n";
	}
	return 0;
}
