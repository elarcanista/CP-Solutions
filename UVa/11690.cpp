//Author: Andrés Felipe Ortega Montoya
//UVa 11690 - Money Matters
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 10000; //max number of vertices
vector<int> g [MAXV]; //undirected graph of friends
int visited[MAXV], owe [MAXV]; //how much money does a person owe
int balance; //which is the money balance per component

void reset(){
	for(int i = 0; i < MAXV; ++i){
		g[i].clear();
		visited[i] = owe[i] = 0;
	} 
}

void dfs(int u){ //tipical dfs, adds owed money to total balance
	visited[u] = true;
	balance += owe[u];
	for(auto &v: g[u]){
		if(!visited[v]) dfs(v);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	while(TC--){
		reset();
		int n, l; cin >> n >> l;
		for(int i = 0; i < n; ++i){ //reads how much money does everyone owes
			cin >> owe[i];
		}
		while(l--){ //reads who is friend with who
			int u, v; cin >> u >> v;
			g[u].push_back(v);
			g[v].push_back(u);
		}
		bool good = true;
		for(int i = 0; i < n; ++i){ //calculates balance per connected component
			if(!visited[i]){
				balance = 0;
				dfs(i);
				if(balance){ //if balance != 0, then it is impossible to split money
					good = false;
					break;
				}
			}
		}
		cout << ((good)? "POSSIBLE":"IMPOSSIBLE") << "\n";
	}
	return 0;
}
