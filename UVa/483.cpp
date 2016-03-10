#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string str;
	while(getline(cin,str)){ //read by lines
		stringstream ss;
		ss << str; //split line by words
		string word;
		ss >> word;
		for(int i = word.size()-1; i >= 0; --i){ //prints words backward
			cout << word[i];
		}
		while(ss >> word){	
			cout << " ";
			for(int i = word.size()-1; i >= 0; --i){
				cout << word[i];
			}
		}
		cout << '\n';
	}
	return 0;
}
