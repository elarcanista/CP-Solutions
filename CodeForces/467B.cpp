#include <bits/stdc++.h>
using namespace std;

int count_equals(int a, int b){ //count bit differences using ~(a <-> b)
	return ~((a&b)|(~a&~b));      // a <-> b  == (a & b) | (~a & ~b)
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n, m, k; cin >> n >> m >> k;
	vector<int> players;
	for(int i = 0; i < m; ++i){
		int temp; cin >> temp;
		players.push_back(temp);
	}
	int fedor; cin >> fedor;
	int sum = 0;
	for(auto &a: players){
		int r = count_equals(a, fedor); //count diffences
		bitset<32> s(r);  ///tell how many 1s are there
		if(s.count() <= k) ++sum;
	}
	cout << sum << "\n";
	return 0;
}
