//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string a; cin >> a;
	int b[7];
	int pos = 0;
	for(int i = 1; i < a.size(); ++i){
		if(a[i] == '0') b[pos-1] *= 10;
		else b[pos++] = a[i]-'0';
	}
	int sum = 0;
	for(int i = 0; i < pos; ++i){
		sum += b[i];
	}
	cout << sum +1;
	return 0;
}