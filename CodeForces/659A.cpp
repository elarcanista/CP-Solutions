//Author: Andrés Felipe Ortega Montoya
//Codeforces 659A - Round House
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, k, l; cin >> n >> k >> l;
	int ans = ((k+l) % (n));
	if(ans < 0) ans = (n-ans)%n;
	else ans = (n+ans)%n;
	if(ans) cout << ans;
	else cout << n;
	return 0;
}
