//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	while(TC--){
		char letter;
		int a, b;
		cin >> a >> letter >> b;
		if(a == b) cout << (a*b) << "\n";
		else if(letter >= 'a' && letter <= 'z') cout << (a + b) << "\n";
		else cout << (b-a) << "\n";
	}
	return 0;
}
