// https://www.hackerrank.com/challenges/a-very-big-sum/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll a, b, c = 0;
	cin >> a;
	for(int i = 0; i < a; ++i){
		cin >> b;
		c += b;
	}
	cout << c;
	return 0;
}
