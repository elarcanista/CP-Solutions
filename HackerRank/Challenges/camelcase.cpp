//Author: Andres Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    string str;
    int counter = 1;
    while(cin >> str){
        for(int i = 0; i < str.size(); ++i){
            if(str[i] >= 'A' && str[i] <= 'Z') ++counter;
        }
        cout << counter << "\n";
    }
	return 0;
}