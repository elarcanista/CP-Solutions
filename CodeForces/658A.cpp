//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, c, a, ta, b, tb; cin >> n >> c;
	a = ta = b = tb = 0;
	int p[n]; int t[n];
	for(int i = 0; i < n; ++i){
		cin >> p[i];
	}
	for(int i = 0; i < n; ++i){
		cin >> t[i];
	}
	for(int i = 0; i < n; ++i){
		a += max(0, p[i]-c*(ta += t[i]));
		b += max(0, p[n-i-1]-c*(tb += t[n-i-1]));
	}
	cout << ((a == b)? "Tie" : ((a > b)? "Limak" : "Radewoosh")) << "\n";
	return 0;
}