//Author: Andrés Felipe Ortega Montoya
//URI 1661 - Wine Trading in Gergovia
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	long long houses; 
	while(cin >> houses && houses){
		long long tot; cin >> tot;
		long long sum = 0;
		while(--houses){
			long long wine; cin >> wine;
			sum += abs(tot);
			tot += wine;
		}
		cout << sum << "\n";
	}
	return 0;
}
