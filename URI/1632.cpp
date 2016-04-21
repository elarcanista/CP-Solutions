//Author: Andrés Felipe Ortega Montoya
//URI 1632 - Variations
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	while(TC--){
		string pass; cin >> pass;
		long long ways = 1;
		for(int i = 0; i < pass.size(); ++i){
		  //these special letters have 3 ways of being written
		  //all the others have only 2
			switch(pass[i]){
				case 'a':
				case 'A':
				case 'e':
				case 'E':
				case 'i':
				case 'I':
				case 'o':
				case 'O':
				case 's':
				case 'S':
					ways *= 3L;
					break;
				default:
					ways *= 2L;
					break;
			}
		}
		cout << ways << "\n";
	}
	return 0;
}
