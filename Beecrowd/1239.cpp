//Author: Andrés Felipe Ortega Montoya
//Bloggo Shortcuts
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

void convert(string s){
	bool ast = false;
	bool und = false;
	for(int i = 0; i < s.size(); ++i){
		if(s[i] == '*'){
			if(!ast){
				cout << "<b>";
				ast = true;
			}else{
				cout << "</b>";
				ast = false;
			}
		}else if(s[i] == '_'){
			if(!und){
				cout << "<i>";
				und = true;
			}else{
				cout << "</i>";
				und = false;
			}
		}else cout << s[i];
	}
	cout << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string s;
	while(getline(cin, s)){
		convert(s);
	}
	return 0;
}
