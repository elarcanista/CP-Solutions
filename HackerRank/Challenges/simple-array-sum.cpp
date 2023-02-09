//Author: Andres Felipe Ortega Montoya
//HackerRank - Simple Array Sum
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int a, b, c = 0;
	cin >> a;
	while(a--){
		cin >> b;
		c += b;
	}
	cout << c;
	return 0;
}
