//Author: Andrés Felipe Ortega Montoya
//URI 1855 - Maester's Map
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll col, row;
vector<char> board [100];

bool run(){
	ll x = 0, y = 0;
	char temp = board[y][x];
	while(true){
		if(x >= col || y >= row || x < 0 || y < 0) return false;
		if(board[y][x] != '.'){
			temp = board[y][x];
			board[y][x] = 'N';
		}
		//cout << x << " " << y << " " << temp << "\n";
		switch(temp){
			case '*': return true;
			case '>':
				++x;
				break;
			case '^':
				--y;
				break;
			case '<':
				--x;
				break;
			case 'v':
				++y;
				break;
			default:
				return false;
		}
	}
}

int main() {
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	cin >> col >> row;
	for(ll i = 0; i < row; ++i){
		cin.ignore();
		for(ll j = 0; j < col; ++j){
			char temp = getchar();
			board[i].push_back(temp);
		}
	}/*
	for(auto &a: board){
		for(auto &b: a){
			cout << b; 
		}
		cout << "\n";
	}*/
	cout << (run()? "*": "!") << "\n";
	return 0;
}
