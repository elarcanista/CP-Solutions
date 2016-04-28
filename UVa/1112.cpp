//Author: Andrés Felipe Ortega Montoya
//UVa 1112 - Mice and Maze
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAXN = 100;
vector<ii> g[MAXN];
int weight[MAXN];

void resetg(){
	for(int i = 0; i < MAXN; ++i){
		g[i].clear();
	}
}

void resetweight(){
	for(int i = 0; i < MAXN; ++i){
		weight[i] = 1 << 30;
	}
}
	
void dijkstra(int s){
	priority_queue<ii, vector<ii>, greater<ii> > q;
	weight[s] = 0;
	q.push({0, s});
	while(!q.empty()){
		int w = q.top().first;
		int v = q.top().second;
		q.pop();
		if(w > weight[v])continue;
		for(auto &u: g[v]){
			int nw = w + u.first;
			if(nw < weight[u.second]){
				weight[u.second] = nw;
				q.push({nw, u.second});
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	while(TC--){
		resetg();
		int v, f, t, e; cin >> v >> f >> t >> e;
		while(e--){
			int x, y, z; cin >> x >> y >> z;
			g[--x].push_back({z, --y});
		}
		int count = 0;
		for(int i = 0; i < v; ++i){
			//if(i == f - 1) continue;
			resetweight();
			dijkstra(i);
			if(weight[f-1] <= t) ++count;
		}
		cout << count << "\n" << (TC? "\n": "");
	}
	return 0;
}
