//Author: Andrés Felipe Ortega Montoya
//Uva 10491 - Cows and Cars
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	double v,c,s; 
	while(cin >> v >> c >> s){
		double a = v/(v+c) * c/(v+c-s-1);
		double b = c/(v+c) * (c-1)/(v+c-s-1);
		cout << fixed << setprecision(5) << a+b << "\n";
	}
	return 0;
}
