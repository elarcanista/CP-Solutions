#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

//UVa 11902 - Dominator 
const int MAXV = 100;
int n;
int v[MAXV][MAXV];
int dom[MAXV][MAXV]; //looks which node dominates which
unordered_set<int> visited;

void clean(){ //resets v and dom
	for(int i = 0; i < MAXV; ++i){
		for(int j = 0; j < MAXV; ++j){
			v[i][j] = 0;
		}
	}
	for(int i = 0; i < MAXV; ++i){
		for(int j = 0; j < MAXV; ++j){
			dom[i][j] = 0;
		}
	}
}

//runs dfs from u ignoring node p. visited nodes are put onto visited 
void dfs(int u, int p){ 
	visited.insert(u);
	for(int i = 0; i < n; ++i){
		if(v[u][i] && i != p && !visited.count(i)){
			dfs(i, p);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	for(int tc = 1; tc <= TC; ++tc){
		clean();
		cin >> n;
		//fills graph
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < n; ++j){
				int temp; cin >> temp;
				v[i][j] = temp;
			}
		}
		visited.clear();
		//looks which nodes are reachable from 0
		dfs(0, -1);
		unordered_set<int> cero = visited;
		for(auto &a: cero){
			dom[0][a] = 1;
		}
		//runs dfs on graph ignoring node i and sees which nodes are no longer reachable
		for(int i = 1; i < n; ++i){
			visited.clear();
			dfs(0, i);
			for(auto &a: cero){
				if(!visited.count(a)){
					dom[i][a] = 1;
				}
			}
		}
		//outputs dominating table
		cout << "Case " << tc << ":\n+";
		for(int j = 0; j < (n*2)-1; ++j){
			cout << "-";
		}
		cout << "+\n";
		for(int i = 0; i < n; ++i){
			cout << "|";
			for(int j = 0; j < n; ++j){
				cout << ((dom[i][j])? "Y": "N") << "|";
			}
			cout << "\n+";
			for(int j = 0; j < (n*2)-1; ++j){
				cout << "-";
			}
			cout << "+\n";
		}
	}
	return 0;
}
