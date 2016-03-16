#include <bits/stdc++.h>
using namespace std;

map<string, vector<string> > g;
map<string, bool> visited;

bool dif1(string &a, string &b){ // checks if 2 strings differ by 1 letter
	if(a == b) return false;
	bool dif = false;
	for(int i = 0; i < a.size(); ++i){
		if(a[i] != b[i]){
			if(dif) return false;
			dif = true;
		}
	}
	return true;
}
int bfs(string &a, string &b){ //runs bfs trying to reach b from a and returns distance
	if(a == b) return 0;
	queue<pair<string, int> > q;
	q.push({a, 0});
	visited[a] = true;
	bool undone = true;
	while(!q.empty() && undone){
		pair<string, int> t = q.front(); q.pop();
		for(auto &c: g[t.first]){
			if(!visited[c]){
				if(c == b){ 
					return t.second + 1;
				}
				q.push({c, t.second + 1});
				visited[c] = true;
			}
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	string word, b;
	while(TC--){
		visited.clear();
		g.clear();
		while(cin >> word && word != "*"){ //fills dictionary
			if(!g.count(word)){
				g[word];
				for(auto &c: g){
					string a = c.first;
					if(a.size() > word.size()) continue;
					if(dif1(word, a)){
						g[word].push_back(a);
						g[a].push_back(word);
					}
				}
			}
		}
		cin.ignore();
		while(getline(cin, word) && word != ""){
			stringstream ss(word);
			ss >> word >> b;
			cout << word << " " << b << " " << bfs(word, b) << "\n";
			visited.clear();
		}
		if(TC)cout << "\n";
	}
	return 0;
}
