#include <bits/stdc++.h>
using namespace std;
//UVa 10150 - Doublets
unordered_set<string> visited;
map<string, string> back; //stores from which node another node is called
vector<string> lengths [18]; //stores all words separated by length

//compares two strings, first by length and then alphabetically
struct compare {
	//important const AFTER parameters, otherwise gives an error when calling .count on g or dic
    bool operator()(const string& first, const string& second) const {
    	if(first.size() != second.size()) return first.size() < second.size();
    	for(int i=0; i < first.size() && i < second.size(); ++i) {
	        if( first[i] != second[i]) return (first[i] < second[i]);
    	}
    	return false;
    }
};

map<string, vector<string>, compare> g; //is a graph that connects doublets words
set<string, compare> dic; //stores all words in dictionary

void reset(){
	for(auto &a: back) back[a.first] = "";
}

bool dif1(string a, string b){ // checks if 2 strings differ by 1 letter
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

//traverse through father of a node recursively until it finds a root
void print(string a){
	if(back[a] == "") return;
	print(back[a]);
	cout << "\n" << a;
}

bool bfs(string &a, string &b){ //runs bfs trying to reach b from a and if it's possible
	queue<string> q;
	q.push(a);
	visited.insert(a);
	bool undone = true;
	while(!q.empty() && undone){
		string t = q.front(); q.pop();
		for(auto &c: g[t]){
			if(c == b){
				back[c] = t;
				return 1;	
			} 
			if(!visited.count(c)){
				q.push(c);
				back[c] = t;
				visited.insert(c);
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
		for(int i = 0; i < 17; ++i){
			lengths[i].clear();
		}
		back.clear();
		visited.clear();
		g.clear();
		dic.clear();
		dic.insert(word);
		lengths[word.size()].push_back(word);
		while(getline(cin,word) && word != ""){ //fills dictionary
			if(!dic.count(word)){
				dic.insert(word);
				for(auto &c: lengths[word.size()]){
					if(c.size() > word.size()) break;
					if(dif1(word, c)){
						g[word].push_back(c);
						g[c].push_back(word);
					}
				}
				lengths[word.size()].push_back(word);
			}
		}
		//runs test cases
		getline(cin, word); 
		while(word != ""){
			reset();
			stringstream ss(word);
			ss >> word >> b;
			if(word == b) cout << word;
			else if(bfs(word, b)){
				cout << word;
				print(b);
			}else cout << "No solution.";
			getline(cin, word);
			cout << "\n" << ((word != "")? "\n": "");
			visited.clear();
		}
		getline(cin, word);
		if(word != "") cout << "\n";
	}
	return 0;
}
