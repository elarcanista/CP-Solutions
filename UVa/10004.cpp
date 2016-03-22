#include <bits/stdc++.h>
using namespace std;
//UVa 10004 - Bicoloring

const int MAXV = 199;
vector<int> g [MAXV];
int color[MAXV];

void cleangraph (){
	for(int i = 0; i < MAXV; ++i){
		g[i].clear();
	}
}

void cleancolor(){
	for(int i = 0; i < MAXV; ++i){
		color[i] = -1;
	}
}

void bfs(){ //runs bfs on graph and checks bicoloreability
	queue<int> q;
	q.push(0);
	color[0] = 1;
	bool coloreable = true;
	while(!q.empty() && coloreable){
		int t = q.front(); q.pop();
		for(auto &a: g[t]){
			if(color[a] == -1){
				color[a] = 1 - color[t];	
				q.push(a);
			} else if(color[a] == color[t]){
				coloreable = false;
				cout << "NOT BICOLORABLE.\n";
				break;
			}
		}
	}
	if(coloreable) cout << "BICOLORABLE.\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int V, E, a, b;
	while((cin >> V)&& V){
		cleangraph();
		cleancolor();
		cin >> E;
		while(E--){
			cin >> a >> b;
			g[a].push_back(b);
			g[b].push_back(a);
		}
		bfs();
	}
	return 0;
}
