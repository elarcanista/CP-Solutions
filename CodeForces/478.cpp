#include <bits/stdc++.h>
using namespace std;

int sum(int n){
	return n*(n+1)/2;
}

int few(int p, int g){                        //creates groups of equal number of contestans
	return sum(ceil((float)p/g)-1)*g - p%g;
}

int much(int p, int g){                       //creates several groups of 1's and one of the remainder people
	return sum(p-g);
}

int main() {
	int p, g; cin >> p >> g;
	cout << few(p, g) << " " << much(p, g) << "\n";
	return 0;
}
