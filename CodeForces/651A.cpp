#include <iostream>
using namespace std;

int main() {
	int a, b, count = 0;
	cin >> a >> b;
	while(true){
		if(a == 1 && b == 1) break;
		++count;
		if(a <= 2 && b <= 2) break;
		if(a < b){
			++a;
			b -= 2;
		}else{
			++b;
			a -= 2;
		}
	}
	cout << count;
	return 0;
}
