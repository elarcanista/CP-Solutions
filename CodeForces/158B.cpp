//Author: Andres Felipe Ortega Montoya
//CodeForces 158B - Taxi
#include <iostream>
#include <stdio.h>

using namespace std;
 
int main() {
	long long a, four = 0, three = 0, two= 0, one= 0;
	cin >> a;
	for(long long i = 0; i < a; i++){
		int b;
		cin >> b;
		if(b == 4) ++four;
		if(b == 3) ++three;
		if(b == 2) ++two;
		if(b == 1) ++one;
	}
	if(three > one){
		one = 0;
	}else{
		one = one - three;
	}
	one += (two % 2) * 2;
	two /= 2;
	if(one % 4 == 0){
		one /= 4;
	}else{
		one /=4;
		++one;
	}
	cout << four + three + two + one;
	return 0;
}
