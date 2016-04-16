//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	double n;
	cout << fixed << setprecision(0);
	while(cin >> n && n != -1){
	  //j(j+1)/2 - i(i+1)/2 + i = n
		for(double i = 1; i <= n; ++i){ //tries values for lower bound
			double c = 2*n + i*(i - 1); //this must be equals to j(j+1)
			double j = (-1 + sqrt(1 + 4*c)) / 2; //calculates j from j^2 + j - c = 0
			if(j == ceil(j)){ //if the answer is exact then it is the answer
				cout << n << " = " << i << " + ... + " << j << "\n";
				break;
			}
		}
	}
	return 0;
}
