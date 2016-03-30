//Author: Andrés Felipe Ortega Montoya
//UVa 10305 - Ordering Tasks
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1000005;
unordered_set<int> v[MAX];
vector<int> sorted; //stores topological sort
int in[MAX]; //stores the income value of nodes
int n, l;

void reset(){
	for(int i = 0; i < MAX; ++i){
		v[i].clear();
		in[i] = 0;
	}	
	sorted.clear();
}

void topo(){ //BFS topological sort (Kahn)
	queue<int> q;
	for(int i = 0; i < n; ++i){
		//cout << i+1 << " " << in[i] << "\n";
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
	while(cin >> n >> l && (n || l)){
		reset();
		while(l--){
			int a, b; cin >> a >> b;
			if(!v[--a].count(--b)){ //reads an edge a single time and increments income of b
				v[a].insert(b);
				++in[b];
			}
		}
		topo();
		if(sorted.size()){ //prints the order
			cout << sorted[0]+1;
			for(int i = 1; i < n; ++i) cout << " " << sorted[i]+1;
		}else{ //if there are no edges, then print all nodes
			cout << 1;
			for(int i = 2; i <=n; ++i) cout << " " << i;
		} 
		cout << "\n";	
	}
	return 0;
}
