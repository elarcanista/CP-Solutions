//Author: Andres Felipe Ortega Montoya
//HackerRank Project Euler #2 - Even Fibonacci numbers
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;

vector<ll> f;

ll fib(int m){
	if(m < f.size()) return f[m];
	f.push_back(fib(m-1)*4 + fib(m-2));
	return f[m];
}

ll ind(ll n, ll low, ll up){
	if(low > up) return low;
	ll mid = (up+low)/2;
	if(f[mid] == n) return low;
	if(n > f[mid]) return ind(n, mid+1, up);
	return ind(n, low, mid-1);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll TC, n; cin >> TC;
	f.push_back(0);
	f.push_back(2);
	while(TC--){
		cin >> n;
		while(f[f.size()-1] < n){
			fib(f.size());
		}
		ll index = ind(n, 0, f.size()-1);
		ll temp = 0;
		for(int i = 0; i < index; ++i){
			temp += f[i];
		}
		cout << temp << "\n";
	}
	return 0;
}
