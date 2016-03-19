#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll n, l; cin >> n >> l;
	vector<ll> v;
	for(int i = 0; i < n;++i){
		ll temp; cin >> temp;
		v.push_back(temp);
	}
	sort(v.begin(), v.begin()+n);
	ll prev = 0, in = 0, first = v[0], last = l-v[v.size()-1];
	for(auto &a: v){
	//	cout << a << " ";
		if(a-prev > in) in = a-prev;
		prev = a;
	}
	cout << fixed << max((double)first, max((double)last, (double)in/2)) << "\n";
	return 0;
}
