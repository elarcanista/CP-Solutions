//Author: Andrés Felipe Ortega Montoya
//URI 1828 - Bazinga!
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	int a [][5] = {{-1,0,1,1,0},{1,-1,0,0,1},{0,1,-1,1,0},{0,1,0,-1,1},{1,0,1,0,-1}};
	for(int i = 1; i <= TC; ++i){
		string shel, raj; cin >> shel >> raj;
		int s, r;
		if(shel == "pedra") s = 0;
		if(shel == "papel") s = 1;
		if(shel == "tesoura") s = 2;
		if(shel == "lagarto") s = 3;
		if(shel == "Spock") s = 4;
		
		if(raj == "pedra") r = 0;
		if(raj == "papel") r = 1;
		if(raj == "tesoura") r = 2;
		if(raj == "lagarto") r = 3;
		if(raj == "Spock") r = 4;
		
		cout << "Caso #" << i << ": ";
		switch(a[s][r]){
			case -1: cout << "De novo!\n"; break;
			case 0: cout << "Raj trapaceou!\n"; break;
			case 1: cout << "Bazinga!\n"; break;
		}
	}
	return 0;
}
