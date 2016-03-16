#include <bits/stdc++.h>
using namespace std;

const int MAXV = 100;
vector<int> g[MAXV];
bool visited[MAXV];

void dfs(int u){ //visit reachable vertex on graph
	for(auto &v: g[u]){
		if(!visited[v]){
			visited[v] = true;
			dfs(v);	
		} 
	}
}

void cleangraph (){
	for(int i = 0; i < MAXV; ++i){
		g[i].clear();
	}
}

void cleanvisited(){
	for(int i = 0; i < MAXV; ++i){
		visited[i] = false;
	}
}

void count(int m){ //counts unreachable vertexs
	vector<int> no;
	for(int i = 0; i < m; ++i){
		if(!visited[i]) no.push_back(i);
	}
	cout << no.size();
	for(auto &a: no){
		cout << " " << ++a;
	}
	cout << "\n";
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int V, a, b, n, s;
	while((cin >> V) && V){
		cleangraph();
		cleanvisited();
		while((cin >> a) && a--){
			while((cin >> b) && b){
				g[a].push_back(--b);
			}
		}
		cin >> n;
		while(n--){
			cin >> s;
			dfs(--s);
			count(V);
			cleanvisited();
		}
	}
	return 0;
}
