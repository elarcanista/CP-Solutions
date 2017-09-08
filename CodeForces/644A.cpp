#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie();
	int n, c, r; cin >> n >> r >> c;
	if (n > (r*c)){ 
		cout << -1 << "\n";
		return 0;
	}
	int pair = 0, odd = -1;
	bool d = true;
	for(int i = 0; i < r; ++i){
		for(int j = 0; j < c; ++j){
			if(j) cout << " ";
			if((i + j) % 2)
				if(pair + 2 <= n) cout << (pair += 2);
				else cout << 0;
			else if (odd + 2 <= n) cout << (odd += 2);
				else cout << 0;
		}
		cout << "\n";
	}
}
