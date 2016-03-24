#include <bits/stdc++.h>
using namespace std;
//UVa 11831 - Sticker Collector Robot

const int MAXV = 100;
const int r []= {-1, 0, 1, 0}; //{N, E, S, W}
const int c []= {0, 1, 0, -1};

pair <int, int> coord;
int dir;
int stamp;

char field [MAXV][MAXV];

void clean_field(){
	for(int i = 0; i < MAXV; ++i){
		for(int j = 0; j < MAXV; ++j){
			field[i][j] = '#';
		}
	}
}

void fill_field(int R, int C){ //fills the field to excecute 
	string line;
	for(int i = 0; i < R; ++i){
		getline(cin, line);
		for(int j = 0; j < C; ++j){
			bool found = true;
			switch(line[j]){ //checks if player is found
				case 'N':
					dir = 0;
					break;
				case 'L':
					dir = 1;
					break;
				case 'S':
					dir = 2;
					break;
				case 'O':
					dir = 3;
					break;
				default:
					field[i][j] = line[j];
					found = false;
			}
			if(found){
				field[i][j] = '.';
				coord.first = i;
				coord.second = j;
			}
		}
	}
}

void turn(char d){ //decides what do do every turn
	if(d == 'D'){
		dir = (dir + 1) % 4;
		return;
	}else if(d == 'E'){
		if (!dir) dir = 3;
		else --dir;
		return;
	}
	int newr = coord.first + r[dir];
	int newc = coord.second + c[dir];
	if((newr >= 0 && newr < MAXV) && (newc >= 0 && newc < MAXV) && field[newr][newc] != '#'){ //checks if it is a valid movement
		if(field[newr][newc] == '*'){
			++stamp;
			field[newr][newc] = '.';
		}
		coord.first = newr;
		coord.second = newc;
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int R, C, I;
	while((cin >> R >> C >> I) && (R || C || I)){
		cin.ignore();
		clean_field();
		stamp = 0;
		fill_field(R, C);
		string line;
		getline(cin, line);
		for(int i = 0; i < line.size(); ++i){
			turn(line[i]);
		}
		cout << stamp << "\n";
	}
	return 0;
}
