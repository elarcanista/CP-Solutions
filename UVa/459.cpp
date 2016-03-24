//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
//UVa 459 - Graph Connectivity

map<char, vector<char>>  v;
unordered_set<char> visited;

void clean(){
	v.clear();
	visited.clear();
}

//a simple traversal through all nodes in this component
void dfs(int u){ 
	visited.insert(u);
	for(int i = 0; i < v[u].size(); ++i){
		if(!visited.count(v[u][i])){
			dfs(v[u][i]);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);
	int TC; cin >> TC;
	cin.ignore();
	cin.ignore();
	while(TC--){
		clean();
		string max;
		string line;
		getline(cin, max);
		//fills undirected graph
		while(getline(cin, line) && line != ""){
			v[line[0]].push_back(line[1]);
			v[line[1]].push_back(line[0]);
		}
		//visits every connected component on the graph and count how many are there
		int cc = 0;
		for(char i = 'A'; i <= max[0]; ++i){
			if(!visited.count(i)){
				dfs(i);
				++cc;
			}
		}
		cout << cc << "\n" << (TC? "\n": "");
	}
	return 0;
}
