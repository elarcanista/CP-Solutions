//Author: Andres Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, a, b; cin >> n;
	a = b = 0;
	int arr[n][n];
	for(int i = 0; i < n; ++i){
		for(int j = 0; j < n; ++j){
			cin >> arr[i][j];
		}
	}
	for(int i = 0; i < n; ++i){
		a += arr[i][i];
		b += arr[i][n-i-1];
	}
	cout << abs(a-b);
	return 0;
}
