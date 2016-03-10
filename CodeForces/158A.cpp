#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, k; cin >> n >> k;
	vector<int> a;
	while(n--){ //fills vector
		int i; cin >> i;
		a.push_back(i);
	}
	int count = 0;
	int s = a[k-1]; //set score goal
	for(auto &i: a){ //counts numbers greater than goal
		if(i > 0 && i >= s) ++count;
	}
	cout << count;
	return 0;
}
