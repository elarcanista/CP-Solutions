#include <bits/stdc++.h>
using namespace std;
//UVa 11498 - Division of Nlogonia

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC;
	int n, m;
	while(cin >> TC, TC != 0){ // read until gets a 0
		cin >> n >> m; // x and y coodinates of the division
		while(TC--){ // does TC test cases
			int x, y;
			cin >> x >> y;
			char cood[2]; // cood[0] = x axys, cood[1] y axys
			if(x == n || y == m){ // if is on a border
				cout << "divisa\n";	
				continue;
			} 
			if(x > n) cood[0] = 'E'; // prints its section
			else cood[0] = 'O';
			if(y > m) cood[1] = 'N';
			else cood[1] = 'S';
			cout << cood[1] << cood[0] << '\n';
		}
	}
	return 0;
}
