//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int m[39];
int n[39];

int fib(int a){
	if (m[a] != -1) return m[a];
	m[a] = fib(a-1) + fib(a-2) + 2;
	return m[a];
}

int fib2(int a){
	if (n[a] != -1) return n[a];
	n[a] = fib2(a-1) + fib2(a-2);
	return n[a];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	memset(m, -1, sizeof(m));
	memset(n, -1, sizeof(n));
	m[0] = 0;
	m[1] = 0;
	n[0] = 0;
	n[1] = 1;
	while(TC--){
		int temp; cin >> temp;
		cout << "fib(" << temp << ") = " << fib(temp) << " calls = " << fib2(temp) << "\n";
	}
	return 0;
}
