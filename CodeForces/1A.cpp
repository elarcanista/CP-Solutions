//Author: Andres Felipe Ortega Montoya
//CodeForces 1A - Theatre Square
#include <iostream>
#include <stdio.h>
using namespace std;
 
int main() {
	long long a, b, c;
	while((cin >> a >> b >> c)){
		long long base = a/c;
		if(a%c != 0){
			++base;
		}
		long long height = b / c;
		if(b % c != 0){
			++height;
		}
		cout << (base * height);
	}
	return 0;
}
