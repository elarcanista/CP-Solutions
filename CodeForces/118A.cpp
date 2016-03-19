#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	string out = "";
	string str;
	cin >> str;
	for(int i = 0; i < str.size(); ++i){
		char c = tolower(str[i]);
		if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'y'){
			cout << '.';
			cout << c;
		}
	}
	cout << out;
	return 0;
}
