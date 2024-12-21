// https://www.hackerrank.com/challenges/compare-the-triplets/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int a[3], b, a1 = 0, b1 = 0;
	for(int i = 0; i < 3; ++i){
		cin >> a[i];
	}
	for(int i = 0; i < 3; ++i){
		cin >> b;
		if(a[i] > b) ++a1;
		else if(a[i] < b) ++b1;
	}
	cout << a1 << " " << b1;
	return 0;
}
