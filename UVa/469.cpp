//Author: Andrés Felipe Ortega Montoya
//UVa 469 - Wetlands of Florida
#include <bits/stdc++.h>
using namespace std;

const int r[] = {-1, -1, 0, 1, 1, 1, 0, -1}; //a little help to move throug the graph
const int c[] = {0, 1, 1, 1, 0, -1, -1, -1};
vector<string> v;

//replace all dots in graph for water again
void fillw(){ 
	for(int i = 0; i < v.size(); ++i){
		for(int j = 0; j < v[i].size(); ++j){
			if(v[i][j] == '.') v[i].replace(j, 1, "W");
		}
	}
}

int bfs(int _r, int _c){
	int count = 1;
	queue<pair<int, int> > q;
	q.push({_r, _c});
	v[_r].replace(_c, 1, "."); 
	while(!q.empty()){
		pair<int, int> p = q.front(); q.pop();
		for(int i = 0; i < 8; ++i){ 
			int newr = p.first + r[i];
			int newc = p.second + c[i];
			//if it is a valid coordinate and it is water, count it
			if(newr >= 0 && newr < v.size() && newc >= 0 && newc < v[0].size() && v[newr][newc] == 'W'){
				++count;
				q.push({newr, newc});
				v[newr].replace(newc, 1, "."); 
			}
		}
	}
	return count;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	cin.ignore();
	cin.ignore();
	while(TC--){
		v.clear();
		string line;
		int i = 0;
		//read graph
		while(getline(cin, line) && (line[0] == 'L' || line[0] == 'W')){
			v.push_back(line);
			++i;
		}
		//read queries
		stringstream ss (line);
		int r, c; ss >> r >> c;
		cout << bfs(r-1, c-1) << "\n";
		fillw();
		while(getline(cin, line) && line != ""){
			stringstream ss2 (line);
			ss2 >> r >> c;
			cout << bfs(r-1, c-1) << "\n";
			fillw();
		}
		if(TC)cout << "\n";
	}
	return 0;
}
