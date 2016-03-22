//Author: Andrés Felipe Ortega Montoya
//UVa 11060 - Beverages
#include <bits/stdc++.h>
using namespace std;

unordered_map<string, vector<string> > v; //stores the graph
unordered_map<string, int> inc; //stores the incoming of each node
vector<string> topo; //stores the topological order
unordered_map<string, int> order; //stores in which order came the nodes

//sees what the topological order is on the graph
void topo_sort(){
	priority_queue<pair<int, string>> q; //order nodes from whichone was given first
	for(auto &a: inc){ //put all 0 incoming nodes into q
		if(!a.second) q.push({order[a.first], a.first});
	}
	while(!q.empty()){
		string s = q.top().second; q.pop();
		topo.push_back(s);
		inc[s] = -1;
		for(int i = 0; i < v[s].size(); ++i){
			--inc[v[s][i]];  //reduces incoming of all conection (is like erase s from the graph)
			if(!inc[v[s][i]]) q.push({order[v[s][i]], v[s][i]}); //if incoming is 0, push it into q
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m, i = 0; 
	while(cin >> n){
		v.clear();
		inc.clear();
		topo.clear();
		order.clear();
		string line, line2;
		while(n--){ //read all nodes
			cin >> line;
			v[line];
			inc[line] = 0;
			order[line] = n;
		}
		cin >> m;
		while(m--){  //read vertex
			cin >> line >> line2;
			v[line].push_back(line2);
			++inc[line2];
		}
		topo_sort();
		//prints answer
		cout << "Case #" << ++i << ": Dilbert should drink beverages in this order:";
		for(auto &a: topo) cout << " " << a;
		cout << ".\n\n";
	}
	return 0;
}
