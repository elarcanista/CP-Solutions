#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

map<string, string> d;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m; cin >> n >> m;
	while(m--){
		string a, b; cin >> a >> b;
		d[a] = (b.size() < a.size())? b: a;
	}
	while(n--){
		string in; cin >> in;
		cout << d[in] << ((n)? " ": "");
	}
	return 0;
}
