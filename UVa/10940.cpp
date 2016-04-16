//Author: Andrés Felipe Ortega Montoya
//UVa 10940 - Throwing cards away II
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	double n;
	while(cin >> n && n){
		if(n == 1) cout << 1 << "\n";
		else{
		  //the secuence in this problem is:
		  //1 1 2 1 2 3 4 1 2...
			double group = ceil(log2(n/2));
			double top = pow(2, group+1)-1;
			double size = pow(2, group);
			cout << 2*(size - (top - n) - 1) << "\n";
		}
	}
	return 0;
}
