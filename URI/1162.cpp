//Author: Andrés Felipe Ortega Montoya
//URI 1162 - Train Swapping
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int buble(int train[], int len){
	bool sorted = false;
	int i = len;
	int swaps = 0;
	while(!sorted){
		sorted = true;
		for(int j = 0; j < i-1; ++j){
			if(train[j+1] < train[j]){
				int temp = train[j+1];
				train[j+1] = train[j];
				train[j] = temp;
				sorted = false;
				++swaps;
			}
		}
		--i;
	}
	return swaps;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	while (TC--){
		int len; cin >> len;
		int train[len];
		for(int i = 0; i < len; ++i){
			cin >> train[i];
		}
		cout << "Optimal train swapping takes " <<  buble(train, len) << " swaps.\n";
	}
	return 0;
}
