//Author: Andrés Felipe Ortega Montoya
//URI 1307 - All You Need Is Love
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

ll pow(ll b, ll e){
	ll a = 1;
	while(e--){
		a *= b;
	}
	return a;
}

ll btoten(string s){
	ll a = 0;
	for(int i = 0; i < s.size(); ++i){
		a += (s[s.size()-1-i] - '0')*pow(2,i);
	}
	return a;
}

ll gcd(ll a, ll b){
	if(!b) return a;
	return gcd(b, a%b);
}

string tentob(ll n){
	string a = "";
	while(n > 1){
		a = to_string(n%2) + a;
		n /= 2;
	}
	a = "1" + a;
	return a;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	for(int i = 1; i <= TC; ++i){
		string a, b; cin >> a >> b;
		ll a1, b1;
		a1 = btoten(a);
		b1 = btoten(b);
		ll c = gcd(a1, b1);
		string c1 = tentob(c);
		cout << "Pair #" << i << ": " 
		     << (c1 == "1" ? "Love is not all you need!" 
		          : "All you need is love!") << "\n";
	}
	return 0;
}
