#include <bits/stdc++.h>
using namespace std;
//Timus OJ 1045 - Funny Game 

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXN = 10000;
vector<int> g[MAXN];
int f[MAXN];
int n,k;

bool dfs(int u, int h){
	if(g[u].size() == 1){
		//cout << u+1 << " " << h << " " << h%2 << "\n";
		return h%2;
	}
	bool b = h%2, c = h%2;
	for(auto &a: g[u]){
		if(f[u] == a) continue;
		f[a] = u;
		if(c) b &= dfs(a, h+1);
		else b |= dfs(a,h+1);
	}
	//cout << u+1 << " " << h << " " << b << "\n";
	return b;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	while(cin >> n >> k){
		for(int i = 1; i < n; ++i){
			int u,v; cin >> u >> v;
			g[--u].push_back(--v);
			g[v].push_back(u);
		}
		int temp = -1;
		f[--k] = -1;
		for(auto &a: g[k]){
			f[a] = k;
			if(dfs(a,1) && (temp < 0 || a < temp)) temp = a;
		}
		if(temp < 0){
			cout << "First player loses\n";	
		}else{
		 	cout << "First player wins flying to airport " << temp+1 << "\n";
		}
	}
	return 0;
}
