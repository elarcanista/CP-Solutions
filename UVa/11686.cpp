//Author: Andrés Felipe Ortega Montoya
//UVa 11686 - Pick up sticks
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1000005;
vector<int> v[MAX];
vector<int> sorted; //stores the topological sort
int in[MAX];
int n, l;

void reset(){
	for(int i = 0; i < MAX; ++i){
		v[i].clear();
		in[i] = 0;
	}	
	sorted.clear();
}

void topo(){ //bfs topological sort (Kahn)
	queue<int> q;
	for(int i = 0; i < n; ++i){
		if (!in[i]) q.push(i);
	}
	while(!q.empty()){
		int p = q.front(); q.pop();
		sorted.push_back(p);
		for(auto &a: v[p]){
			if(!--in[a]) q.push(a);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	while(cin >> n >> l && n && l){
		reset();
		while(l--){
			int a, b; cin >> a >> b;
			v[--a].push_back(--b);
			++in[b];
		}
		topo();
		//if number of elements on topo is less tan number of nodes is because
		//there are nodes which form a cycle
		if(sorted.size() != n) cout << "IMPOSSIBLE\n"; 
		else for(auto &a:sorted) cout << a+1 << "\n";
	}
	return 0;
}
