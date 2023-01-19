//Author: Andrés Felipe Ortega Montoya
//URI 1715 - Handball
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m;
	while(cin >> n >> m){
		int cont = 0;
		for(int i = 0; i < n; ++i){
			bool good = true;
			for(int j = 0; j < m; ++j){
				int temp; cin >> temp;
				if(!temp) good = false;
			}
			if(good)++cont;
		}
		cout << cont << "\n";
	}
	return 0;
}
