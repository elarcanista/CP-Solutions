#include <bits/stdc++.h>
using namespace std;

int main() {
	//freopen("A-large-practice.in", "r", stdin);   reads input from file
	freopen("A-large-practice.out", "w", stdout);   writes output to a file
	long long TC; cin >> TC;
	for (long long i = 1; i <= TC; ++i){
		long long n; cin >> n;
		vector<long long> a;
		vector<long long> b;
		for(long long j = 0; j < n; ++j){
			long long t; cin >> t;
			a.push_back(t);
		}
		for(long long j = 0; j < n; ++j){
			long long t; cin >> t;
			b.push_back(t);
		}
		sort(a.begin(), a.end());  //sort both vectors
		sort(b.begin(), b.end());
		long long sum = 0;
		for(long long j = 0; j < a.size(); ++j){  //matches biggest a with smallest b
			sum += a[j]*b[b.size()-1-j];
		}
		cout << "Case #" << i << ": " << sum << "\n";
	}
	return 0;
}
