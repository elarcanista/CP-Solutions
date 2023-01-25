//Author: Andres Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
bool vowel(char s){
	//cout << s << " " << ((s == 'A') || (s == 'E') || (s == 'I') || (s == 'O') || (s == 'U') || (s == 'Y'));	
	return ((s == 'A') || (s == 'E') || (s == 'I') || (s == 'O') || (s == 'U') || (s == 'Y'));	
} 
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string str;
	while(cin >> str){
		int maxi = 0;
		int last = -1;
		for(int i = 0; i < str.size(); ++i){
			if(vowel(str[i])){
				if(i-last > maxi){
					maxi = i-last;
				}
				last = i;
			}
		}
		if(str.size()-last > maxi){
			maxi = str.size()-last;
		}
		cout << maxi << "\n";
	}
	return 0;
}