//Author: Andrés Felipe Ortega Montoya
//UVa 11710 - Expensive subway
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

unordered_set<string>tree;
map<string, vector<pair<int, string> > > g;
priority_queue<pair<int, string> > q;

void primq(string s){
	//cout << s << "\n";
	tree.insert(s);
	for(auto &v: g[s]){
		if(!tree.count(v.second)) q.push({-v.first, v.second});
	}
}

int prim(string s){
	primq(s);
	int weight = 0;
	while(!q.empty()){
		int w = -q.top().first;
		string v = q.top().second;
		q.pop();
		//cout << v << "v\n";
		if(!tree.count(v)){
			weight += w;
			primq(v);
		}
	}
	return weight;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, e;
	while(cin >> n >> e && (n || e)){
		tree.clear();
		g.clear();
		for(int i = 0; i < n ; ++i){
			string s; cin >> s;
			//parent[s] = s;
		}
		while(e--){
			string a, b;
			int c;
			cin >> a >> b >> c;
			g[a].push_back({c, b});
			g[b].push_back({c, a});
		}
		string house; cin >> house;
		int weight = prim(house);
		//cout << weight << "\n";
		cout << (tree.size() == n? to_string(weight): "Impossible") << "\n";
	}
	return 0;
}
