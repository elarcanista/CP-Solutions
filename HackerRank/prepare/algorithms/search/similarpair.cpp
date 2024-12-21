// https://www.hackerrank.com/challenges/similarpair/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
const int MAXN = 100005;
int k, V;
vector<int> g[MAXN];
int parent[MAXN];
int fen[MAXN];

void update(int i, ll n){
	if(i <= V){
		fen[i] += n;
		update(i+(i&(-i)), n);
	}
}

ll sum(int i){
	if(!i)return 0;
	return sum(i-(i&(-i))) + fen[i];
}

ll dfs(int s){
	ll count = sum(min(V, s+k+1)) - sum(max(1, s-k+1)-1);
	update(s+1, 1);
	for(auto &i:g[s]){
		count += dfs(i);
	}
	update(s+1,-1);
	return count;
}

int root(int s){
	if(parent[s] == -1)return s;
	return root(parent[s]);
}

void reset(){
	for(int i = 0; i < MAXN; ++i){
		fen[i] = 0;
		parent[i] = -1;
		g[i].clear();
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int u, v;
	cin >> V >> k;
	reset();
	while(cin >> u >> v){
		g[--u].push_back(--v);
		parent[v] = u;
	}
	int father = root(0);
	cout << dfs(father) << "\n";
	return 0;
}
