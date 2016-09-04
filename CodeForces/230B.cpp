//Author: Andres Felipe Ortega Montoya
//CodeForces 230B - T-primes
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

set<ll> primes;

void fill(ll t){
	for(ll i = 3; i <= t; i+=2){
		bool prime = true;
		for(auto &a: primes){
			if(a*a > i) break;
			if(!(i%a)){
				prime = false;
				break;
			}
		}
		if(prime)primes.insert(i);
	}
	primes.insert(2);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	vector<ll> list;
	ll max = 0;
	while(TC--){
		ll t; cin >> t;
		list.push_back(t);
		if(t > max) max = t;
	}
	fill(sqrt(max)+1);
	for(auto &a: list){
		if(a > 3 && (ll)sqrt(a)*(ll)sqrt(a) == a && primes.count(sqrt(a)))
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	return 0;
}
