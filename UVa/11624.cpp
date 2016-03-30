//Author: Andrés Felipe Ortega Montoya
//UVa 11624 - Fire!
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1000;
char field[MAX][MAX];
const int x []= {0, 1, 0, -1};
const int y []= {1, 0, -1, 0};
int joeX, joeY, r, c;
queue<vector<int> > q;

void reset(){
	for(int i = 0; i < MAX; ++i)
		for(int j = 0; j < MAX; ++j)
			field[i][j] = '#';
	while(!q.empty())q.pop();
}

void bfs(){
	q.push({joeY, joeX, 0, 1});
	while(!q.empty()){
		vector<int> v = q.front(); q.pop();
		for(int i = 0; i < 4; ++i){
			int newY = v[0] + y[i];
			int newX = v[1] + x[i];
			if(newY >= r || newY < 0 || newX >= c || newX < 0){
				if(v[3]){
					cout << v[2]+1 << "\n";
					return;	
				}
			}else{
				if(field[newY][newX] == '.'){
					if(v[3]){
						field[newY][newX] = 'J';
						q.push({newY, newX, v[2]+1, 1});	
					} else{
						field[newY][newX] = 'F';
						q.push({newY, newX, v[2]+1, 0});
					}
				}else if(!v[3] && field[newY][newX] == 'J'){
					field[newY][newX] = 'F';
					q.push({newY, newX, v[2]+1, 0});
				}
			}
		}
	}
	cout << "IMPOSSIBLE\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	while(TC--){
		reset();
		cin >> r >> c;
		cin.ignore();
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				char temp;
				cin.get(temp);
				if(temp == 'J'){
					joeX = j;
					joeY = i;
				}else{
					if(temp == 'F'){
						q.push({i, j, 0, 0});	
					} 
				} 
				field[i][j] = temp;
			}
			cin.ignore();
		}
		bfs();
	}
	return 0;
}
