#include <bits/stdc++.h>
using namespace std;
//UVa 429 - Word Transformation
map<string, vector<string> > g;
map<string, bool> visited;
map<string, string> back;

void reset(){
	for(auto &a: back) back[a.first] = "";
}

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

void print(string a){
	if(back[a] == "") return;
	print(back[a]);
	cout << "\n" << a;
}

bool bfs(string &a, string &b){ //runs bfs trying to reach b from a and returns distance 
	queue<string> q;
	q.push(a);
	visited[a] = true;
	bool undone = true;
	while(!q.empty() && undone){
		string t = q.front(); q.pop();
		for(auto &c: g[t]){
			if(c == b){
				back[c] = t;
				return 1;	
			} 
			if(!visited[c]){
				q.push(c);
				back[c] = t;
				visited[c] = true;
			}
		}
	}
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string word, b;
	getline(cin, word);
	while(word != ""){
		visited.clear();
		g.clear();
		g[word];
		while(getline(cin,word) && word != ""){ //fills dictionary
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
		getline(cin, word);
		while(word != ""){
			reset();
			stringstream ss(word);
			ss >> word >> b;
			if(bfs(word, b)){
				cout << word;
				print(b);
			}else cout << "IMPOSSIBLE";
			getline(cin, word);
			cout << "\n" << ((word != "")? "\n": "");
			visited.clear();
		}
		getline(cin, word);
		if(word != "") cout << "\n";
	}
	return 0;
}
