#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll sum(ll n){
	return n*(n+1)/2;
}

ll few(ll p, ll g){
	ll a = (p/g)+1;
	ll b = p/g;
	return sum(a-1)*(p%g) + sum(b-1)*(g-(p%g));
}

ll much(ll p, ll g){
	return sum(p-g);	
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll p, g; cin >> p >> g;
	cout << few(p,g) << " " << much(p, g) << "\n";
	return 0;
}
