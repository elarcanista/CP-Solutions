#include <bits/stdc++.h>
using namespace std;
//UVa 272 - TEX Quotes 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string str;
	bool open = false; // true if we are inside quotes
	while(getline(cin, str)){ // reads input by lines
		for(int i = 0; i < str.size(); ++i){
			if(str[i] == '\"'){ // check if we opened or closed quotes and prints
				if(!open){
					cout << "``";
					open = true;
				}else{
					cout << "''";
					open = false;
				}
			}else{
				cout << str[i]; // prints everything that is not a quote 
			}
		} 
		cout << "\n";
	}
	return 0;
}
