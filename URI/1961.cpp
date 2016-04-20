//Author: Andrés Felipe Ortega Montoya
//URI 1961 - Jumping Frog
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int j, n, last; cin >> j >> n >> last;
	bool done = true;
	for(int i = 2; i <= n; ++i){
		int temp; cin >> temp;
		if(abs(temp-last) > j){
			cout << "GAME OVER\n";
			done = false;
			break;
		}
		last = temp;
	}
	if(done) cout << "YOU WIN\n";
	return 0;
}
