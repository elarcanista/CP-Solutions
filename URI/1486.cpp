//Author: Andrés Felipe Ortega Montoya
//URI 1486 - Biochemical Digital Circuit
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int P, N, C;
	while (cin >> P >> N >> C && (P || N || C)){
	  //fist it creates the matrix
		int test[N][P];
		for(int i = 0; i < N; ++i){
			for(int j = 0; j < P; ++j){
				cin >> test[i][j];
			}
		}
		//here he counts "toothpicks"
		int tot = 0;
		for(int i = 0; i < P; ++i){
			int cont = (test[0][i])? 1: 0;
			for(int j = 1; j < N; ++j){
				if(test[j][i] && (test[j][i] == test[j-1][i])) ++cont;
				else{
					if(cont >= C)++tot;
					cont = (test[j][i])? 1: 0;
				}
			}
			if(cont >= C)++tot;
		}
		cout << tot << "\n";
	}
	return 0;
}
