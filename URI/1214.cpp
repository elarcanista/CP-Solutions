//Author: Andrés Felipe Ortega Montoya
//URI 1214 - Above Average
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll TC; cin >> TC;
	while(TC--){
		ll N;
		double sum = 0, temp; cin >> N;
		double s[N];
		for(ll i = 0; i < N; ++i){
			cin >> temp;
			s[i] = temp;
			sum += temp;
		}
		sum /= N;
		double sum2 = 0;
		for(auto &a: s){
			if(a > sum) ++sum2;
		}
		sum2 /= N;
		sum2 *= 100;
		cout << fixed << setprecision(3) << sum2 << "%\n";
	}
	return 0;
}
