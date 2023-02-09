//Author: Andres Felipe Ortega Montoya
//HackerRank - Plus Minus
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	float n;
	int a, pos, neg, zer; cin >> n;
	pos = neg = zer = 0;
	for(int i = 0; i < n; ++i){
		cin >> a;
		if(a > 0) ++pos;
		else if(a < 0) ++neg;
		else ++zer;
	}
	streamsize ss = cout.precision();
	cout << fixed << setprecision(6)
		<< pos/n << "\n" << neg/n << "\n" << zer/n << "\n";
	return 0;
}
