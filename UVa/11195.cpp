//Author: Andres Felipe Ortega Montoya
//UVa 11195 - Another n-Queen Problem
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INFI = 1 << 30;
const ll INFLL = 1LL << 62;

vector<string> s;
int queens;
bitset<30> rw, ld, rd;

void queen(int m, int n){
	if(m == n){
		++queens;
		return;
	}
	for(int i = 0; i < n; ++i){
		if(s[m][i] != '*' && !rw[i] && !ld[m-i+n-1] && !rd[m+i]){
			rw[i] = ld[m-i+n-1] = rd[m+i] = true;
			queen(m+1, n);
			rw[i] = ld[m-i+n-1] = rd[m+i] = false;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, TC = 1;
	while(cin >> n && n){
		queens = 0;
		s.clear();
		char c;
		string str;
		for(int i = 0; i < n; ++i){
			cin >> str;
			s.push_back(str);
		}
		queen(0, n);
		cout << "Case " << TC++ << ": " << queens << "\n";
	}
	return 0;
}
