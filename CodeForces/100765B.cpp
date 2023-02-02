//Author: Andres Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INFI = 1 << 30;
const ll INFLL = 1LL << 62;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n,m;
	while(cin >> n >> m){
		int sum = 0;
		while(m--){
			int bill;
			cin >> bill;
			sum += bill;
		}
		cout << sum%n << "\n";
	}
	return 0;
}