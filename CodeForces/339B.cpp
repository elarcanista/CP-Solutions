#include <bits/stdc++.h>
using namespace std;

int main() {
	long long n, m, in, last = 1, count = 0;
	cin >> n >> m;
	while(m--){
		cin >> in;
		if (in >= last){
			count += in - last;
		}else{
			count += (n-last) + in;
		}
		last = in;
	}
	cout << count;
}
