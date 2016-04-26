//Author: Andrés Felipe Ortega Montoya
//UVa 11631 - Dark roads
#include <bits/stdc++.h>
using namespace std;
 
const int MAXV = 200000;
vector<pair<int, pair<int, int> > > g;
int parent[MAXV];
 
void reset(){
	for(int i = 0; i < MAXV; ++i){
		parent[i] = i;
	}
	g.clear();
}
 
int find(int v){
	if(parent[v] == v) return v;
	return find(parent[v]);
}
 
void onion(int v, int u){
	parent[find(u)] = find(v);
}
 
int kruskal(){
	sort(g.begin(), g.end());
	int price = 0;
	for(auto &a: g){
		int weight = a.first;
		pair<int, int> ver = a.second;
		if(find(ver.first) != find(ver.second)){
			price += weight;
			onion(ver.first, ver.second);
		}
	}
	return price;
}
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int m, n;
	while(cin >> m >> n && (m || n)){
		int price = 0;
		//cout << m << " " << n << "\n";
		reset();
		for(int i = 0; i < n; ++i){
			int x, y, z;
			cin >> x >> y >> z;
			//cout << x << " " << y << " " << z << "\n";
			g.push_back({z,{x, y}});
			price += z;
		}
		cout << price - kruskal() << "\n";
	}
	return 0;
}
