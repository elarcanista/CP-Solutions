//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string line;
	while(getline(cin, line) && line != "*"){
		int counter = 0;
		int good = 0;
		for(int i = 1; i < line.size(); ++i){
			if(line[i] == '/'){
				good += (counter == 64)? 1: 0;
				counter = 0;
			}else if(line[i] == 'W')
				counter += 64;
			else if(line[i] == 'H')
				counter += 32;
			else if(line[i] == 'Q')
				counter += 16;
			else if(line[i] == 'E')
				counter += 8;
			else if(line[i] == 'S')
				counter += 4;
			else if(line[i] == 'T')
				counter += 2;
			else 
				counter += 1;
		}
		cout << good << "\n";
	}
	return 0;
}
