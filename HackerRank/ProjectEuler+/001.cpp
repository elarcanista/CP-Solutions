//Author: Andres Felipe Ortega Montoya
//HackerRank Project Euler #1 - Multiples of 3 and 5 
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 300;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC, n; cin >> TC;
	while(TC--){
		cin >> n;
		--n;
		ll t = n/3;
		ll f = n/5;
		ll b = n/15;
		//sums all multiples of 3 and all multiples of 5
		//substracts multiples of both so that they only sum once
		cout << (t*(t+1)/2*3) + (f*(f+1)/2*5) - (b*(b+1)/2*15)<< "\n";
	}
	return 0;
}
