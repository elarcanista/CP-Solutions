//Author: Andrés Felipe Ortega Montoya
//URI 1743 - Automated Checking Machine
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int a[5];
	for(int i = 0; i < 5; ++i){
		cin >> a[i];
	}
	bool goog = true;
	for(int i = 0; i < 5; ++i){
		int temp; cin >> temp;
		if(temp == a[i]){
			goog = false; break;
		}
	}
	cout << ((goog)? "Y": "N") << "\n";
	return 0;
}
